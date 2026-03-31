def grade(state):
    oxygens = state["oxygen"]
    energy = state["energy_used"]

    good = sum(1 for o in oxygens if 5 <= o <= 8)
    score = (good / len(oxygens)) * 0.7

    score += max(0, 0.3 - energy * 0.01)
    return min(score, 1.0)
