import asyncio

from app.state.store import state


async def events_task():

    while True:

        await asyncio.sleep(20)

        puntos = state.scores.get("Katherine", 0)

        state.scores["Katherine"] = puntos + 10

        print(
            f"⭐ Bonus para Katherine: {state.scores['Katherine']}"
        )