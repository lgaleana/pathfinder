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

    def test_multiple_attempts_google_search(self):
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
                {"role": "assistant", "content": "EXECUTE_PYTHON"},
                {
                    "role": "system",
                    "content": 'The function that you wrote produced the following error: Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 70, in run_code\n    output = func(*params.values())\n  File "<string>", line 5, in google_search\nTypeError: search() got an unexpected keyword argument \'num_results\'\n',
                },
                {
                    "role": "assistant",
                    "content": "I apologize for the error. It seems that the `googlesearch` package does not have a `num_results` parameter in its `search` function. Let me update the function for you:\n\n```\ndef google_search(query):\n    from googlesearch import search\n    \n    results = []\n    for result in search(query, num=5):\n        results.append(result)\n    \n    return results\n```\n\nWould you like me to run the updated function for you?",
                },
                {"role": "user", "content": "yes"},
            ]
        )

    def test_google_search_too_many_requests(self):
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
                {"role": "assistant", "content": "EXECUTE_PYTHON"},
                {
                    "role": "system",
                    "content": 'The function that you wrote produced the following error: Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 70, in run_code\n    output = func(*params.values())\n  File "<string>", line 5, in google_search\nTypeError: search() got an unexpected keyword argument \'num_results\'\n',
                },
                {
                    "role": "assistant",
                    "content": "I apologize for the error. It seems that the `googlesearch` package does not have a `num_results` parameter in its `search` function. Let me update the function for you:\n\n```\ndef google_search(query):\n    from googlesearch import search\n    \n    results = []\n    for result in search(query, num=5):\n        results.append(result)\n    \n    return results\n```\n\nWould you like me to run the updated function for you?",
                },
                {"role": "user", "content": "yes"},
                {"role": "assistant", "content": "EXECUTE_PYTHON"},
                {
                    "role": "system",
                    "content": 'The function that you wrote produced the following error: Traceback (most recent call last):\n  File "/Users/lgaleana/pathfinder/main.py", line 70, in run_code\n    output = func(*params.values())\n  File "<string>", line 5, in google_search\n  File "/Users/lgaleana/pathfinder/venv/lib/python3.9/site-packages/googlesearch/__init__.py", line 305, in search\n    html = get_page(url, user_agent, verify_ssl)\n  File "/Users/lgaleana/pathfinder/venv/lib/python3.9/site-packages/googlesearch/__init__.py", line 174, in get_page\n    response = urlopen(request)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 214, in urlopen\n    return opener.open(url, data, timeout)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 523, in open\n    response = meth(req, response)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 632, in http_response\n    response = self.parent.error(\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 555, in error\n    result = self._call_chain(*args)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 494, in _call_chain\n    result = func(*args)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 747, in http_error_302\n    return self.parent.open(new, timeout=req.timeout)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 523, in open\n    response = meth(req, response)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 632, in http_response\n    response = self.parent.error(\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 561, in error\n    return self._call_chain(*args)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 494, in _call_chain\n    result = func(*args)\n  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 641, in http_error_default\n    raise HTTPError(req.full_url, code, msg, hdrs, fp)\nurllib.error.HTTPError: HTTP Error 429: Too Many Requests\n',
                },
                {
                    "role": "assistant",
                    "content": "I apologize, but it seems that the function encountered an HTTP Error 429: Too Many Requests. This error occurs when there are too many requests being made to the Google search engine in a short period of time.\n\nTo avoid this error, I recommend adding a delay between each request. Here's an updated version of the function:\n\n```\nimport time\nfrom googlesearch import search\n\ndef google_search(query):\n    results = []\n    for result in search(query, num_results=5):\n        results.append(result)\n        time.sleep(1)  # Add a 1-second delay between requests\n    \n    return results\n```\n\nWould you like me to run the updated function for you?",
                },
                {"role": "user", "content": "do you know the serp api?"},
                {
                    "role": "assistant",
                    "content": "Yes, I'm familiar with the SERP API. It is a service that allows you to retrieve search engine results programmatically. With the SERP API, you can get search results from various search engines, including Google, Bing, Yahoo, and more.\n\nIf you would like to use the SERP API for your Google search, I can provide you with a Python function that utilizes the API. Would you like me to do that?",
                },
                {"role": "user", "content": "yes"},
                {
                    "role": "assistant",
                    "content": 'To use the SERP API for your Google search, you will need to sign up for an account and obtain an API key. Once you have your API key, you can use the following Python function to make a request to the SERP API and retrieve the search results:\n\n```python\nimport requests\n\ndef serp_api_search(query, api_key):\n    url = f"https://api.serpapi.com/search?q={query}&engine=google&api_key={api_key}"\n    \n    response = requests.get(url)\n    data = response.json()\n    \n    results = []\n    for result in data.get("organic_results", []):\n        title = result.get("title")\n        link = result.get("link")\n        snippet = result.get("snippet")\n        \n        results.append({\n            "title": title,\n            "link": link,\n            "snippet": snippet\n        })\n    \n    return results\n```\n\nMake sure to replace `api_key` with your actual API key. This function sends a GET request to the SERP API endpoint with the specified query and API key. It then extracts the relevant information from the JSON response and returns a list of dictionaries containing the title, link, and snippet of each search result.\n\nWould you like me to run this function for you?',
                },
                {"role": "user", "content": "use the python package"},
                {
                    "role": "assistant",
                    "content": 'Certainly! To use the `serpapi` Python package, you will need to install it first. Please run the following command to install the package:\n\n```\n!pip install serpapi\n```\n\nOnce the package is installed, you can use the following Python function to make a request to the SERP API and retrieve the search results:\n\n```python\nfrom serpapi import GoogleSearch\n\ndef serpapi_search(query, api_key):\n    params = {\n        "q": query,\n        "engine": "google",\n        "api_key": api_key\n    }\n    \n    search = GoogleSearch(params)\n    results = search.get_dict().get("organic_results", [])\n    \n    return results\n```\n\nMake sure to replace `api_key` with your actual API key. This function creates a `GoogleSearch` object with the specified query and API key. It then retrieves the search results as a dictionary and returns the list of organic results.\n\nWould you like me to run this function for you?',
                },
                {
                    "role": "user",
                    "content": "the name of the package is google-search-results",
                },
                {
                    "role": "assistant",
                    "content": 'Apologies for the confusion. If you are referring to the `google-search-results` package, please run the following command to install it:\n\n```\n!pip install google-search-results\n```\n\nOnce the package is installed, you can use the following Python function to make a request to the Google Search Results API and retrieve the search results:\n\n```python\nfrom serpapi import GoogleSearch\n\ndef google_search_results(query, api_key):\n    params = {\n        "q": query,\n        "api_key": api_key\n    }\n    \n    search = GoogleSearch(params)\n    results = search.get_dict().get("organic_results", [])\n    \n    return results\n```\n\nMake sure to replace `api_key` with your actual API key. This function creates a `GoogleSearch` object with the specified query and API key. It then retrieves the search results as a dictionary and returns the list of organic results.\n\nWould you like me to run this function for you?',
                },
                {"role": "user", "content": "yes"},
            ]
        )
