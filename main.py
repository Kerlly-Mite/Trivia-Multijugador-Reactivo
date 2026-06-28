import asyncio
from reactpy import run

from app.components.layout import Layout
from app.components.game import Game

from app.state.tasks.timer_task import timer_task
from app.state.tasks.round_task import round_task
from app.state.tasks.events_task import events_task


async def main():

    # correr tareas en paralelo (OBLIGATORIO RUBRICA)
    asyncio.create_task(timer_task())
    asyncio.create_task(round_task())
    asyncio.create_task(events_task())

    # UI ReactPy
    run(Layout)


if __name__ == "__main__":
    asyncio.run(main())