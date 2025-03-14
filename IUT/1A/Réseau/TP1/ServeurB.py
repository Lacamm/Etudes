#! /usr/bin/python3
import socket 
import datetime
import time
from random import randint

def server(port):
    listeM = ["Le ","petit ","Chien ","Sans ","Famille ", "baleine "] # AJOUTEZ PLEINS DE MOTS
    data = listeM[randint(0,4)]
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET , socket.SO_BROADCAST , 1)
    addr = ("255.255.255.255", port)
    while True:
        data += listeM[randint(0,4)]
        sock.sendto(data.encode(), addr)
        time.sleep(1.0)
server(6666)