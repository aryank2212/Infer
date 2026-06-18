from agent_registry.registry import AgentRegistry

registry = AgentRegistry()

print(
    registry.get_agent(
        "coding_agent"
    )
)