from promptflow import tool
import json


@tool
def extract_intent(input: str) -> str:
    answer = json.loads(input)
    return answer['intent']
