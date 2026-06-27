from dataclasses import replace


def update(state, action):

    tipo = action["type"]

    if tipo == "UPDATE_TIMER":

        return replace(
            state,
            timer=action["timer"]
        )

    return state