from planner.planner import Planner
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

plan = planner.create_plan(objective)

print(
    json.dumps(
        plan,
        indent=4
    )
)