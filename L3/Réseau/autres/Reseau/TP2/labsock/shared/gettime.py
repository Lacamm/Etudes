#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from socket import gethostbyname
import asyncio
from datetime import datetime

async def service_daytime(reader,writer) :
    addr = writer.get_extra_info('peername')

    print(f"Connecting to {addr}")

    data = datetime.now().strftime('%c').encode()
    writer.write(data)
    print("Close the connexion")
    writer.close()

async def daytime_client(server) :
    reader, writer = await asyncio.open_connection(server, 8888)

    print(reader.decode())

async def init_server() :
    server = await asyncio.start_server(service_daytime, '0.0.0.0',8888) #numéro du port que l'on souhaite ouvrir
    print("serveur en attente")
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")
    async with server:
        await server.serve_forever()



if __name__ == '__main__':
    asyncio.run(init_server())
