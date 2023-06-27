import json
import re
from typing import Dict, List, Optional, Tuple

from pydantic import BaseModel, Field

from ai import llm
from utils.io import print_system


class FunctionInfo(BaseModel):
    logic: str = Field(description="Explain the function logic.")
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
{previous_subtask_and_function}
Write a function for: "{task}".

To write the function, you must follow the following criteria:
- Include necessary imports.
- Consider the output from previous functions.
- Consider the input of the next task.
- Your function must return something.

Do it in the following steps:
1. Explain the function logic.
2. Write the function code.
3. Do you need to install any packages from pip? yes/no
    3.a. If yes, what is the pip install command to install them?
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
    main_task: str, subtasks: List[Tuple[str, Optional[str]]], idx: int
) -> FunctionInfo:
    prev_subtask_func = "\n"
    if len(subtasks) > 0:
        subtasks_str = ", ".join([f"{i}: {s[0]}" for i, s in enumerate(subtasks)])
        prev_subtask_func = f"\nThis is the breakdown of subtasks to accomplish that task: {subtasks_str}\n\n"
        if idx > 0:
            prev_subtask_func += f'This is the function for the previous task "{subtasks[idx - 1][0]}":\n\n{subtasks[idx - 1][1]}\n\n'
    prompt = PROMPT.format(
        main_task=main_task,
        previous_subtask_and_function=prev_subtask_func,
        task=subtasks[idx][0],
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
