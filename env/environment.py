import random
from env.dynamics import temperature_effect, natural_oxygen_decay

class FishFarmEnv:
    def __init__(self, ponds=2, seed=42):
        self.ponds = ponds
        random.seed(seed)
        self.reset()

    def reset(self):
        self.state_data = {
            "oxygen": [random.uniform(4, 7) for _ in range(self.ponds)],
            "temperature": random.uniform(25, 30),
            "energy_used": 0,
            "time": 0
        }
        return self.state()

    def state(self):
        return self.state_data

    def step(self, actions):
        reward = 0
        self.state_data["temperature"] += random.uniform(-0.5, 0.5)

        for i in range(self.ponds):
            self.state_data["oxygen"][i] += natural_oxygen_decay()

            if actions[i] == "increase":
                self.state_data["oxygen"][i] += 0.6
                self.state_data["energy_used"] += 1
            elif actions[i] == "decrease":
                self.state_data["oxygen"][i] -= 0.3

            self.state_data["oxygen"][i] += temperature_effect(self.state_data["temperature"])
            self.state_data["oxygen"][i] = max(0, min(10, self.state_data["oxygen"][i]))

            if 5 <= self.state_data["oxygen"][i] <= 8:
                reward += 1
            elif self.state_data["oxygen"][i] < 3:
                reward -= 2
            else:
                reward -= 0.2

        reward -= self.state_data["energy_used"] * 0.03
        self.state_data["time"] += 1
        done = self.state_data["time"] >= 50

        return self.state(), reward, done, {}
