import json
import traceback
from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple

from code_exec import execute_code
from tasks import analyzer, chat, code
from tasks.analyzer import TaskTree
from utils.io import print_assistant, print_system, user_input

FOUR_K_TOKENS = 16000


class Conversation(List[Dict[str, str]]):
    def __init__(self, iterable):
        super().__init__(iterable)

    def add_assistant(self, message: str) -> "Conversation":
        return self.add("assistant", message)

    def add_system(self, message: str) -> "Conversation":
        return self.add("system", message)

    def add_user(self, message: str) -> "Conversation":
        return self.add("user", message)

    def add_function(self, name: str, message: str) -> "Conversation":
        self.append({"role": "function", "name": name, "content": message})
        return self

    def add(self, role: str, message: str) -> "Conversation":
        self.append({"role": role, "content": message})
        return self

    def copy(self) -> "Conversation":
        return deepcopy(self)


def run(_conversation: List[Dict[str, str]] = []) -> None:
    conversation = Conversation(_conversation)

    while True:
        ai_action = chat.next_action(conversation)

        if not ai_action["function"]:
            conversation.add_assistant(ai_action["message"])
            user_message = user_input()
            conversation.add_user(user_message)
        else:
            if ai_action["function"]["name"] != "special_task":
                conversation.add_function(
                    ai_action["function"]["name"],
                    f"There is no function named {ai_action['function']['name']}",
                )
                continue

            try:
                arguments = json.loads(ai_action["function"]["arguments"])
            except:
                tb = traceback.format_exc()
                conversation.add_function(
                    ai_action["function"]["name"],
                    f"There was an error parsing the arguments of the function_call {ai_action['function']['name']}. They must be a valid json: {tb}",
                )
                print_system(json.dumps(ai_action, indent=2))
                print_system(tb)
                breakpoint()
                continue

            task_tree = build_solvable_tree(Conversation([]), arguments["task"])

            if not task_tree.is_solvable or task_tree.unsolvable_subtasks:
                print_assistant(f"Task is unsolvable for now.")
                break

            print_assistant(f"Will execute:")
            print_assistant(str(task_tree))
            confirmation = user_input('"n" to stop: ')
            if confirmation == "n":
                break

            atomic_tasks = find_atomic_tasks(task_tree)

            output = execute_tasks(task_tree.task, atomic_tasks)
            conversation.add_function(
                name=ai_action["function"]["name"], message=output
            )


def build_solvable_tree(conversation: Conversation, task: str) -> TaskTree:
    conversation.add_user(f"Task: {task}")
    task_breakdown = analyzer.task_breakdown(conversation)

    if task_breakdown.is_atomic:
        return TaskTree(
            task=task,
            is_solvable=True,
            is_atomic=True,
            solvable_subtasks=[],
            unsolvable_subtasks=[],
        )

    if task_breakdown.subtasks:
        # These trees have not be analyzed
        solvable_subtasks = [
            TaskTree(
                task=s.task,
                is_solvable=True,
                is_atomic=None,
                solvable_subtasks=None,
                unsolvable_subtasks=None,
            )
            for s in task_breakdown.subtasks
            if s.is_code_solvable
        ]
        unsolvable_subtasks = [
            TaskTree(
                task=s.task,
                is_solvable=False,
                is_atomic=None,
                solvable_subtasks=None,
                unsolvable_subtasks=None,
            )
            for s in task_breakdown.subtasks
            if not s.is_code_solvable
        ]

        if unsolvable_subtasks:
            return TaskTree(
                task=task,
                is_atomic=False,
                is_solvable=False,
                solvable_subtasks=solvable_subtasks,
                unsolvable_subtasks=unsolvable_subtasks,
            )

        subtasks = [s.task for s in task_breakdown.subtasks]
        conversation.add_assistant(str({"is_atomic": "false", "subtasks": subtasks}))

        subtask_trees = []
        for subtask in solvable_subtasks:
            subtask_tree = build_solvable_tree(conversation.copy(), subtask.task)
            if not subtask_tree.is_solvable:
                raise AssertionError(
                    "Code that was said code-solvable before is not code-solvable."
                )
            subtask_trees.append(subtask_tree)
        return TaskTree(
            task=task,
            is_atomic=False,
            is_solvable=True,
            solvable_subtasks=subtask_trees,
            unsolvable_subtasks=[],
        )
    raise ValueError("Subtasks should be present.")


def find_atomic_tasks(task_tree: TaskTree) -> List[TaskTree]:
    assert (
        task_tree.is_solvable and not task_tree.unsolvable_subtasks
    ), "Atomic tasks must be solvable."

    if task_tree.is_atomic:
        return [task_tree]

    assert (
        task_tree.solvable_subtasks
    ), "No solvable subtasks found when looking for atomic tasks."
    return [t for s in task_tree.solvable_subtasks for t in find_atomic_tasks(s)]


def execute_tasks(main_task: str, tasks: List[TaskTree]) -> str:
    subtasks: List[Tuple[str, Optional[str]]] = [(t.task, None) for t in tasks]
    output = None
    for i, task in enumerate(subtasks):
        function_info = code.get(main_task, subtasks, i)
        subtasks[i] = (task[0], function_info.code)
        print_system(function_info.code)
        breakpoint()

    if not output:
        output = "Task executed but no information returned."

    return output


def exec_code(
    script: str, pip_install: Optional[str]
) -> Tuple[Optional[str], Optional[Dict[str, Any]], Any, Optional[str]]:
    try:
        func_name, inputs, output, stdout = execute_code(script, pip_install)
        if output is not None and len(output) >= FOUR_K_TOKENS:
            output = "Function output is too long for the context window."
        if stdout is not None:
            output_len = len(output) if output else 0
            if output_len + len(stdout) >= FOUR_K_TOKENS:
                stdout = "Function standard output is too long for the context window."
        return func_name, inputs, output, stdout
    except Exception:
        return (
            None,
            None,
            f"There was an error executing the function: {traceback.format_exc()}",
            None,
        )


if __name__ == "__main__":
    run()
