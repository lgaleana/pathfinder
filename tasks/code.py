import json
import re
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from ai import llm
from utils.io import print_system


class FunctionInfo(BaseModel):
    logic: str = Field(description="Explain the logic in your function.")
    code: str = Field(description="Write the function code.")
    is_pip_needed: bool = Field(
        description="Do you need to install any packages from pip?"
    )
    pip_install: Optional[str] = Field(
        None, description="what is the pip install command?"
    )


FUNCTIONS = [
    {
        "name": "steps",
        "description": "Follow the steps to write a python function.",
        "parameters": FunctionInfo.schema(),
    }
]

PROMPT = """You are an assistant that writes clever, readable python code.

The ultimate goal is to write code for this task: {main_task}
{subtasks_and_previous_functions}
To write a function, you must follow the following criteria:
- Include necessary imports.
- Consider the output from previous functions.
- Your function must return something.

Do it in the following steps:
1. Explain the logic in your function.
2. Write the function code.
3. Do you need to install any packages from pip? yes/no
    3.a. If yes, what is the pip install command to install them?

Write a function for: {task}.
"""


def _get(conversation: List[Dict[str, str]]) -> FunctionInfo:
    print_system(conversation)
    _, function = llm.stream_next(
        conversation,
        functions=FUNCTIONS,
        function_call={"name": "steps"},  # type: ignore
    )
    print_system(function["arguments"])
    return _parse_response(function["arguments"])


def _parse_response(arguments: str) -> FunctionInfo:
    match = re.search('"""(.*)"""', arguments, re.DOTALL)
    if match:
        escaped = json.dumps(match.group(1))
        arguments = re.sub('(""".*""")', f"{escaped}", arguments, flags=re.DOTALL)
    arguments = json.loads(arguments, strict=False)
    return FunctionInfo.parse_obj(arguments)


def get(
    main_task: str, task: str, subtasks: List[str], previous_functions: List[str]
) -> FunctionInfo:
    subtasks_prev_functions = "\n"
    if len(subtasks) > 0:
        subtasks_prev_functions = f"Subtasks: {subtasks}\n"
    if len(previous_functions) > 0:
        prev_functions = "\n".join([f"{f}\n" for f in previous_functions])
        subtasks_prev_functions = f"{subtasks_prev_functions}\nFunctions implemented so far:\n\n{prev_functions}"
    prompt = PROMPT.format(
        main_task=main_task,
        subtasks_and_previous_functions=subtasks_prev_functions,
        task=task,
    )

    converstaion = [{"role": "user", "content": prompt}]
    function_info = _get(converstaion)
    if function_info.code:
        return function_info

    converstaion.append(
        {"role": "function", "name": "steps", "content": function_info.json()}
    )
    converstaion.append({"role": "user", "content": "Your function has no code."})
    function_info = _get(converstaion)
    if function_info.code:
        return function_info

    raise ValueError("No code provided.")
