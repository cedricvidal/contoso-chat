from promptflow import tool
import json


@tool
def extract_intent(input: str) -> str:
    try:
        answer = json.loads(input)
    except:
        print("Error parsing intent {}".format(input))
        return 'error'
    intent = answer['intent']
    print("Intent: " + intent)
    return intent
