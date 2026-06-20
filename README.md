# Infer : An AI agent framework that transforms complex objectives into executable plans using specialized agents.
Infer is a Python-based AI agent framework designed to break down complex objectives into actionable plans and execute them using specialized agents.

## Architecture

The system is composed of several key components:

- **Decision Engine**: Classifies user requests into predefined schemas (e.g., Coding, Research, Automation).
- **Goal Analyzer**: Breaks down high-level user objectives into structured specifications, identifying deliverables, constraints, and required agents.
- **Planner**: Converts objective specifications into an ordered list of executable tasks.
- **Task Allocator & Agent Registry**: Maps and assigns tasks to the appropriate specialized agents.
- **Worker Agents**: Specialized agents that perform the actual work (e.g., `CodingAgent`, `ResearchAgent`, `VerificationAgent`).
- **Plan Executor**: Orchestrates the execution of the entire task plan, managing task dependencies and collecting results.

## Requirements

- Python 3.10+
- An active Ollama instance running locally (defaulting to the `lfm2.5` model)
- `fastapi` and `requests`

## Setup

1. Clone this repository.
2. Create and activate a virtual environment (`python -m venv .venv`).
3. Install dependencies using `pip install -r requirements.txt`.
4. Ensure Ollama is running on your local machine (`http://localhost:11434`).

## Usage

You can test the system's various components using the provided test scripts:

- `planner_test.py`: Tests the plan generation capabilities.
- `plan_executor_test.py`: Tests the full pipeline from planning to execution.
- `tests.py` / `tests_new.py`: Tests for basic component integration.

You can also run the FastAPI server:
```bash
uvicorn main:app --reload
```
