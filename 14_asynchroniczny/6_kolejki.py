import asyncio
import random

async def producer(queue, n):
    for i in range(n):
        await asyncio.sleep(random.uniform(0.5, 3))
        item = f'item-{i}'
        await queue.put(item)
        print(f'wyprodukowano {item}')

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f'Otrzymano {item}')
        await asyncio.sleep(random.uniform(1, 5))
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    num_items = 10

    producer_task = asyncio.create_task(producer(queue, num_items))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await queue.join()

    consumer_task.cancel()

    try:
        await consumer_task
    except asyncio.CancelledError:
        print('konsument cancelled')

asyncio.run(main())

