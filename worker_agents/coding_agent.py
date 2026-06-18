from worker_agents.base_agent import BaseAgent
from llm.ollama_client import OllamaClient
from result_processor.processor import ResultProcessor


class CodingAgent(BaseAgent):

    def __init__(self):

        self.llm = OllamaClient()
        self.processor = ResultProcessor()

    def build_prompt(self, task):

        context = task.get("context", {})

        language = context.get(
            "language",
            "Not Specified"
        )

        framework = context.get(
            "framework",
            "Not Specified"
        )

        database = context.get(
            "database",
            "Not Specified"
        )

        return f"""
You are a senior software engineer.

Complete the following task.

Task ID:
{task["id"]}

Task Name:
{task["name"]}

Task Description:
{task.get("description", "")}

Expected Output:
{task.get("expected_output", "")}

Technology Context:

Language: {language}
Framework: {framework}
Database: {database}

Requirements:

1. Produce a complete solution.
2. Include code when appropriate.
3. Explain architecture decisions.
4. Do not ask questions.
5. Do not return JSON.
6. Return the final result only.
"""

    def execute(self, task):

        prompt = self.build_prompt(
            task
        )

        raw_output = self.llm.generate(
            prompt
        )

        cleaned_output = self.processor.clean(
            raw_output
        )

        return {
            "status": "completed",
            "task_id": task["id"],
            "agent": "coding_agent",
            "output": cleaned_output
        }