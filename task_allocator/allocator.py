from agent_registry.registry import AgentRegistry


class TaskAllocator:

    def __init__(self):

        self.registry = AgentRegistry()

    def allocate(
        self,
        task
    ):

        agent_name = task["agent"]

        agent = self.registry.get_agent(
            agent_name
        )

        return {
            "task": task,
            "assigned_agent": agent_name,
            "agent_details": agent
        }