from promptflow import tool
import json


@tool
def extract_intent(input: str) -> str:
    try:
        answer = json.loads(input)
    except:
        return 'error'
    return answer['intent']
