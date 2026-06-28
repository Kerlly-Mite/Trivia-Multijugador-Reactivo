import asyncio
from app.state.store import state

async def events_task():

    global state

    while True:
        await asyncio.sleep(20)

        state.scores["Katherine"] = state.scores.get("Katherine", 0) + 10

        print("Evento especial: bonus aplicado")