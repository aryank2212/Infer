from fastapi import FastAPI

# pyrefly: ignore [missing-import]
from engine.decision_engine import decision_engine

app = FastAPI()

engine = decision_engine()


@app.post("/decision")
async def decision(payload: dict):

    text = payload["text"]

    result = engine.process(text)

    return result.model_dump()
