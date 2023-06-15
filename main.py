from tasks import chat
from utils.io import user_input, print_assistant


conversation = []

while True:
    ai_message = chat.next_message(conversation)
    print_assistant(ai_message)
    conversation.append({"role": "assistant", "content": ai_message})
    user_message = user_input()
    conversation.append({"role": "user", "content": user_message})
