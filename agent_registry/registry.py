import json


class AgentRegistry:

    def __init__(self):

        with open(
            "agent_registry/agents.json",
            "r"
        ) as f:

            self.agents = json.load(f)

    def get_agent(
        self,
        agent_name
    ):

        return self.agents.get(
            agent_name
        )

    def list_agents(self):

        return self.agents.keys()