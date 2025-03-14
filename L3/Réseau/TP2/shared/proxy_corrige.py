#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
from sys import argv
from socket import gethostbyname


async def pipe(reader, writer):
	""" ce qu'on lit dans le reader, on l'écrit dans le writer """
	while not reader.at_eof():
		data = await reader.read(1024)
		writer.write(data)
		print(data.decode())


async def handle_request(reader, writer, rhost, rport):
	addr = writer.get_extra_info("peername")
	print(f"Connection from {addr}")

	rreader, rwriter = await asyncio.open_connection(rhost, rport)

	await asyncio.gather(pipe(reader,rwriter),pipe(rreader,writer))


async def proxy_server(port, rhost, rport):
	server = await asyncio.start_server(lambda r,w:handle_request(r,w,rhost,rport), '0.0.0.0', port)
	addr = server.sockets[0].getsockname()
	print(f'Serving on {addr}')
	await server.serve_forever() # handle requests for ever


if __name__ == '__main__':
	if len(argv)!=4:
		print("usage: {scriptname} port rhost rport".format(scriptname= argv[0]))
		exit(1)
	port = argv[1]
	rhost = gethostbyname(argv[2])
	rport = argv[3]
	asyncio.run(proxy_server(port,rhost,rport))
