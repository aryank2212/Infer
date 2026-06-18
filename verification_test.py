from worker_agents.verification_agent import VerificationAgent
import json

agent = VerificationAgent()

task = {
    "id": "VERIFY_001",

    "generated_output": """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home()
    return {"hello":"world"}
"""
}

result = agent.execute(task)

print(
    json.dumps(
        result,
        indent=4
    )
)