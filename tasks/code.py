import json
import re
from typing import Dict, List

from pydantic import BaseModel, Field

from ai import llm
from utils.io import print_system


class FunctionInfo(BaseModel):
    definition: str = Field(description="The function code.")
    pip_install: str = Field(description="pip install command")


FUNCTIONS = [
    {
        "name": "python_function",
        "description": "Write a python function.",
        "parameters": FunctionInfo.schema(),
    }
]

PROMPT = """You are an assistant that writes readable python code. If you need data from the user, make it part of the function parameters. Add type hints to the function parameters. Include necessary imports. Add the pip install command to install any necessary packages from pip.

Here are some examples of how to call the python_function function:
- python_function("import json\n\n# def function", "")
- python_function("import requests\n\n# def function", "pip install requests")"""


def get(conversation: List[Dict[str, str]]) -> FunctionInfo:
    print_system(conversation)
    _, function = llm.stream_next(
        conversation + [{"role": "system", "content": PROMPT}],
        functions=FUNCTIONS,
        function_call={"name": "python_function"},  # type: ignore
    )
    print_system(function["arguments"])
    return _parse_response(function["arguments"])


def _parse_response(arguments: str) -> FunctionInfo:
    match = re.search('"""(.*)"""', arguments, re.DOTALL)
    if match:
        escaped = json.dumps(match.group(1))
        escaped = re.sub('(""".*""")', f"{escaped}", arguments, flags=re.DOTALL)
    escaped = json.loads(arguments, strict=False)
    return FunctionInfo.parse_obj(escaped)
