
from promptflow import tool
from promptflow.connections import CustomConnection
from openai import OpenAI


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def classify_intent(connection: CustomConnection, system_prompt: str, user_prompt: str) -> str:

    #endpoint_url = 'https://Llama-2-7b-chat-gmqyf-serverless.westus3.inference.ai.azure.com'
    #api_key = 'b7JHHhhMlMim8i8g1YzXBNCb5WSnQGzI'

    endpoint_url = connection['endpoint_url']
    api_key = connection['endpoint_api_key']

    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    base_url = endpoint_url + '/v1'
    client = OpenAI(
        base_url = base_url,
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model="Llama-2-7b-chat-gmqyf", # model = "deployment_name".
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )

    return response.choices[0].message.content
