from dataclasses import replace
from types import MappingProxyType

from app.state.game_state import GameState
from app.state.actions import (
    ENTER_PLAYER,
    START_GAME,
    ANSWER_QUESTION,
    NEXT_ROUND,
    UPDATE_TIMER,
    END_GAME,
    RESET_GAME
)
from app.services.trivia_service import get_question


def update(state, action):

    tipo = action["type"]

    if tipo == ENTER_PLAYER:

        nombre = action["nombre"]

        if nombre in state.players:
            return state

        nuevos_jugadores = state.players + (nombre,)

        nuevos_puntajes = dict(state.scores)
        nuevos_puntajes[nombre] = 0

        return replace(
            state,
            players=nuevos_jugadores,
            scores=MappingProxyType(nuevos_puntajes)
        )

    elif tipo == START_GAME:

        if len(state.players) == 0:
            return state

        primera_pregunta = get_question(0)

        return replace(
            state,
            screen="game",
            game_started=True,
            round_number=1,
            timer=30,
            current_question=MappingProxyType(primera_pregunta)
        )

    elif tipo == ANSWER_QUESTION:

        jugador = action["jugador"]
        opcion = action["opcion"]

        es_correcta = (
            opcion == state.current_question.get("correct")
        )

        nuevos_puntajes = dict(state.scores)

        if es_correcta:
            nuevos_puntajes[jugador] = (
                nuevos_puntajes.get(jugador, 0) + 10
            )

        return replace(
            state,
            scores=MappingProxyType(nuevos_puntajes)
        )

    elif tipo == NEXT_ROUND:

        siguiente_indice = state.round_number

        siguiente_pregunta = get_question(siguiente_indice)

        if siguiente_pregunta is None:

            return replace(
                state,
                screen="results",
                game_finished=True
            )

        return replace(
            state,
            round_number=state.round_number + 1,
            timer=30,
            current_question=MappingProxyType(siguiente_pregunta)
        )

    elif tipo == UPDATE_TIMER:

        return replace(
            state,
            timer=action["timer"]
        )

    elif tipo == END_GAME:

        return replace(
            state,
            screen="results",
            game_finished=True
        )

    elif tipo == RESET_GAME:

        return GameState(
            screen="home",
            players=tuple(),
            current_question=MappingProxyType({}),
            scores=MappingProxyType({}),
            timer=30,
            round_number=1,
            game_started=False,
            game_finished=False
        )

    return state
