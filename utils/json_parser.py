import json
import re


def extract_json(text):

    candidates = re.findall(
        r'\{[\s\S]*?\}',
        text
    )

    for candidate in reversed(candidates):

        try:
            return json.loads(candidate)

        except:
            pass

    return None