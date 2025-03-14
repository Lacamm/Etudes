#! /usr/bin/python3

import socket 
import datetime
import time
import os

BUFSIZE = 1024

def server(port):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET , socket.SO_BROADCAST , 1)
    addr = ("255.255.255.255", port)
    msg, addr = sock.recvfrom(BUFSIZE)
    while True:
        user = os.environ["USER"]+": "
        data = user+msg.decode()
        sock.sendto(data.encode(), addr)
        time.sleep(5.0)
server(6666)