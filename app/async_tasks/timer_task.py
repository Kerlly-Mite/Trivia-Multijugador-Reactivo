import asyncio
from app.state.store import state
from app.state.reducer import update

async def timer_task():

    global state

    while True:
        await asyncio.sleep(1)

        new_timer = state.timer - 1

        if new_timer <= 0:
            new_timer = 30

        state = update(state, {
            "type": "UPDATE_TIMER",
            "timer": new_timer
        })

        print("Timer actualizado:", state.timer)