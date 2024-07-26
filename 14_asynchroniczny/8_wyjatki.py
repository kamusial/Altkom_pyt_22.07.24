import asyncio
async def may_fail(delay, fail=False):
    await asyncio.sleep(delay)
    if fail:
        raise ValueError(f"Zadanie zakonczone niepowodzeniem po {delay} sekundach")
    return f'Zakończono po {delay} sekundach'

async def main():
    task1 = asyncio.create_task(may_fail(1))
    task2 = asyncio.create_task(may_fail(2, fail=True))
    task3 = asyncio.create_task(may_fail(3))
    tasks = [task1, task2, task3]

    for task in tasks:
        try:
            result = await task
            print(result)
        except ValueError as e:
            print(f'złapano wyjatek {e}')

asyncio.run(main())
