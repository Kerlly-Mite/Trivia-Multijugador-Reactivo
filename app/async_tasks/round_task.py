import asyncio

from app.state.store import state


async def round_task():

    while True:

        await asyncio.sleep(30)

        state.round_number += 1

        print(f"🎮 Nueva ronda: {state.round_number}")