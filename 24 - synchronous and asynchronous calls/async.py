import asyncio

async def taskRoutine():
    print("Stand in the line for ticket")
    await asyncio.sleep(2)
    print("talking with father ji")

async def main():
    TR = taskRoutine()
    task = asyncio.create_task(TR)
    await asyncio.sleep(5)
    print("both tasks are completed")
    await task

asyncio.run(main())

