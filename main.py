import re
import traceback
from typing import Dict, List, Optional

from code_exec import get_func_params, get_function_by_exec, install_packages
from tasks import chat, pip
from tasks.chat import CHAT_LABEL
from utils.io import print_system, user_input


def run(conversation: List[Dict[str, str]] = []) -> None:
    while True:
        ai_action = chat.next_action(conversation)
        conversation.append({"role": "assistant", "content": ai_action["message"]})

        if ai_action["label"] == CHAT_LABEL:
            user_message = user_input()
            conversation.append({"role": "user", "content": user_message})
        else:
            code = get_last_code_in_conversation(conversation)
            if code:
                print_system(code)
                packages = pip.get_packages(code)
                print_system(f"Will install the following packages: {packages}")
                install_packages(packages)
                func = get_function_by_exec(code)
                if func:
                    input_names = get_func_params(func)
                    params = {}
                    for name in input_names:
                        params[name] = user_input(f"{name}: ")

                    try:
                        output = func(*params.values())
                        print_system(output)
                        conversation.append(
                            {
                                "role": "system",
                                "content": f"The function you wrote returned the following: {output}",
                            }
                        )
                    except Exception as e:
                        tb = traceback.format_exc()
                        print_system(tb)
                        conversation.append(
                            {
                                "role": "system",
                                "content": f"The function you wrote returned the following exception: {tb}",
                            }
                        )


def get_last_code_in_conversation(conversation: List[Dict[str, str]]) -> Optional[str]:
    for message in reversed(conversation):
        if message["role"] == "assistant":
            for code in reversed(
                re.findall("[```|```python]\n(.*)\n```", message["content"], re.DOTALL)
            ):
                if code:
                    return code
    return None


if __name__ == "__main__":
    run()
