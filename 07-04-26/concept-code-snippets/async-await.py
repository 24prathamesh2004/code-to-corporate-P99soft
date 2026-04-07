import asyncio

async def task():
    await asyncio.sleep(1)
    print("Task done")

async def main():
    await task()

asyncio.run(main())