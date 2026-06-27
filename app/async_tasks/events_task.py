import asyncio


async def events_task():

    while True:

        await asyncio.sleep(20)

        print("Evento especial")