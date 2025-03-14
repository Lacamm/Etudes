#! /usr/bin/python3

import socket

BUFSIZE = 1024
def serveur(port):
    sock = socket.socket(type = socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", port))
    while(True):
        data, adr = sock.recvfrom(BUFSIZE)
        print(data.decode(), end="")
        sock.sendto(b"Salut \n", adr)

serveur(5555)