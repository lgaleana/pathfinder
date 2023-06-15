from typing import Dict, List

from ai import llm


PROMPT = """
You are a helpful AI assistant.
You have one major upgrade. You can execute python functions. To execute a python function, say: EXCUTE_PYTHON. The last python function that you wrote will be executed.

The EXECUTE_PYTHON command has the following constraints:
 1. You must use it at the end of your message.
 2. Your function must be placed in between ```\n...\n```.
 3. You can only execute one python function at a time.

Here is an example:
...
User: I want to do a google search.
Assistant: Sure! I can help you with that. What would you like to search for on Google?
User: Dogs!
Assistant: Here is a python function to do a google search about dogs:

```
python function
```

Would you like me to run that for you?
User: Yes!
Assistant: EXCUTE_PYTHON
System: Python function executed: ...
Python packages installed: ...
Python function output: ...
Assistant: ...


Note that EXCUTE_PYTHON is at the end of your message. Once the function is executed, I will let you know the name of the function, what packages were installed and what it returned.
"""


def next_message(conversation: List[Dict[str, str]]) -> Dict[str, str]:
    return llm.stream_next([{"role": "system", "content": PROMPT}] + conversation)
