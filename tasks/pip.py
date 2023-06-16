import json
import re
from typing import List

from ai import llm


PROMPT = """From a text, extract the packages that need to be installed and get their corresponding names in pip.
Package names in the imports and in pip might be different. Use the correct names.
Include only the packages that need to be installed with pip.

Put them in a valid JSON:
```
{{
    "packages": List of packages. If no packages, empty list.
}}

Examples:

Input: from googlesearch import search
def google_search(query):
    results = []
    for result in search(query, num_results=5):
        results.append(result)
    return results
Output: {{
    "packages": ["googlesearch-python"]
}}

Input: {text}
```"""


def get_packages(text: str) -> List[str]:
    formatted_prompt = PROMPT.format(text=text)
    reponse = llm.next([{"role": "user", "content": formatted_prompt}])
    return _parse_response(reponse)


def _parse_response(response: str) -> List[str]:
    # Can throw
    json_str = re.search("({.*})", response, re.DOTALL).group(0)  # type: ignore
    return json.loads(json_str)["packages"]
