import asyncio


async def timer_task():

    while True:

        await asyncio.sleep(1)

        print("Timer")