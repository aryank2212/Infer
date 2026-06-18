import requests
import json

prompt = """
Return ONLY valid JSON.

{
    "request_type":"",
    "objective_type":"",
    "complexity":"",
    "requires_planning":true,
    "requires_human_clarification":false,
    "priority":1,
    "confidence":0.0
}

Request:
Monitor all GitHub repositories and notify me of failures.
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "lfm2.5",
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }
)

data = response.json()

parsed = json.loads(data["response"])

print("\nPARSED JSON:\n")
print(json.dumps(parsed, indent=4))