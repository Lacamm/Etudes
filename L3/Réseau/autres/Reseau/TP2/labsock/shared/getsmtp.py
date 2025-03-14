#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from socket import gethostbyname
import asyncio



async def reponse(reader,writer,message) :

    # string message is encoded to bytes (default encoding: utf-8)
    writer.write(message.encode())
    # get server's answer
    data = await reader.readline()
    print(data.decode())
    d = data.decode()

    return d[:3]


async def smtp_client(server):
    # connecting to server on port 25
    reader, writer = await asyncio.open_connection(server, 25)

    # message = "EHLO\r\n MAIL FROM:<fhujsdghfjzendjktgfvnzejhkdhng@iiia.net>\r\n RCPT TO:<guest@iiia.net>\r\nDATA\r\njrcipdfghiozeifzeijfiozhufiozhiufhzui\r\n.\r\nQUIT\r\n"

    if( await reponse(reader,writer,"EHLO moi\r\n") == "220") :
            if(await reponse(reader,writer,"MAIL FROM:<fhujsdghfjzendjktgfvnzejhkdhng@iiia.net>\r\n") == "250") :
                if(await reponse(reader,writer,"RCPT TO:<guest@iiia.net>\r\n") == "250") :
                    if(await reponse(reader,writer,"DATA\r\n") == "250") :
                        if(await reponse(reader,writer,"message\r\n.\r\n") == "250") :
                            if(await reponse(reader,writer,"QUIT\r\n") == "250") :
                                print("Message arrive a destination")


if __name__ == '__main__':
    if len(argv)!=2:
        print("usage: {scriptname} server".format(scriptname= argv[0]))
        exit(1)
    sname=argv[1]
    server=gethostbyname(sname)
    print("connecting to :", sname, server)
    asyncio.run(smtp_client(server))
