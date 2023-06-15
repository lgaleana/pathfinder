import inspect
import subprocess
import sys
from typing import Callable, List, Optional


def install_packages(packages: List[str]) -> None:
    for p in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", p])
