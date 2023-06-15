from typing import Dict, List

from ai import llm


PROMPT = """
You are a helpful AI assistant.
You have one tool at your disposal, which you can use at any time. The tool is to execute python code that you write yourself. All you need to do is say EXECUTE_PYTHON and the last python code that you wrote will be executed. Whenever you want to use this tool, it must be at the end of your message.
"""


def next_message(conversation: List[Dict[str, str]]) -> Dict[str, str]:
    return llm.stream_next([{"role": "system", "content": PROMPT}] + conversation)
