from typing import Dict, List, Optional

from ai import llm
from utils.io import print_system


FUNCTIONS = [
    {
        "name": "answer",
        "description": "Answer the questions.",
        "parameters": {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string",
                    "description": "Description of the task.",
                },
                "is_atomic": {
                    "type": "string",
                    "enum": ["yes", "no"],
                    "description": "Could you write a one python function to accomplish this task?",
                },
                "subtasks": {
                    "type": "string",
                    "description": "List of subtasks. Each in a new line.",
                },
                "is_code_solvable": {
                    "type": "string",
                    "enum": ["yes", "no", "n\a"],
                    "description": "Can each of these subtasks be solved with code?",
                },
                "subtasks_no_code": {
                    "type": "string",
                    "description": "List of subtasks that can't be solved with code. Each in a new line.",
                },
            },
            "required": ["task", "is_atomic"],
        },
    }
]


PROMPT = """You are an assistant that analyzes a task and decides what is the best way to accomplish it. Ideally, you want to write python code to accomplish the task.

Be resourceful. For example,
- To do a google search you can write a function that calls an api to do a google search.
- To visit a website, you can write a function that scrapes the website.

Answer the following questions:
- What is the task?
- Could you write a one python function to accomplish this task? yes/no.
- If no,
    - How would you break it apart into more subtasks?
    - Can each of these subtasks be solved with code? yes/no.
    - If no,
        - Which subtasks can't be solved with code?"""


def task_breakdown(conversation: List[Dict[str, str]]) -> Optional[Dict]:
    print_system(conversation)
    _, answer = llm.stream_next(
        conversation + [{"role": "system", "content": PROMPT}],
        model="gpt-4-0613",
        functions=FUNCTIONS,
        function_call={"name": "answer"},  # type: ignore
    )
    print_system(answer["arguments"])
    return answer["arguments"]
