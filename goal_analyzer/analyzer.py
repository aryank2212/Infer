import requests
import json

from goal_analyzer.prompts import GOAL_ANALYZER_PROMPT


class GoalAnalyzer:

    def __init__(self):
        self.model = "lfm2.5"

    def analyze(self, objective):

        prompt = f"""
{GOAL_ANALYZER_PROMPT}

User Objective:

{objective}
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