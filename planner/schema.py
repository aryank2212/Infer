from pydantic import BaseModel


class Task(BaseModel):
    id: str
    name: str
    agent: str


class Plan(BaseModel):
    tasks: list[Task]