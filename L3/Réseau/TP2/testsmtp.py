#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from socket import gethostbyname
import asyncio
	
	
async def smtp_client(server):
	reader, writer = await asyncio.open_connection(server, 25)

	data = await reader.readline()
	print(data.decode())
	
	writer.write("HELO Client\r\n".encode())
	data = await reader.readline()
	print(data.decode())

	writer.write("MAIL FROM: <client@iiia.net>\r\n".encode())
	data = await reader.readline()
	print(data.decode())

	writer.write("RCPT TO: <guest@iiia.net>\r\n".encode())
	data = await reader.readline()
	print(data.decode())
	
	writer.write("DATA\r\n".encode())
	data = await reader.readline()
	print(data.decode())

	msg = "test\r\n" # <-- à remplacer par un vrai mail
	
	msg = """From: The Cake Factory <cakefactory@iiia.net>
To: Gérard Uest <guest@iiia.net>
Date: Tue Sep 28 15:13:37 2021
Subject: GET A FREE CAKE!

Dear Gérard,

Do you want a cake?

Best,
The Cake Factory
""".replace('\n','\r\n')

	writer.write(msg.encode())
	writer.write(".\r\n".encode())
	data = await reader.readline()
	print(data.decode())

	writer.write("QUIT\r\n".encode())
	data = await reader.readline()
	print(data.decode())

	


if __name__ == '__main__':
	if len(argv)!=2:
		print("usage: {scriptname} server".format(scriptname= argv[0]))
		exit(1)
	sname=argv[1]
	server=gethostbyname(sname)
	asyncio.run(smtp_client(server))