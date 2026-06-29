import asyncio

from app.state import store
from app.state.actions import END_GAME
from app.services.trivia_service import total_preguntas


async def round_task():
    """
    Corrutina autónoma #2: vigilante de duración máxima de partida.

    Cada 5 segundos revisa si la partida sigue activa y si ya se
    superó el número de preguntas disponibles en el banco de
    trivia. Si es así, fuerza el cierre automático del juego
    (END_GAME) aunque ningún jugador haya hecho clic en nada,
    evitando que una partida quede "viva" indefinidamente.
    """

    while True:

        await asyncio.sleep(5)

        estado_actual = store.state

        if not estado_actual.game_started or estado_actual.game_finished:
            continue

        if estado_actual.round_number > total_preguntas():

            store.dispatch({"type": END_GAME})
