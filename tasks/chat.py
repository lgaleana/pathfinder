from typing import Any, Dict, List

from ai import llm
from utils.io import print_system


FUNCTIONS = [
    {
        "name": "special_task",
        "description": "Executes a task that otherwise you would be unable to do.",
        "parameters": {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string",
                    "description": "The description of the task to accomplish.",
                },
            },
            "required": ["task"],
        },
    }
]

PROMPT = """You are a helpful AI assistant.

Here are some examples of how to call the special_task function:
- special_task(Do a google search about dogs)
- special_task(Visit openai.com and summarize it)

Say hi."""


def next_action(conversation: List[Dict[str, str]]) -> Dict[str, Any]:
    print_system(conversation)
    message, function_ = llm.stream_next(
        [{"role": "system", "content": PROMPT}] + conversation,
        functions=FUNCTIONS,
    )
    return {"message": message, "function": function_}
