#!/usr/bin/python3

import socket

def client(host, port):
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw")

    f.write("envoyerMessage(Pierre, Jean, salut)\n")
    f.flush()
    print(f.readline(), end="")

    f.write("consulterBoite(Jean)\n")
    f.flush()
    print(f.readline(), end="")
    
    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client("localhost", 5555)