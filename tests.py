import requests
import json

prompt = """
You are a classification engine.

You MUST choose ONLY from these values.

REQUEST_TYPE:
NEW_OBJECTIVE
STATUS_QUERY
DIRECT_COMMAND
OBJECTIVE_UPDATE
CONVERSATION
CLARIFICATION

OBJECTIVE_TYPE:
RESEARCH
CODING
MONITORING
AUTOMATION
ANALYSIS
SYSTEM
GENERAL

COMPLEXITY:
LOW
MEDIUM
HIGH

If you use any value not listed above, your answer is wrong.

Return ONLY JSON.

{
    "request_type":"NEW_OBJECTIVE",
    "objective_type":"CODING",
    "complexity":"HIGH",
    "requires_planning":true,
    "requires_human_clarification":false,
    "priority":1,
    "confidence":0.0
}

Request:

Build a complete SaaS application.
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