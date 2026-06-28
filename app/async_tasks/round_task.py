import asyncio
from app.state.store import state
from app.state.reducer import update

async def round_task():

    global state

    while True:
        await asyncio.sleep(30)

        state = update(state, {
            "type": "NEXT_ROUND"
        })

        print("Nueva ronda:", state.round_number)