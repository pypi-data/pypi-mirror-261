import subprocess
from openai import OpenAI

try:
    import openai
except ImportError:
    subprocess.run(['pip', 'install', 'openai'])

from openai import OpenAI

client = OpenAI(
    api_key="sk-BpGV5jQSmgyckAq22UIPO9SOpDgjSs9J3VRhh2MrirUMC7Lj", 
    base_url="https://api.chatanywhere.tech/v1"
)

def gpt_35_api_stream(messages: list):
    stream = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages, stream=True)
    for chunk in stream:
        print(chunk.choices[0].delta.content, end="") if chunk.choices and chunk.choices[0].delta.content else None

def gpt():
    text = input('问题：')
    gpt_35_api_stream([{'role': 'user', 'content': text}])

