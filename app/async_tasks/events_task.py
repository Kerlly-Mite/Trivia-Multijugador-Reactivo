import asyncio
import random

from app.state import store
from app.state.actions import ANSWER_QUESTION


async def events_task():
    """
    Corrutina autónoma #3: generación periódica de eventos de bonus.

    Cada 20 segundos, si hay una partida activa con jugadores
    conectados, otorga un bonus de puntos a un jugador elegido
    al azar entre los conectados (no a un nombre fijo), simulando
    un evento aleatorio del tablero. El cambio se aplica siempre
    mediante dispatch, nunca mutando 'state.scores' directamente.
    """

    while True:

        await asyncio.sleep(20)

        estado_actual = store.state

        if not estado_actual.game_started or estado_actual.game_finished:
            continue

        if len(estado_actual.players) == 0:
            continue

        jugador_bonus = random.choice(estado_actual.players)

        store.dispatch({
            "type": ANSWER_QUESTION,
            "jugador": jugador_bonus,
            "opcion": estado_actual.current_question.get("correct")
        })
