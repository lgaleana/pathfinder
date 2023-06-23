import json
import traceback
from copy import deepcopy
from typing import Dict, List

from code_exec import execute_code, extract_imports_and_function
from tasks import analyzer, chat, code
from utils.io import print_system, user_input

FOUR_K_TOKENS = 16000


class Conversation(List[Dict[str, str]]):
    def __init__(self, iterable):
        super().__init__(iterable)

    def add_assistant(self, message: str) -> None:
        self.add("assistant", message)

    def add_system(self, message: str) -> None:
        self.add("system", message)

    def add_user(self, message: str) -> None:
        self.add("user", message)

    def add_function(self, name: str, message: str) -> None:
        self.append({"role": "function", "name": name, "content": message})

    def add(self, role: str, message: str) -> None:
        self.append({"role": role, "content": message})

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

            planner_convo = conversation.copy()
            planner_convo.add_user(str(arguments))
            task_breakdown = analyzer.task_breakdown(planner_convo)
            planner_convo.add_assistant(f"Task breakdown: {task_breakdown.json()}")

            code_convo = Conversation(planner_convo.copy()[-2:])
            user_prompt = "Write a python function for: {}."
            if task_breakdown.is_atomic:
                code_convo.add_user(user_prompt.format(task_breakdown.task))
                function_info = code.get(code_convo)
                code_convo.add_assistant(function_info.json())
                exec_code(function_info.code, function_info.pip_install)
            elif task_breakdown.subtasks:
                if all([t.is_code_solvable for t in task_breakdown.subtasks]):
                    for subtask in task_breakdown.subtasks:
                        if subtask.is_code_solvable:
                            code_convo.add_user(user_prompt.format(subtask.task))
                            function_info = code.get(code_convo)
                            code_convo.add_assistant(function_info.json())
                            print_system(
                                extract_imports_and_function(function_info.code)
                            )
            break


# From previous code
def exec_code(code: str, pip_install: str) -> str:
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
