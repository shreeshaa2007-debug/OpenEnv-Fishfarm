def policy(state):
    actions = []
    for o in state["oxygen"]:
        if o < 5:
            actions.append("increase")
        elif o > 7.5:
            actions.append("decrease")
        else:
            actions.append("none")
    return actions
