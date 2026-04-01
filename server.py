import sys
import os
from importlib import import_module

from fastapi import FastAPI   

# Fix path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Load environment
FishFarmEnv = import_module("env.environment").FishFarmEnv

app = FastAPI()

env = FishFarmEnv()

@app.get("/")
def home():
    return {"message": "Fish Farm API Running 🚀"}


@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}


from pydantic import BaseModel

class ActionRequest(BaseModel):
    actions: list


@app.post("/step")
def step(req: ActionRequest):
    try:
        print("Received:", req.actions)

        state, reward, done, _ = env.step(req.actions)

        return {
            "state": state,
            "reward": reward,
            "done": done
        }

    except Exception as e:
        return {"error": str(e)}