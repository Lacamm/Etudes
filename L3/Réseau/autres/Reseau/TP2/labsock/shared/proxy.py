#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Pour lancer le proxy ./proxy.py 8888 10.0.0.1 6666
# Pour se connecter au proxy : nc -C 10.0.0.2 8888

from sys import argv
import asyncio

clients = [] # empty list of connected users

async def RcvChat(reader_proxy, writer) :
    while True:
        data = await reader_proxy.readline()
        writer.write(data)

async def RcvClient(reader, writer_proxy) :
    while True :
        data = await reader.readline()
        writer_proxy.write(data)


async def handle_request(reader, writer):
    # Connexion au chat
    reader_proxy , writer_proxy = await asyncio.open_connection(argv[2], argv[3])


    addr = writer.get_extra_info('peername')[0]
    print(f"User {addr} is connected")

    task1 = asyncio.create_task(RcvChat(reader_proxy,writer))
    task2 = asyncio.create_task(RcvClient(reader, writer_proxy))



async def proxy_server(port):
    print("Lancement du serveur proxy")
    server = await asyncio.start_server(handle_request, '0.0.0.0', port)
    addr = server.sockets[0].getsockname()
    print(f'Proxing on {addr}')
    async with server:
        await server.serve_forever() # handle requests for ever

if __name__ == '__main__':
    if len(argv) != 4 :
        print("usage : {scriptname} port rhost rport".format(scriptname=argv[0]))
        exit(1)
    asyncio.run(proxy_server(argv[1]))

# argv[1] : port ; port de la machine qui souhaite se connecter
# argv[2] : rhost : ip du chat
# argv[3] : rport : port du chat
