from executor.executor import AgentExecutor
import json

executor = AgentExecutor()

task = {
    "id": "TASK_001",

    "name": "Build Backend API",

    "description":
    "Create a REST API for project management",

    "agent": "coding_agent",

    "expected_output":
    "Production ready API",

    "context": {
        "language": "Python",
        "framework": "FastAPI",
        "database": "PostgreSQL"
    }
}

result = executor.execute(task)

print(
    json.dumps(
        result,
        indent=4
    )
)