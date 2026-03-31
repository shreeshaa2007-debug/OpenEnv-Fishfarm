import requests
import time

BASE_URL = "http://127.0.0.1:8000"
EPISODES = 3
STEPS = 20


def choose_action(state):
    actions = []

    for oxygen in state["oxygen"]:
        if oxygen < 5:
            actions.append("increase")
        elif oxygen > 8:
            actions.append("decrease")
        else:
            actions.append("none")

    return actions
def run_episode():
    total_reward = 0

    # Reset environment
    res = requests.post(f"{BASE_URL}/reset")
    state = res.json()["state"]

    for _ in range(STEPS):
        actions = choose_action(state) # simple baseline
     # simple baseline

        res = requests.post(
            f"{BASE_URL}/step",
            json={"actions": actions}
        )
        data = res.json()

        total_reward += data["reward"]
        state = data["state"]
        if data["done"]:
            break

    return total_reward


def main():
    scores = []

    for i in range(EPISODES):
        score = run_episode()
        print(f"Episode {i+1}: {score}")
        scores.append(score)
        time.sleep(1)

    avg = sum(scores) / len(scores)
    print(f"\nAverage Score: {avg}")


if __name__ == "__main__":
    main()