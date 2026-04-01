import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import manually
from importlib import import_module

FishFarmEnv = import_module("env.environment").FishFarmEnv


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