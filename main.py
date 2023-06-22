import json
import traceback
from typing import Dict, List

from code_exec import execute_code
from tasks import chat, analyzer
from utils.io import print_system, user_input

FOUR_K_TOKENS = 16000


class Conversation(List[Dict[str, str]]):
    def __init__(self, iterable):
        super().__init__(iterable)

    def add_assistant(self, message: str) -> None:
        self.append({"role": "assistant", "content": message})

    def add_system(self, message: str) -> None:
        self.append({"role": "system", "content": message})

    def add_user(self, message: str) -> None:
        self.append({"role": "user", "content": message})

    def add_function(self, name: str, message: str) -> None:
        self.append({"role": "function", "name": name, "content": message})


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

            task_breakdown = analyzer.task_breakdown(
                conversation
                + [
                    {"role": "system", "content": str(arguments)}
                ]  # Doesn't update conversation
            )
            print_system(task_breakdown)
            break


# From previous code
def exec_code(code: str) -> str:
    try:
        packages, func_name, inputs, output, stdout = execute_code(code)
        if output is not None and len(output) >= FOUR_K_TOKENS:
            system_message = "Function output is too long for the context window."
        else:
            system_message = f"""Function executed: {func_name}
Packages installed: {packages}
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
