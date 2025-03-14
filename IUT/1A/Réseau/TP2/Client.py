#! /usr/bin/python3

import socket
import sys

BUFSIZE = 1024

def client(dest, port, msg):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    input(">")
    sock.sendto(msg.encode(),(dest, int(port)))
    data = sock.recv(BUFSIZE)
    input(">") # faire netstat -ua dans un terminal, ca affiche la socket
    print(data.decode(), end="")

client(sys.argv[1],sys.argv[2],sys.argv[3])
