from agent.llm import get_llm
from agent.tools import TOOLS, handle_tool_calls

llm = get_llm()

SYSTEM_PROMPT = """
You are a flight booking assistant.
If required information is missing, ask the user.
Do NOT call tools with empty or placeholder values.
"""

def chat(message, history):
    history = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history + [{"role": "user", "content": message}]

    response = llm.chat.completions.create(
        model="llama3.2:3b",
        messages=messages,
        tools=TOOLS
    )

    while response.choices[0].finish_reason == "tool_calls":
        tool_message = response.choices[0].message
        tool_responses = handle_tool_calls(tool_message)
        messages.append(tool_message)
        messages.extend(tool_responses)

        response = llm.chat.completions.create(
            model="llama3.2:3b",
            messages=messages,
            tools=TOOLS
        )

    return response.choices[0].message.content
