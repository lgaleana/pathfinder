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
                    "content": "Here is a python function to do a google search about dogs:\n\n```\nfrom googlesearch import search\n\ndef google_search(query: str):\n    results = []\n    for result in search(query, num=5):\n        results.append(result)\n    return results\n```\n\nWould you like me to run that for you?",
                },
                {"role": "user", "content": "yes"},
            ]
        )

    def test_serp(self):
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
                    "content": "Here is a python function to do a google search about dogs:\n\n```\nfrom googlesearch import search\n\ndef google_search(query: str):\n    results = []\n    for result in search(query, num=5):\n        results.append(result)\n    return results\n```\n\nWould you like me to run that for you?",
                },
                {"role": "user", "content": "yes"},
                {"role": "assistant", "content": "EXECUTE_PYTHON"},
                {
                    "role": "system",
                    "content": 'The function that you wrote produced the following error: Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 26, in run\n    func_name, inputs, output = run_code(packages, code)\n  File "/Users/lgaleana/pathfinder/main.py", line 72, in run_code\n    output = func(*resolved_params.values())\n  File "<string>", line 5, in google_search\n  File "/Users/lgaleana/pathfinder/venv/lib/python3.9/site-packages/googlesearch/__init__.py", line 305, in search\n    html = get_page(url, user_agent, verify_ssl)\n  File "/Users/lgaleana/pathfinder/venv/lib/python3.9/site-packages/googlesearch/__init__.py", line 174, in get_page\n    response = urlopen(request)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 214, in urlopen\n    return opener.open(url, data, timeout)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 523, in open\n    response = meth(req, response)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 632, in http_response\n    response = self.parent.error(\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 555, in error\n    result = self._call_chain(*args)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 494, in _call_chain\n    result = func(*args)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 747, in http_error_302\n    return self.parent.open(new, timeout=req.timeout)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 523, in open\n    response = meth(req, response)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 632, in http_response\n    response = self.parent.error(\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 561, in error\n    return self._call_chain(*args)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 494, in _call_chain\n    result = func(*args)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 641, in http_error_default\n    raise HTTPError(req.full_url, code, msg, hdrs, fp)\nurllib.error.HTTPError: HTTP Error 429: Too Many Requests\n',
                },
                {
                    "role": "assistant",
                    "content": "I apologize, but it seems that there was an error while executing the function. The error message indicates that there were too many requests made to the server. This could be due to rate limiting or other restrictions imposed by the website.\n\nIs there anything else I can assist you with?",
                },
                {"role": "user", "content": "do you know the serp api?"},
                {
                    "role": "assistant",
                    "content": "Yes, I'm familiar with the SERP API. The SERP API (Search Engine Results Page API) is a service that allows you to retrieve search engine results programmatically. It provides a convenient way to access search results from various search engines, such as Google, Bing, Yahoo, and more.\n\nWith the SERP API, you can retrieve search results, including organic search results, paid advertisements, featured snippets, and other search features. You can also specify search parameters, such as the search query, location, language, and device type, to get customized search results.\n\nIf you have any specific questions or need assistance with using the SERP API, feel free to ask!",
                },
                {
                    "role": "user",
                    "content": "can you write a function that uses the serp api?",
                },
            ]
        )
