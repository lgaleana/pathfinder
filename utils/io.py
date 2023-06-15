def print_system(message: str = "") -> str:
    print(f"\033[0;0m{message}")
    return message


def print_assistant(message: str = "", end: str = "\n", flush: bool = False) -> str:
    print(f"\033[92m{message}", end=end, flush=flush)
    return message


def user_input() -> str:
    return input("\033[1;34m")
