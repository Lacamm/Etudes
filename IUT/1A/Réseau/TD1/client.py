#! /usr/bin/python3

import socket

BUFSIZE = 1024
def client(port):
    sock = socket.socket(type = socket.SOCK_DGRAM)
    sock.sendto(b"Dring", ("localhost",port))
    data, adr = sock.recvfrom(BUFSIZE)
    print(data.decode(), end="")

client(5555)