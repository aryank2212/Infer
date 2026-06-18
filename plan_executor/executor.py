from task_allocator.allocator import TaskAllocator
from executor.executor import AgentExecutor


class PlanExecutor:

    def __init__(self):

        self.allocator = TaskAllocator()
        self.executor = AgentExecutor()

    def execute_plan(self, plan):

        results = []

        for task in plan["tasks"]:

            allocation = self.allocator.allocate(
                task
            )

            result = self.executor.execute(
                task
            )

            results.append({
                "allocation": allocation,
                "result": result
            })

        return {
            "status": "completed",
            "results": results
        }