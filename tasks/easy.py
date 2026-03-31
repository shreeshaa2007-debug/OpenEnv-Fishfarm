def grade(state):
    oxygen = state["oxygen"][0]
    return 1.0 if 5 <= oxygen <= 8 else 0.0
