def grade(state):
    oxygen = state["oxygen"][0]
    energy = state["energy_used"]

    score = 0
    if 5 <= oxygen <= 8:
        score += 0.7

    score += max(0, 0.3 - energy * 0.01)
    return min(score, 1.0)
