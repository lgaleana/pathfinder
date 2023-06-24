import json
import traceback
from copy import deepcopy
from typing import Dict, List, Optional

from code_exec import execute_code
from tasks import analyzer, chat
from tasks.analyzer import TaskTree
from utils.io import print_system, user_input

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
            print_system(task_tree)
            break


def build_solvable_tree(conversation: Conversation, task: str) -> TaskTree:
    conversation.add_user(f"Task: {task}")
    task_breakdown = analyzer.task_breakdown(conversation)

    if task_breakdown.is_atomic:
        return TaskTree(
            task=task,
            is_code_solvable=True,
            is_atomic=True,
            solvable_subtasks=[],
            unsolvable_subtasks=[],
        )

    if task_breakdown.subtasks:
        # These trees have not be analyzed
        solvable_subtasks = [
            TaskTree(
                task=s.task,
                is_code_solvable=True,
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
                is_code_solvable=False,
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
                is_code_solvable=False,
                solvable_subtasks=solvable_subtasks,
                unsolvable_subtasks=unsolvable_subtasks,
            )

        subtasks = [s.task for s in task_breakdown.subtasks]
        conversation.add_assistant(str({"is_atomic": "false", "subtasks": subtasks}))

        subtask_trees = []
        for subtask in solvable_subtasks:
            subtask_tree = build_solvable_tree(conversation.copy(), subtask.task)
            if not subtask_tree.is_code_solvable:
                raise AssertionError(
                    "Code that was said code-solvable before is not code-solvable."
                )
            subtask_trees.append(subtask_tree)
        return TaskTree(
            task=task,
            is_atomic=False,
            is_code_solvable=True,
            solvable_subtasks=solvable_subtasks,
            unsolvable_subtasks=[],
        )
    raise ValueError("Subtasks should be present.")


# From previous code
def exec_code(code: str, pip_install: Optional[str]) -> str:
    try:
        func_name, inputs, output, stdout = execute_code(code, pip_install)
        if output is not None and len(output) >= FOUR_K_TOKENS:
            system_message = "Function output is too long for the context window."
        else:
            system_message = f"""Function executed: {func_name}
Packages installed: {pip_install}
Function inputs: {inputs}
Function output: {output}"""
            if len(stdout) < FOUR_K_TOKENS:
                system_message += f"\n Standard output: {stdout}"
        print_system(system_message)
    except Exception:
        system_message = (
            f"There was an error executing the function: {traceback.format_exc()}"
        )
        print_system(system_message)
    return system_message


if __name__ == "__main__":
    run()
