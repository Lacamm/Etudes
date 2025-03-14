#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from socket import gethostbyname
import asyncio
    
    
async def http_client(server):
    # connecting to server on port 80
    reader, writer = await asyncio.open_connection(server, 80)

    message = "GET / HTTP/1.0\r\nHost: {server}\r\nAccept: */*\r\n\r\n".format(server=server)
    
    # string message is encoded to bytes (default encoding: utf-8)
    writer.write(message.encode())
    
    # get server's answer
    data = await reader.read()
    print(data.decode())
  

if __name__ == '__main__':
    if len(argv)!=2:
        print("usage: {scriptname} server".format(scriptname= argv[0]))
        exit(1)
    sname=argv[1]
    server=gethostbyname(sname)
    print("connecting to :", sname, server)
    asyncio.run(http_client(server))
    