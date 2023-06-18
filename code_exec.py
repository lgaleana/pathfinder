import inspect
import subprocess
import sys
from typing import Callable, List, Optional


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
