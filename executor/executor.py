from worker_agents.research_agent import ResearchAgent
from worker_agents.coding_agent import CodingAgent
from worker_agents.verification_agent import VerificationAgent


class AgentExecutor:

    def __init__(self):

        self.agents = {
            "research_agent": ResearchAgent(),
            "coding_agent": CodingAgent(),
            "verification_agent": VerificationAgent()
        }

    def execute(self, task):

        agent_name = task["agent"]

        agent = self.agents.get(
            agent_name
        )

        if not agent:
            raise Exception(
                f"Unknown agent: {agent_name}"
            )

        return agent.execute(task)