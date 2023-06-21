from typing import Any, Dict, List

from ai import llm
from utils.io import print_system


FUNCTIONS = [
    {
        "name": "execute_function",
        "description": "Execute a python function.",
        "parameters": {
            "type": "object",
            "properties": {
                "function": {
                    "type": "string",
                    "description": "The function definition.",
                },
            },
            "required": ["function"],
        },
    }
]

PROMPT = """You are a helpful AI assistant.
You can execute python functions from code that you write yourself. Consider this to be a tool that you can use to accomplish a variety of tasks.

Example:
Assistant: Hi! How can I help you today?
User: I want to do a google search.
Assistant: Sure! I can help you with that. Here's a Python function that performs a Google search:

```
# imports
# def function
```

Let me know if you would like me to execute this function for you.
User: Yes, please!
Assistant: {
    "name": "execute_function",
    "arguments": "{"function": "#imports\n#def function"}"
}

Always show the function first and confirm with the user whether you should execute it. Work with the user and use your best judegement to determine when is the right moment to execute a function.
"""


def next_action(conversation: List[Dict[str, str]]) -> Dict[str, Any]:
    print_system(conversation)
    message, function_ = llm.stream_next(
        [{"role": "system", "content": PROMPT}] + conversation,
        functions=FUNCTIONS,
        model="gpt-3.5-turbo-16k-0613",
    )
    return {"message": message, "function": function_}
