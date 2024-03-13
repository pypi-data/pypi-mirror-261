import re
import json
import yaml

from .common import DotDict, printd
from .llms import LLM

# Globals
llm = LLM()
with open('prompts.yaml', 'r') as file:
    PROMPTS = DotDict(yaml.safe_load(file))

def query_decomposer(query, prompt=None):
    if prompt is None:
        prompt = PROMPTS.query_decomposer.format(query=query)
    resp = llm.call_api(prompt)
    print(resp)
    resp = DotDict(json.loads(resp))
    return resp

def transform(text_list, encoder_name, prompt=None, is_query=True):
    match encoder_name:
        case 'llm/query_decomposer':
            printd(3, f'encoding with llm/query_decomposer: {text_list}')
            return [query_decomposer(text, prompt=prompt) for text in text_list]
        case _:
            raise ValueError(f'unknown {encoder_name}')


if __name__ == '__main__':
    #read_data()
   query_decomposer("What's the net worth of the fourth richest billionaire in 2023?")