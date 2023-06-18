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

    def test_katana_kitten(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {
                    "role": "user",
                    "content": "can you get me the opening hours of katana kitten?",
                },
                {
                    "role": "function",
                    "name": "execute_function",
                    "content": 'Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 27, in run\n    packages, func_name, inputs, output, stdout = run_code(code)\n  File "/Users/lgaleana/pathfinder/main.py", line 76, in run_code\n    output = func(*resolved_params.values())\n  File "<string>", line 7, in get_opening_hours\nAttributeError: \'NoneType\' object has no attribute \'text\'\n',
                },
                {
                    "role": "assistant",
                    "content": 'Sure! I can help you with that. Here\'s a Python function that retrieves the opening hours of Katana Kitten:\n\n```python\nimport requests\nfrom bs4 import BeautifulSoup\n\ndef get_opening_hours():\n    url = "https://www.katanakitten.com/"\n    response = requests.get(url)\n    soup = BeautifulSoup(response.text, "html.parser")\n    opening_hours = soup.find("div", class_="hours").text.strip()\n    return opening_hours\n```\n\nWould you like me to execute this function for you?',
                },
                {"role": "user", "content": "yeah"},
                {
                    "role": "function",
                    "name": "execute_function",
                    "content": 'Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 27, in run\n    packages, func_name, inputs, output, stdout = run_code(code)\n  File "/Users/lgaleana/pathfinder/main.py", line 76, in run_code\n    output = func(*resolved_params.values())\n  File "<string>", line 7, in get_opening_hours\nAttributeError: \'NoneType\' object has no attribute \'text\'\n',
                },
                {
                    "role": "assistant",
                    "content": "I apologize, but it seems that there was an error while executing the function. It appears that the website structure may have changed, causing the function to fail in retrieving the opening hours.\n\nIs there anything else I can assist you with?",
                },
                {
                    "role": "user",
                    "content": "make no assumptions of the structure of the website. just return all text, no html and no empty lines",
                },
                {
                    "role": "assistant",
                    "content": 'Understood! Here\'s an updated Python function that retrieves all the text from the website without any HTML tags and empty lines:\n\n```python\nimport requests\nfrom bs4 import BeautifulSoup\n\ndef get_website_text(url):\n    response = requests.get(url)\n    soup = BeautifulSoup(response.text, "html.parser")\n    text = soup.get_text(separator="\\n").strip()\n    text = "\\n".join(line for line in text.split("\\n") if line.strip())\n    return text\n```\n\nYou can use this function by providing the URL of the website you want to retrieve the text from. Would you like me to execute this function for you?',
                },
                {"role": "user", "content": "yeah"},
            ]
        )
