import asyncio
from reactpy import run

from app.components.layout import Layout
from app.async_tasks.timer_task import timer_task
from app.async_tasks.round_task import round_task
from app.async_tasks.events_task import events_task


def start_async_tasks():
    loop = asyncio.get_event_loop()
    loop.create_task(timer_task())
    loop.create_task(round_task())
    loop.create_task(events_task())


if __name__ == "__main__":
    start_async_tasks()
    run(Layout)