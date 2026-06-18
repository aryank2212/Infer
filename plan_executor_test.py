from planner.planner import Planner
from plan_executor.executor import PlanExecutor

import json


planner = Planner()

objective = {
    "goal": "Build Project Management SaaS",

    "deliverables": [
        "Frontend",
        "Backend",
        "Database"
    ],

    "constraints": [],

    "required_agents": [
        "coding_agent",
        "research_agent"
    ],

    "success_criteria": [
        "Users can create projects"
    ]
}

plan = planner.create_plan(
    objective
)

executor = PlanExecutor()

result = executor.execute_plan(
    plan
)

print(
    json.dumps(
        result,
        indent=4
    )
)