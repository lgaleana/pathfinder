from ai import llm


PROMPT = """The following text has some python code:
{text}

Extract it. Remove anything after the function definition."""


def extract(text: str) -> str:
    formatted_prompt = PROMPT.format(text=text)
    response = llm.next([{"role": "user", "content": formatted_prompt}])
    return response.replace("```python", "").replace("```", "").strip()
