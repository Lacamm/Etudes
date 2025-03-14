#!/usr/bin/python3
import socket 


def server(port):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    sock.bind(("0.0.0.0", port))
    sock.listen(10)
    while True:
        cli, addr = sock.accept()
        session(cli)

COUNTER = 0

def session(cli):
    global COUNTER
    f = cli.makefile(mode="rw")
    while True:
        cmd = f.readline().strip()
        if cmd == "get":
            f.write("val %d\n" % COUNTER)
            f.flush()
        elif cmd == "quit":
            f.write("quit\n")
            f.flush()
            break
        else:
            f.write("error\n")
            f.flush()
    f.close()
    cli.shutdown(socket.SHUT_RDWR)
    cli.close()

server(4444)

