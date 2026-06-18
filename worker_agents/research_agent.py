from worker_agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):

    def execute(self, task):

        return {
            "status": "completed",
            "task_id": task["id"],
            "agent": "research_agent",
            "output": f"Research completed for {task['name']}"
        }