import asyncio
async def may_fail(delay, fail=False):
    await asyncio.sleep(delay)
    if fail:
        raise ValueError(f"Zadanie zakonczone niepowodzeniem po {delay} sekundach")
    return f'Zakończono po {delay} sekundach'

async def main():
    try:
        result = await may_fail(2, fail=True)
        print(result)
    except ValueError as e:
        print(f'złapano wyjatek {e}')

asyncio.run(main())
