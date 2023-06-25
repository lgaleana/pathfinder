from typing import Dict, List

from pydantic import BaseModel, Field

from ai import llm
from utils.io import print_system


class Script(BaseModel):
    script: str = Field(description="The script to execute the functions")


FUNCTIONS = [
    {
        "name": "python_script",
        "description": "Write a python script that executes the functions correctly.",
        "parameters": Script.schema(),
    }
]

PROMPT = "Write a python script that executes these functions correctly. Put the output of the last function in a variable named: _end_of_path."


def get(conversation: List[Dict[str, str]]) -> Script:
    print_system(conversation)
    _, function = llm.stream_next(
        conversation + [{"role": "user", "content": PROMPT}],
        functions=FUNCTIONS,
        function_call={"name": "python_script"},  # type: ignore
    )
    print_system(function["arguments"])
    return Script.parse_raw(function["arguments"])
