import json
import re
from typing import List

from ai import llm


PROMPT = """Below is some python code:
{code}

Extract the pip packages that need to be installed and get their corresponsing names in pip.
Package names in the imports and in pip might be different. Use the correct pip names.
Include only the packages that need to be installed with pip.
                            
Put them in a valid JSON:
```
{{
    "packages": List of packages. If no packages, empty list.
}}
```"""


CODE_LABEL = "EXECUTE_PYTHON"
CHAT_LABEL = "CHAT"


def get_packages(code: str) -> List[str]:
    formatted_prompt = PROMPT.format(code=code)
    reponse = llm.next([{"role": "user", "content": formatted_prompt}])
    return _parse_response(reponse)


def _parse_response(response: str) -> List[str]:
    # Can throw
    json_str = re.search("({.*})", response, re.DOTALL).group(0)  # type: ignore
    return json.loads(json_str)["packages"]
