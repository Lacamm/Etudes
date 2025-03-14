#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from socket import gethostbyname
import asyncio

from datetime import datetime

############# FONCTIONS #############
async def handle_request(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"incoming request from {addr}")

    message = datetime.now().strftime('%c')
    writer.write(message.encode())

    writer.close()

async def daytime_server():
    server = await asyncio.start_server(handle_request,"0.0.0.0",13)

    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    await server.serve_forever()

############# MAIN #############
if __name__ == '__main__':
    asyncio.run(daytime_server())
