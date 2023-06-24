from typing import List, Optional

from pydantic import BaseModel, Field

from ai import llm
from utils.io import print_system


class SubTask(BaseModel):
    task: str = Field(description="Description of the subtask.")
    is_code_solvable: bool = Field(description="Can it be solved with code?")


class TaskBreakdown(BaseModel):
    is_atomic: bool = Field(
        description="Could you write a one python function to accomplish this task?"
    )
    subtasks: Optional[List[SubTask]] = Field(None, description="List of subtasks.")


FUNCTIONS = [
    {
        "name": "answer",
        "description": "Answer the questions.",
        "parameters": TaskBreakdown.schema(),
    }
]

PROMPT = """You are an assistant that analyzes a task and decides what is the best way to accomplish it. Ideally, you want to write python code to accomplish the task.

Be resourceful. For example,
- To do a google search you can write a function that calls an api to do a google search.
- To visit a website, you can write a function that scrapes the website.

Answer the following questions:
- Could you write a one python function to accomplish this task? yes/no.
- If no,
    - How would you break it apart into more subtasks?
    - For each subtask, can it be solved with code? yes/no."""


def task_breakdown(task: str) -> TaskBreakdown:
    print_system(task)
    _, answer = llm.stream_next(
        [
            {"role": "system", "content": PROMPT},
            {"role": "system", "content": f"Task: {task}"},
        ],
        model="gpt-4-0613",
        functions=FUNCTIONS,
        function_call={"name": "answer"},  # type: ignore
    )
    print_system(answer["arguments"])
    return TaskBreakdown.parse_raw(answer["arguments"])
