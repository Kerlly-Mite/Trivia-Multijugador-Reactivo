from app.state.reducer import update
from app.state.actions import (
    ENTER_PLAYER,
    START_GAME,
    ANSWER_QUESTION,
    NEXT_ROUND,
    END_GAME
)


def enter_player(state, nombre):

    action = {
        "type": ENTER_PLAYER,
        "nombre": nombre
    }

    return update(state, action)


def start_game(state):

    action = {
        "type": START_GAME
    }

    return update(state, action)


def answer_question(state, jugador, opcion):

    action = {
        "type": ANSWER_QUESTION,
        "jugador": jugador,
        "opcion": opcion
    }

    return update(state, action)


def next_round(state):

    action = {
        "type": NEXT_ROUND
    }

    return update(state, action)


def end_game(state):

    action = {
        "type": END_GAME
    }

    return update(state, action)


def ranking_ordenado(state):

    return sorted(
        state.scores.items(),
        key=lambda item: item[1],
        reverse=True
    )


def obtener_ganador(state):

    ranking = ranking_ordenado(state)

    if len(ranking) == 0:
        return None

    return ranking[0]
