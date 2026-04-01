from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import FishFarmEnv

app = FastAPI()
env = FishFarmEnv()

class StepRequest(BaseModel):
    actions: list

@app.get("/")
def home():
    return {"message": "Fish Farm API Running 🚀"}

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(req: StepRequest):
    state, reward, done, _ = env.step(req.actions)
    return {"state": state, "reward": reward, "done": done}