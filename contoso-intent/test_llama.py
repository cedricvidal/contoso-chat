
from openai import OpenAI
from os import environ as env
from dotenv import load_dotenv

def classify_intent(prompt: str) -> str:

    load_dotenv("../.env")
    endpoint_url = env.get('LLAMA_ENDPOINT')
    api_key = env.get('LLAMA_KEY')

    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    base_url = endpoint_url + '/v1'
    client = OpenAI(
        base_url = base_url,
        api_key=api_key,
    )

    deployment_name = "Llama-2-7b-chat-gmqyf"

    # COMPLETION API
    response = client.completions.create(
        model=deployment_name,
        prompt=prompt,
        stop="STOP",
        temperature=0.5,
        max_tokens=128,
        top_p=0.1,
        best_of=1,
        presence_penalty=0,
    )

    return response.choices[0].text.strip()

# python entry point
if __name__ == "__main__":
    print(classify_intent("What is the weather like today?"))
