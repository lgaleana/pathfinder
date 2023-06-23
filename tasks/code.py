import json
import re
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from ai import llm
from utils.io import print_system


class FunctionInfo(BaseModel):
    logic: str = Field(description="Logic of the code.")
    code: str = Field(description="The function code.")
    pip_install: Optional[str] = Field(None, description="pip install command")


FUNCTIONS = [
    {
        "name": "steps",
        "description": "Write a python function.",
        "parameters": FunctionInfo.schema(),
    }
]

PROMPT = """You are an assistant that writes clever, readable python code. You have been asked to write a python function to accomplish a task.

Do it in the following steps:
1. Explain the logic in your code.
2. Write the function code. If you need data from the user, make it part of the function parameters. Add type hints to the function parameters. Include necessary imports.
3. If there are pip packages that need to be installed, provide the pip install command."""


def get(conversation: List[Dict[str, str]]) -> FunctionInfo:
    print_system(conversation)
    _, function = llm.stream_next(
        conversation + [{"role": "system", "content": PROMPT}],
        functions=FUNCTIONS,
        function_call={"name": "steps"},  # type: ignore
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
