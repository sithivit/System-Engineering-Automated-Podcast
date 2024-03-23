from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api = openai_api = os.environ.get("OPENAI_API_KEY")

def check_script(script):
    checker = OpenAI(api_key=api).chat.completions
    response = checker.create(
        messages=[
            {"role": "system", "content": "Can you check if this podcast script make sense by editing part that doesn't fit in, and leave good part untouched"},
            {"role": "user", "content": script}
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content