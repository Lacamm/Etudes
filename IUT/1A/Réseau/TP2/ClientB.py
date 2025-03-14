#! /usr/bin/python3
import socket
import sys

def client(port):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    addr = ("255.255.255.255", port)
    sock.bind(addr)
    while True:
        msg = input()
        sock.sendto(msg.encode(),(addr, int(port)))
        data, saddr = sock.recvfrom(128)
        print(saddr, data.decode())
client(6666)