import json
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from ai import llm
from utils.io import print_system


class SubTask(BaseModel):
    task: str = Field(description="Description of the subtask.")
    is_code_solvable: bool = Field(
        description="Can it be accomplished by writing code?"
    )


class TaskBreakdown(BaseModel):
    is_atomic: bool = Field(
        description="Could you write a one python function to accomplish this task?"
    )
    subtasks: Optional[List[SubTask]] = Field(None, description="List of subtasks.")


class TaskTree(BaseModel):
    task: str
    is_solvable: bool
    is_atomic: Optional[bool]
    solvable_subtasks: Optional[List["TaskTree"]]
    unsolvable_subtasks: Optional[List["TaskTree"]]

    def __str__(self):
        return json.dumps(self.dict(), indent=2)


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
    - For each subtask, can it be accomplished by writing code? yes/no."""


def task_breakdown(conversation: List[Dict[str, str]]) -> TaskBreakdown:
    print_system(conversation)
    _, answer = llm.stream_next(
        [{"role": "system", "content": PROMPT}] + conversation,
        model="gpt-4-0613",
        functions=FUNCTIONS,
        function_call={"name": "answer"},  # type: ignore
    )
    print_system(answer["arguments"])
    return TaskBreakdown.parse_raw(answer["arguments"])
