import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "lfm2.5",
        "prompt": "Say hello",
        "stream": False
    }
)

print(response.json()["response"])