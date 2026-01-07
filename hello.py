import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models, what is the future of ai and beyond",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print("=" * 80)
print("AI RESPONSE:")
print("=" * 80)
print(chat_completion.choices[0].message.content)
print("\n" + "=" * 80)
print("METADATA:")
print("=" * 80)
print(f"Model: {chat_completion.model}")
print(f"Finish Reason: {chat_completion.choices[0].finish_reason}")
print(f"Total Tokens: {chat_completion.usage.total_tokens}")
print(f"Prompt Tokens: {chat_completion.usage.prompt_tokens}")
print(f"Completion Tokens: {chat_completion.usage.completion_tokens}")
print("=" * 80)
