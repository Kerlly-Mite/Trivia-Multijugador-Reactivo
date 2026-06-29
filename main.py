import asyncio

from fastapi import FastAPI
import uvicorn

from reactpy.backend.fastapi import configure

from app.components.layout import Layout
from app.async_tasks.timer_task import timer_task
from app.async_tasks.round_task import round_task
from app.async_tasks.events_task import events_task


app = FastAPI()

configure(app, Layout)


@app.on_event("startup")
async def iniciar_corrutinas_autonomas():
    """
    Las 3 corrutinas autónomas se agendan AQUÍ, dentro del evento
    'startup' de FastAPI/uvicorn. Esto garantiza que ya exista un
    event loop corriendo (el mismo que usa uvicorn para atender
    a todos los navegadores conectados) antes de crear las tareas.

    Antes, 'loop.create_task(...)' se llamaba con
    asyncio.get_event_loop() ANTES de que run(Layout) arrancara su
    propio loop, así que las tareas quedaban agendadas en un loop
    que nunca llegaba a ejecutarse.
    """

    asyncio.create_task(timer_task())
    asyncio.create_task(round_task())
    asyncio.create_task(events_task())


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)
