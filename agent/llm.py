import json
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv(override=True)

local_llm = OpenAI(base_url= os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

MODEL = "gemma3:latest"

SYSTEM_PROMPT = """
You are a helpful assistant for an Airline called FLIGHTAGENT.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.
"""

def chat_completion(messages, tools = None):
    return local_llm.chat.completions.create(
        model= MODEL,
        messages= messages,
        tools= tools
    )

def summarize_conversation(history):
    prompt = f"""
Summarize the following conversation in 2 short sentences:

{history}
"""
    response = local_llm.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content