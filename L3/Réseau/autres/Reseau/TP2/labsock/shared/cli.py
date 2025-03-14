#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from socket import gethostbyname
import asyncio


async def tcp_client(server) :
    reader, writer = await asyncio.open_connection(server, 8888)

    # get server's answer
    data = await reader.read()
    print(data.decode())

if __name__ == '__main__':
    asyncio.run(tcp_client("10.0.0.1"))
