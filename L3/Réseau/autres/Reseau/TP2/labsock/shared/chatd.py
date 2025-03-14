#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Pour lancer le client nc -C pc1 6666


import asyncio

users = [] # empty list of connected users

async def forward(writer, addr, msg):
    for user in users:
        if user != writer:
            # Envoi un message a tout les utilisateurs sauf celui qui a envoye le message
            user.write(f"{addr}: {msg}\n".encode())
            # On verifie que tout les messages ont bien ete envoye
            await user.drain()


async def handle_request(reader, writer):
    addr = writer.get_extra_info('peername')[0]
    users.append(writer)



    # Ajout d'une personne qui se connecte au chat a la liste
    message = f"User {addr} is connected."
    print(message)
    await forward(writer, addr, message)

    while True:
        data = await reader.readline() # thanks to await, other users can also read data in the sametime
        if reader.at_eof() : #or writer.is_closing(): on regarde si le message ferme la connexion
            print(f"Socket closed by user {addr}")
            data = b"quit" # <- simulated 'quit' command
        message = data.decode().strip()

        if message == "quit":
            message = f"User {addr} quit the chat."
            print(message)
            await forward(writer, "Server", message)
            users.remove(writer)
            writer.close()
            break

        print(message)
        await forward(writer, addr, message)


async def chat_server():
    # start a socket server
    server = await asyncio.start_server(handle_request, '0.0.0.0', 6666)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever() # handle requests for ever

if __name__ == '__main__':
    asyncio.run(chat_server())
