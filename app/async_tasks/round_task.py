import asyncio


async def round_task():

    while True:

        await asyncio.sleep(30)

        print("Nueva ronda")