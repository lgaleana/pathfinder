import json
import re
from typing import List

from ai import llm


PROMPT = """I will give you a python script. Extract the packages that need to be installed and get their corresponding names in pip. Package names in the imports and in pip might be different. Use the correct names. Include only the necessary packages that need to be installed with pip.

Put them in a valid JSON:
{
    "packages": List of packages. If no packages, empty list.
}

Examples:

Input: from googlesearch import search
def my_function():
    # code
Output: {
    "packages": ["googlesearch-python"]
}
Input: import webbrowser  # There is no need to pip install the webbrowser package
def my_function():
    # code
Output: {
    "packages": []
}
"""


def get_packages(text: str) -> List[str]:
    reponse = llm.next(
        [
            {"role": "user", "content": PROMPT},
            {"role": "user", "content": f"Input: {text}"},
        ]
    )
    return _parse_response(reponse)


def _parse_response(response: str) -> List[str]:
    # Can throw
    json_str = re.search("({.*})", response, re.DOTALL).group(0)  # type: ignore
    return json.loads(json_str)["packages"]
