import asyncio

async def set_future_result(future):
    await asyncio.sleep(2)
    future.set_result('Wynik ustawiony')
    print('Ustawiono')

async def main():
    future = asyncio.Future()
    asyncio.create_task(set_future_result(future))
    print('Czekam na wyniki')
    result = await future
    print(f'mam wynik {result}')

asyncio.run(main())

