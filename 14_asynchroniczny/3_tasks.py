import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    print(f'Rozpoczęto {asyncio.get_running_loop().time()}')

    task1 = asyncio.create_task(say_after(2, 'hello'))
    task2 = asyncio.create_task(say_after(1, 'world'))

    await task1
    await task2

    print(f'Done {asyncio.get_running_loop().time()}')

asyncio.run(main())