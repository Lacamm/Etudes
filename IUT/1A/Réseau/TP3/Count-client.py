#!/usr/bin/python3

import socket

def client(host, port):
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw")

    f.write("get\n")
    f.flush()
    print(f.readline(), end="")

    f.write("quit\n")
    f.flush()
    print(f.readline(), end="")
    
    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client("localhost", 4444)