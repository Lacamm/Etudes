#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from socket import gethostbyname
import asyncio

async def smtp_client(msg):

    server=gethostbyname("smtp.iiia.net")
    reader, writer = await asyncio.open_connection(server, 25)

    data = await reader.readline()
    print(data.decode())
    writer.write("HELO Client\r\n".encode())

    data = await reader.readline()
    print(data.decode())
    writer.write("MAIL FROM: <test@test.fr>\r\n".encode())

    data = await reader.readline()
    print(data.decode())
    writer.write("RCPT TO: <guest@iiia.net>\r\n".encode())

    data = await reader.readline()
    print(data.decode())
    writer.write("DATA\r\n".encode())

    # contenu de msg à remplacer par un vrai mail

    msg += "\r\n"

    msg.replace('\n', '\r\n')
    writer.write(msg.encode())
    writer.write(".\r\n".encode())
    data = await reader.readline()

    data = await reader.readline()
    print(data.decode())
    writer.write("QUIT\r\n".encode())

    data = await reader.readline()
    print(data.decode())

asyncio.run(smtp_client("coucou"))
