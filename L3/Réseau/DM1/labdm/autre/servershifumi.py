#!/usr/bin/env python3
# -*- coding: utf-8 -

import asyncio

users = [] # liste des clients

async def forward(writer, addr, msg): # à modifier pour respecter le formats des commandes 
    for user in users:
        if user != writer:
            user.write(f"{addr}: {msg}\n".encode())
            await user.drain()


async def handle_request(reader, writer): # on gere les requetes clients
    addr = writer.get_extra_info('peername')[0] #on recupere les clients
    users.append(writer)
    
    message = f"User {addr} is connected."
    print(message)


    # await forward(writer, addr, message) # demander mode de jeu
    # créer table, trouver adversaire
    # on doit pouvoir gerer plusieurs clients en meme temps
    
    while True:
        data = await reader.readline() # tout le monde peut savoir se qui se passe (await)
        if reader.at_eof() : #or writer.is_closing():  # le joueur quitte le server
            print(f"Socket closed by user {addr}")
            data = b"quit"
        message = data.decode().strip()
        
        if message == "quit": # un joueur s'en va
            message = f"User {addr} quit the chat."
            print(message)
            await forward(writer, "Server", message)
            users.remove(writer)
            writer.close()
            break
        
        # pour chaque mode de jeu, definir le déroulé
        
        print(message)
        #await forward(writer, addr, message) # demander mode de jeu

        # si pas de conditionnelle, faire un truc à chaque fois?    


async def server_shifumi(): #lance le server
    server = await asyncio.start_server(handle_request, '10.0.0.0', 999) #gere les requetes
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever() # handle requests for ever


if __name__ == '__main__':
    asyncio.run(server_shifumi())