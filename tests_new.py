from goal_analyzer.analyzer import GoalAnalyzer
import json

analyzer = GoalAnalyzer()

result = analyzer.analyze(
    "Build a complete SaaS application for project management."
)

print(json.dumps(result, indent=4))