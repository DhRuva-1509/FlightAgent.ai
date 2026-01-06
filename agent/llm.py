from openai import OpenAI

def get_llm():
    return OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )
