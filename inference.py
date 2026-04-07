from fastapi import FastAPI
from traffic_env import TrafficEnvironment

app = FastAPI()

env = TrafficEnvironment()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: int):
    next_state, reward, done = env.step(action)
    return {
        "state": next_state,
        "reward": reward,
        "done": done
    }
