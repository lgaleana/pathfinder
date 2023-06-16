import re
import traceback
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional, Tuple

from code_exec import get_func_params, get_function_by_exec, install_packages
from tasks import chat, code, pip
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
            packages, code = get_packages_and_code(conversation)
            print_system(code)
            print_system(f"Will install the following packages: {packages}")
            if packages is not None and code:
                try:
                    func_name, output = run_code(packages, code)
                    system_message = f"""Python function executed: {func_name}
Python packages installed: {packages}
Python function output: {output}"""
                    print_system(system_message)
                    break
                except Exception:
                    tb = traceback.format_exc()
                    print_system(tb)
                    system_message = f"The function that you wrote produced the following error: {tb}"
                conversation.append({"role": "system", "content": system_message})


def get_packages_and_code(
    conversation: List[Dict[str, str]]
) -> Tuple[Optional[List[str]], Optional[str]]:
    for message in reversed(conversation):
        if message["role"] == "assistant" and re.search(
            "[```|```python]\n(.*)\n```", message["content"], re.DOTALL
        ):
            with ThreadPoolExecutor() as executor:
                pip_f = executor.submit(pip.get_packages, message["content"])
                code_f = executor.submit(code.extract, message["content"])
                return pip_f.result(), code_f.result()
    return None, None


def run_code(
    packages: List[str],
    code: str,
) -> Tuple[str, Any]:
    install_packages(packages)

    func = get_function_by_exec(code)
    if func:
        input_names = get_func_params(func)
        params = {}
        print_system("Function inputs")
        for name in input_names:
            params[name] = user_input(f"{name}: ")

        print_system("Running function...")
        output = func(*params.values())
        print_system(output)

        return func.__name__, output
    raise Exception("No function found.")


if __name__ == "__main__":
    run()
