import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print('Connected by', addr)

    while True:
        data = await reader.read(100)   # czytanie danych max 100 bajtów
        if not data:
            break
        message = data.decode()
        print(f'Otrzymano {message} z {addr}')
        response = f'Otrzymano {message}'
        writer.write(response.encode())
        await writer.drain()    #upewnij się, że bufor opróżniony

    print('POłączenie zamknięte')
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Server on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())