from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from env.environment import FishFarmEnv

app = FastAPI()
env = FishFarmEnv(ponds=2)

class ActionRequest(BaseModel):
    actions: List[str]

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return {"state": env.reset()}

@app.post("/step")
def step(req: ActionRequest):
    state, reward, done, _ = env.step(req.actions)
    return {"state": state, "reward": reward, "done": done}

@app.get("/state")
def state():
    return {"state": env.state()}
