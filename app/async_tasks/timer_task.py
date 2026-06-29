import asyncio

from app.state import store
from app.state.actions import UPDATE_TIMER, NEXT_ROUND


async def timer_task():
    """
    Corrutina autónoma #1: temporizador global de rondas.

    Cada segundo descuenta el timer del estado global mediante
    dispatch (nunca mutando 'state' directamente). Cuando el
    timer llega a 0, dispara NEXT_ROUND para forzar el cierre
    automático de la ronda por tiempo agotado.
    """

    while True:

        await asyncio.sleep(1)

        estado_actual = store.state

        if not estado_actual.game_started or estado_actual.game_finished:
            continue

        if estado_actual.timer > 0:

            store.dispatch({
                "type": UPDATE_TIMER,
                "timer": estado_actual.timer - 1
            })

        else:

            store.dispatch({"type": NEXT_ROUND})
