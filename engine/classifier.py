import json
import os

from anthropic import Anthropic

from prompts.classifier import CLASSIFIER_PROMPT
from schemas.decision_schema import DecisionOutput

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


def classify(user_input: str) -> DecisionOutput:

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        temperature=0,
        system=CLASSIFIER_PROMPT,
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    result = response.content[0].text

    data = json.loads(result)

    return DecisionOutput(**data)