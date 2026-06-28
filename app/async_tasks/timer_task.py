import asyncio

from app.state.store import state


async def timer_task():

    while True:

        await asyncio.sleep(1)

        if state.timer > 0:
            state.timer -= 1
        else:
            state.timer = 30

        print(f"⏳ Timer: {state.timer}")