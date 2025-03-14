#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from sys import argv
from socket import gethostbyname

async def sendrecv(message, code_retour, reader, writer):
	""" envoie un message et vérifie un code retour """
	if message is not None:
		writer.write(message.encode()+b"\r\n")
	data = await reader.readline()

	if data[:3]!=code_retour:
		print(f"Erreur ... {code_retour} attendu, mais {data[:3]} obtenu")
		exit(1)
	return data.decode()

async def recup_data(data):
	debut = data.index("(")
	fin = data.index(")")
	token = data[debut+1:fin].split(",")
	print(token)

	server = ".".join(token[:4])
	port = 256*int(token[4])+int(token[5])

	print("server :", server)
	print("port   :", port)

	dreader,dwriter = await asyncio.open_connection(server,port)

	data = await dreader.read()
	print(data.decode())

	dwriter.close()

async def client_ftp(server):
	reader, writer = await asyncio.open_connection(server, 21)
	await sendrecv(None, b"220", reader, writer)
	await sendrecv("USER guest", b"331", reader, writer)
	await sendrecv("PASS guest", b"230", reader, writer)
	await sendrecv("SYST", b"215", reader, writer)
	await sendrecv("TYPE I", b"200", reader, writer)

	await sendrecv("CWD /home/guest", b"250", reader, writer)
	await sendrecv("TYPE A", b"200", reader, writer)
	data = await sendrecv("PASV", b"227", reader, writer)
	print(data)

	task = asyncio.create_task(recup_data(data))
	await sendrecv("LIST", b"150", reader, writer)
	await sendrecv(None, b"226", reader, writer)
	await task



	data = await sendrecv("PASV", b"227", reader, writer)
	print(data)

	task = asyncio.create_task(recup_data(data))
	await sendrecv("RETR cake", b"150", reader, writer)
	await sendrecv(None, b"226", reader, writer)
	await task



	await sendrecv("QUIT", b"221", reader, writer)


if __name__ == '__main__':
	if len(argv)!=2:
		print("usage: {scriptname} server".format(scriptname= argv[0]))
		exit(1)
	server = gethostbyname(argv[1])
	asyncio.run(client_ftp(server))

# ./ftp.py server.iiia.net
