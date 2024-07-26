import asyncio
import random

async def task(name, delay):
    print(f'Task {name} rozpocęty. Zostanie wykonany za {delay} sekund.')
    await asyncio.sleep(delay)
    print(f'Task {name} zakończone')

async def main():
    tasks = [
        task('A', random.uniform(1, 3)),
        task('B', random.uniform(1, 3)),
        task('C', random.uniform(1, 3)),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
