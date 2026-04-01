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


@app.post("/step")
def step(actions: list):
    state, reward, done, _ = env.step(actions)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }