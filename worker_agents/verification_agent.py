from worker_agents.base_agent import BaseAgent
from llm.ollama_client import OllamaClient
from result_processor.processor import ResultProcessor


class VerificationAgent(BaseAgent):

    def __init__(self):

        self.llm = OllamaClient()
        self.processor = ResultProcessor()

    def execute(self, task):

        code = task["generated_output"]

        prompt = f"""
You are a senior software reviewer.

Review the following output.

Check:

1. Correctness
2. Missing components
3. Bugs
4. Scalability
5. Security

Return:

VERDICT:
PASS or FAIL

ISSUES:
...

IMPROVEMENTS:
...

Output:

{code}
"""

        result = self.llm.generate(
            prompt
        )

        result = self.processor.clean(
            result
        )

        return {
            "status": "completed",
            "task_id": task["id"],
            "agent": "verification_agent",
            "output": result
        }