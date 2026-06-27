from app.state.reducer import update


def start_game(state):

    action = {
        "type": "START_GAME"
    }

    return update(state, action)