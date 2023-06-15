import inspect
import subprocess
import sys
from typing import Callable, List, Optional


def install_packages(packages: List[str]) -> None:
    for p in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", p])


def get_function_by_exec(script: str) -> Optional[Callable]:
    exec(script, locals())

    locals_ = locals()
    for var in reversed(locals_.values()):
        # Try to run all local functions
        if callable(var):
            return var
    return None


def get_func_params(func: Callable) -> List[str]:
    sig = inspect.signature(func)
    return list(sig.parameters.keys())