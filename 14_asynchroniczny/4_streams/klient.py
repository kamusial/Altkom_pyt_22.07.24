import asyncio

async def tcp_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print(f'Wysyłam {message}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'otrzymano {data.decode()}')

    print('Zamykam połączenie')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_client('Hello World!'))