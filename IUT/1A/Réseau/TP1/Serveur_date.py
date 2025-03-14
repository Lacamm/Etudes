#! /usr/bin/python3

import socket
import datetime
import sys
import os

BUFSIZE = 1024

def server(port):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", int(port)))
    while True:
        data, addr = sock.recvfrom(BUFSIZE)
        print(data.decode())
        msg = data.decode()

        if (msg=="dring"):
            sock.sendto(b"salut\n", addr)
        elif (msg=="date"):
            data = datetime.datetime.now()
            data = "%s\n" % data
            sock.sendto(data.encode(), addr)
        elif (msg=="user"):
            data = os.environ["USER"]+"\n"
            sock.sendto(data.encode(),addr)
        else:
            sock.sendto(b"hein \n", addr)


server(sys.argv[1])