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
