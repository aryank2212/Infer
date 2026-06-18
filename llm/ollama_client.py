import requests


class OllamaClient:

    def generate(self, prompt):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "lfm2.5",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]