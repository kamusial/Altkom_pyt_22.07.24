import asyncio

async def say_hello():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

def hello_periodically(loop):
    print('Hello periodically')
    loop.call_later(2, hello_periodically, loop)

async def main(loop):
    print(f'start głównej korutyny')
    task = loop.create_task(say_hello())
    loop.call_later(2, hello_periodically, loop)
    await task
    print(f'główne zadanie skonczone')

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main(loop))
finally:
    loop.close()

