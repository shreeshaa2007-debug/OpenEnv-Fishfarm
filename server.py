import sys
import os

# ✅ Force Python to find project folders
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from env.environment import FishFarmEnv

app = FastAPI()

env = FishFarmEnv()


@app.get("/")
def home():
    return {"message": "Fish Farm API Running 🚀"}


@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}


@app.post("/step")
def step(actions: list):
    state, reward, done, _ = env.step(actions)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }