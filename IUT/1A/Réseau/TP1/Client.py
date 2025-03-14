#! /usr/bin/python3

import socket
import sys

BUFSIZE = 1024

def client(dest, port, msg):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.sendto(msg.encode(),(dest, int(port)))
    data = sock.recv(BUFSIZE)
    print(data.decode(), end="")

client(sys.argv[1],sys.argv[2],sys.argv[3])