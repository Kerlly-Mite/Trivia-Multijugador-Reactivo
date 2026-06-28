from dataclasses import replace


def update(state, action):

    tipo = action["type"]

    if tipo == "UPDATE_TIMER":

        return replace(
            state,
            timer=action["timer"]
        )

    elif tipo == "NEXT_ROUND":

        return replace(
            state,
            round_number=state.round_number + 1,
            timer=30
        )

    return state