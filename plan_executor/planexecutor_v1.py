from executor.executor import AgentExecutor


class PlanExecutor:

    def __init__(self):

        self.executor = AgentExecutor()

    def execute_plan(
        self,
        plan
    ):

        results = []

        for task in plan["tasks"]:

            result = self.executor.execute(
                task
            )

            results.append(
                result
            )

        return results