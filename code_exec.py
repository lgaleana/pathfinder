import inspect
import subprocess
import sys
from contextlib import redirect_stdout
from io import StringIO
from typing import Any, Dict, Callable, List, Optional, Tuple

from tasks import pip
from utils.io import print_system, user_input


def install_packages(packages: List[str]) -> None:
    for p in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", p])


def get_function_by_exec(script: str) -> Optional[Callable]:
    locals_ = {}
    exec(script, locals_)
    # Find the last declared function
    for var in reversed(locals_.values()):
        if callable(var):
            return var
    return None


def get_func_params(func: Callable):
    sig = inspect.signature(func)
    return sig.parameters


def extract_imports_and_function(script: str) -> str:
    keep_lines = []
    for line in script.split("\n"):
        if (
            line.startswith("import")
            or line.startswith("from")
            or line.startswith("def")
            or line == ""
            or line.startswith("    ")  # Very naive
        ):
            keep_lines.append(line)
    return "\n".join(keep_lines)


def execute_code(
    script: str,
) -> Tuple[Optional[List[str]], str, Dict[str, Any], Any, str]:
    code = extract_imports_and_function(script)
    print_system(code)
    if code:
        func = get_function_by_exec(code)
        packages = pip.get_packages(code)
        print_system(f"Will install the following packages: {packages}")
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

            if packages is not None:
                install_packages(packages)
            print_system("Running function...")
            stdout = StringIO()
            with redirect_stdout(stdout):
                output = func(*resolved_params.values())
            if stdout.getvalue():
                print_system(stdout.getvalue())
            print_system(output)

            return packages, func.__name__, resolved_params, output, stdout.getvalue()
    raise Exception("No function found to execute.")
