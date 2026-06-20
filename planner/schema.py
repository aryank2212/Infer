from pydantic import BaseModel


class Task(BaseModel):
    id: str
    name: str
    description: str

    agent: str

    dependencies: list[str]

    priority: int

    expected_output: str


class Plan(BaseModel):
    tasks: list[Task]