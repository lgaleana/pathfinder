import re
from typing import Dict, List, Optional

from code_exec import install_packages
from tasks import chat, pip
from tasks.chat import CHAT_LABEL
from utils.io import user_input


conversation = []


def get_last_code_in_conversation(conversation: List[Dict[str, str]]) -> Optional[str]:
    for message in reversed(conversation):
        if message["role"] == "assistant":
            for code in reversed(
                re.findall("[```|```python]\n(.*)\n```", message["content"], re.DOTALL)
            ):
                if code:
                    return code
    return None


while True:
    ai_action = chat.next_action(conversation)
    conversation.append({"role": "assistant", "content": ai_action["message"]})

    if ai_action["label"] == CHAT_LABEL:
        user_message = user_input()
        conversation.append({"role": "user", "content": user_message})
    else:
        code = get_last_code_in_conversation(conversation)
        if code:
            packages = pip.get_packages(code)
            install_packages(packages)
            print(packages)
        break
