from pydantic import BaseModel

class ObjectiveSpecification(BaseModel):

    goal: str

    deliverables: list[str]

    constraints: list[str]

    required_agents: list[str]

    success_criteria: list[str]