from litellm import completion

response = completion(
    model="ollama/qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": "Explain Google ADK in one sentence."
        }
    ]
)

print(response.choices[0].message.content)