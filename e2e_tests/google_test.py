from unittest import TestCase

from main import run


class TestPip(TestCase):
    def test_google_search(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I help you today?"},
                {"role": "user", "content": "i want to do a google search"},
                {
                    "role": "assistant",
                    "content": "Sure! I can help you with that. Here's a Python function that performs a Google search:\n\n```python\ndef google_search(query: str):\n    # imports\n    from googlesearch import search\n\n    # code\n    for result in search(query, num_results=10):\n        print(result)\n```\n\nLet me know if you would like me to execute this function for you.",
                },
                {"role": "user", "content": "yeah"},
                {
                    "role": "system",
                    "content": 'Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 27, in run\n    func_name, inputs, output = run_code(packages, code)\n  File "/Users/lgaleana/pathfinder/main.py", line 56, in run_code\n    output = func(*resolved_params.values())\n  File "<string>", line 6, in google_search\nTypeError: search() got an unexpected keyword argument \'num_results\'\n',
                },
                {
                    "role": "assistant",
                    "content": "It seems that there is an error in the code. The `search` function from the `googlesearch` library does not have a `num_results` parameter. Let me fix that for you.\n\n```python\ndef google_search(query: str):\n    # imports\n    from googlesearch import search\n\n    # code\n    results = search(query, num_results=10)\n    for result in results:\n        print(result)\n```\n\nWould you like me to execute this updated function for you?",
                },
                {"role": "user", "content": "use num=5 instead of num_results=10"},
                {
                    "role": "assistant",
                    "content": "Sure! Here's the updated code:\n\n```python\ndef google_search(query: str):\n    # imports\n    from googlesearch import search\n\n    # code\n    results = search(query, num=5)\n    for result in results:\n        print(result)\n```\n\nWould you like me to execute this updated function for you?",
                },
                {"role": "user", "content": "yeah"},
            ]
        )
