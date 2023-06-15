import re
import traceback
from typing import Any, Dict, List, Optional, Tuple

from code_exec import get_func_params, get_function_by_exec, install_packages
from tasks import chat, pip
from tasks.chat import CHAT_LABEL
from utils.io import print_system, user_input


def run(conversation: List[Dict[str, str]] = []) -> None:
    while True:
        ai_action = chat.next_action(conversation)
        conversation.append({"role": "assistant", "content": ai_action["message"]})

        if ai_action["label"] == CHAT_LABEL:
            user_message = user_input()
            conversation.append({"role": "user", "content": user_message})
        else:
            code = get_last_code_in_conversation(conversation)
            print_system(code)
            if code:
                packages = pip.get_packages(code)
                err, func_name, output = run_code(packages, code)

                if not err:
                    system_message = f"""Python function executed: {func_name}
Python packages installed: {packages}
Python function output: {output}"""
                else:
                    system_message = f"The function that you wrote produced the following error: {err}"
                conversation.append({"role": "system", "content": system_message})


def get_last_code_in_conversation(conversation: List[Dict[str, str]]) -> Optional[str]:
    code = None
    for message in reversed(conversation):
        if message["role"] == "assistant":
            for potential_code in reversed(
                re.findall("[```|```python]\n(.*)\n```", message["content"], re.DOTALL)
            ):
                # Append all code in this message
                if potential_code:
                    if not code:
                        code = potential_code
                    else:
                        code = f"{code}\n\n{potential_code}"
            if code:
                break
    return code


def run_code(
    packages: List[str],
    code: str,
) -> Tuple[Optional[str], Optional[str], Any]:
    print_system(f"Will install the following packages: {packages}")
    install_packages(packages)

    func = get_function_by_exec(code)
    if func:
        input_names = get_func_params(func)
        params = {}
        print_system("Function inputs")
        for name in input_names:
            params[name] = user_input(f"{name}: ")

        try:
            print_system("Running function...")
            output = func(*params.values())
            print_system(output)

            return None, func.__name__, output
        except Exception:
            tb = traceback.format_exc()
            print_system(tb)
            return tb, None, None

    return (
        "The function that you wrote produced the following error: No function found",
        None,
        None,
    )


if __name__ == "__main__":
    run()
