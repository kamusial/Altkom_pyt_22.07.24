import asyncio

async def example():
    print('start coroutine')
    await asyncio.sleep(1)
    print('end coroutine')

async def main():
    print('przed korutyną')
    await example()
    print('po korutynie')

asyncio.run(main())