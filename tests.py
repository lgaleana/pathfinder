from unittest import TestCase

from main import run


class TestPip(TestCase):
    def test_google_search(self):
        run(
            [
                {"role": "assistant", "content": "Hello! How can I assist you today?"},
                {"role": "user", "content": "i want to do a google search"},
                {
                    "role": "assistant",
                    "content": "Sure! I can help you with that. What would you like to search for on Google?",
                },
                {"role": "user", "content": "dogs"},
                {
                    "role": "assistant",
                    "content": "Here is a python function to do a google search about dogs:\n\n```\ndef google_search(query):\n    from googlesearch import search\n    \n    results = []\n    for result in search(query, num_results=5):\n        results.append(result)\n    \n    return results\n```\n\nWould you like me to run that for you?",
                },
                {"role": "user", "content": "yes"},
            ]
        )

    def test_many_attempts_google_search(self):
        run(
            [
                {"role": "assistant", "content": "Hello! How can I assist you today?"},
                {"role": "user", "content": "i want to do a google search"},
                {
                    "role": "assistant",
                    "content": "Sure! I can help you with that. What would you like to search for on Google?",
                },
                {"role": "user", "content": "dogs"},
                {
                    "role": "assistant",
                    "content": "Here is a python function to do a google search about dogs:\n\n```\ndef google_search(query):\n    from googlesearch import search\n    \n    results = []\n    for result in search(query, num_results=5):\n        results.append(result)\n    \n    return results\n```\n\nWould you like me to run that for you?",
                },
                {"role": "user", "content": "yes"},
                {"role": "assistant", "content": ""},
                {
                    "role": "system",
                    "content": 'The function you wrote returned the following exception: Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 34, in run\n    output = func(*params.values())\n  File "<string>", line 5, in google_search\nTypeError: search() got an unexpected keyword argument \'num_results\'\n',
                },
                {
                    "role": "assistant",
                    "content": "It seems that there is an issue with the `googlesearch` package. The `search` function does not have a `num_results` parameter. Let me modify the function for you:\n\n```\ndef google_search(query, num_results=5):\n    from googlesearch import search\n    \n    results = []\n    for result in search(query, num_results=num_results):\n        results.append(result)\n    \n    return results\n```\n\nWould you like me to run the modified function for you?",
                },
                {"role": "user", "content": "yes"},
                {"role": "assistant", "content": ""},
                {
                    "role": "system",
                    "content": 'The function you wrote returned the following exception: Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 34, in run\n    output = func(*params.values())\n  File "<string>", line 5, in google_search\nTypeError: search() got an unexpected keyword argument \'num_results\'\n',
                },
                {
                    "role": "assistant",
                    "content": 'I apologize for the inconvenience. It seems that the `googlesearch` package does not have a `num_results` parameter. Let me modify the function for you:\n\n```\ndef google_search(query, num_results=5):\n    from googlesearch import search\n    \n    results = []\n    for i, result in enumerate(search(query, num_results=num_results), start=1):\n        results.append(f"Result {i}: {result}")\n    \n    return results\n```\n\nWould you like me to run the modified function for you?',
                },
                {"role": "user", "content": "yes"},
                {"role": "assistant", "content": ""},
                {
                    "role": "system",
                    "content": 'The function you wrote returned the following exception: Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 34, in run\n    output = func(*params.values())\n  File "<string>", line 5, in google_search\nTypeError: search() got an unexpected keyword argument \'num_results\'\n',
                },
                {
                    "role": "assistant",
                    "content": "I apologize for the inconvenience. It seems that the `googlesearch` package does not have a `num_results` parameter. Let me modify the function for you:\n\n```\ndef google_search(query):\n    from googlesearch import search\n    \n    results = []\n    for result in search(query, num_results=5):\n        results.append(result)\n    \n    return results\n```\n\nWould you like me to run the modified function for you?",
                },
                {"role": "user", "content": "yes"},
                {"role": "assistant", "content": ""},
                {
                    "role": "system",
                    "content": 'The function you wrote returned the following exception: Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 34, in run\n    output = func(*params.values())\n  File "<string>", line 5, in google_search\nTypeError: search() got an unexpected keyword argument \'num_results\'\n',
                },
            ]
        )
