import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen2.5:7b",
    "prompt": "What is Google ADK? Explain in one sentence.",
    "stream": False
}

response = requests.post(url, json=data)

print(response.json()["response"])