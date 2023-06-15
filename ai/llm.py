import os
from typing import Any, Dict, List, Optional

import openai
from dotenv import load_dotenv

from utils.io import print_assistant

load_dotenv()


openai.api_key = os.environ["OPENAI_KEY_PERSONAL"]
MODEL = "gpt-3.5-turbo-16k-0613"
TEMPERATURE = 0


def call(
    messages: List[Dict[str, str]],
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    stop: Optional[str] = None,
    stream: Optional[bool] = None,
) -> Dict[str, Any]:
    if not model:
        model = MODEL
    if temperature is None:
        temperature = TEMPERATURE

    return openai.ChatCompletion.create(  # type: ignore
        model=model,
        messages=messages,
        temperature=temperature,
        stop=stop,
        stream=stream,
    )


def next(
    messages: List[Dict[str, str]],
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    stop: Optional[str] = None,
) -> str:
    return call(messages, model, temperature, stop)["choices"][0]["message"]["content"]


def stream_next(
    messages: List[Dict[str, str]],
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    stop: Optional[str] = None,
) -> str:
    response = call(messages, model, temperature, stop, stream=True)

    next_ = ""
    for chunk in response:
        delta = chunk["choices"][0]["delta"]  # type: ignore
        if "content" in delta and delta["content"]:  # type: ignore
            next_ += delta["content"]  # type: ignore
            print_assistant(delta["content"], end="", flush=True)  # type: ignore
    print_assistant()
    return next_
