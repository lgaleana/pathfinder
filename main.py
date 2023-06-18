from contextlib import redirect_stdout
from io import StringIO
import re
import json
import traceback
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional, Tuple

from code_exec import get_func_params, get_function_by_exec, install_packages
from tasks import chat, code, pip
from utils.io import print_system, user_input


def run(conversation: List[Dict[str, str]] = []) -> None:
    while True:
        ai_action = chat.next_action(conversation)
        print_system(ai_action)

        if not ai_action["function"]:
            conversation.append({"role": "assistant", "content": ai_action["message"]})
            user_message = user_input()
            conversation.append({"role": "user", "content": user_message})
        else:
            system_message = None
            try:
                code = json.loads(ai_action["function"]["arguments"])["function"]
                code = extract_function(code)
                print_system(code)
                packages = pip.get_packages(code)
                print_system(f"Will install the following packages: {packages}")
                if packages is not None and code:
                    func_name, inputs, output, stdout = run_code(packages, code)
                    system_message = f"""Function executed: {func_name}
Packages installed: {packages}
Function inputs: {inputs}
Function output: {output}
Standard output: {stdout}"""
                print_system(system_message)
            except Exception:
                system_message = traceback.format_exc()
                print_system(system_message)
                breakpoint()
            conversation.append(
                {
                    "role": "function",
                    "name": ai_action["function"]["name"],
                    "content": str(system_message),
                }
            )


def run_code(
    packages: List[str],
    code: str,
) -> Tuple[str, Dict[str, Any], Any, str]:
    func = get_function_by_exec(code)
    if func:
        params = get_func_params(func)
        resolved_params = {}
        print_system("Function inputs")
        for name, param in params.items():
            param_value = user_input(f"{name}: ")
            if param.annotation is not param.empty:
                resolved_params[name] = param.annotation(param_value)
            else:
                resolved_params[name] = param_value

        install_packages(packages)
        print_system("Running function...")
        stdout = StringIO()
        with redirect_stdout(stdout):
            output = func(*resolved_params.values())
        if stdout.getvalue():
            print_system(stdout.getvalue())
        print_system(output)

        return func.__name__, resolved_params, output, stdout.getvalue()
    raise Exception("No function found to execute.")


def extract_function(script: str) -> str:
    keep_lines = []
    for line in script.split("\n"):
        if (
            line.startswith("import")
            or line.startswith("from")
            or line.startswith("def")
            or line.startswith("    ")  # Very naive
        ):
            keep_lines.append(line)
    return "\n".join(keep_lines)


if __name__ == "__main__":
    run()
