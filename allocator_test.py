from task_allocator.allocator import TaskAllocator
import json

allocator = TaskAllocator()

task = {
    "id": "TASK_001",
    "name": "Build Backend API",
    "agent": "coding_agent"
}

result = allocator.allocate(task)

print(
    json.dumps(
        result,
        indent=4
    )
)