import requests
import json

from planner.prompts import PLANNER_PROMPT


class Planner:

    def __init__(self):
        self.model = "lfm2.5"

    def create_plan(self, objective):

        prompt = f"""
{PLANNER_PROMPT}

Objective:

{json.dumps(objective, indent=4)}
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "format": "json"
            }
        )

        data = response.json()

        return json.loads(data["response"])