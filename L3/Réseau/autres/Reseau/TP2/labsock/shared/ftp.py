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

    print(d[:3])

    return d[:3]

    # recuperer le nouveau port pour recevoir les donnees
    # Commande passive affiche dans wireshark : (10,0,1,1,f1,f2) avec nbPorts = f1 * 256 + f2

async def ftp_client(server) :

    reader, writer = await asyncio.open_connection(server,21)
    if (await reponse(reader,writer,"")) == "220" :
        if(await reponse(reader,writer,"USER guest\r\n") == "331" ) :
            if(await reponse(reader,writer,"PASS guest\r\n") == "230") :
                if(await reponse(reader,writer,"SYST\r\n") == "215") :
                    if(await reponse(reader,writer,"TYPE I\r\n") == "200") :
                        if(await reponse(reader,writer,"PASV\r\n") == "227") :
                            if(await reponse(reader,writer,"CWD /home/guest\r\n") == "250") :
                                reader2 , writer2 = await asyncio.open_connection(server,)
                                if(await reponse(reader,writer,"\r\n") == "") :
                                    await reponse(reader,writer,"QUIT\r\n")



if __name__ == '__main__':
    sname=argv[1]
    server=gethostbyname(sname)
    print("connecting to :", sname, server)
    asyncio.run(ftp_client(server))
