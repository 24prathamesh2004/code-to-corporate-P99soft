import asyncio

async def task():
    await asyncio.sleep(2)
    print("Task done")

async def main():
    await task()
    print("Next line")

asyncio.run(main())