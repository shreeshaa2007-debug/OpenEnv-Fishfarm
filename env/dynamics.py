import random

def temperature_effect(temp):
    if temp > 30:
        return -0.3
    elif temp < 20:
        return -0.2
    return 0

def natural_oxygen_decay():
    return random.uniform(-0.3, -0.1)
