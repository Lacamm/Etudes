#!/usr/bin/python3
import socket
import threading
from threading import Thread


class Serveur(object):

    def __init__(self,port):
        self.port = port
        self.bd = dict()
        self.lock = threading.Lock()
    
    def recevoir(self):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
        sock.bind(("0.0.0.0", self.port))
        sock.listen(10)
        while True:
            cli, addr = sock.accept()
            Session(cli, self).envoyer()
    
    def lireMessages(self,expe, dest):
        if expe in self.bd:
            for message in bd.values():
                if dest == message[0]:
                    return message
    def consulterBoite(self, expe):
        if expe in self.bd:
            for message in bd.values():
                return message
    def effacerMessage(self, expe, dest):
        if expe in self.bd:
            for message in bd.values():
                if dest == message[0]:
                    del message

    def envoyerMessage(self,expe,dest,message):
        if dest in self.bd.keys():
            self.bd[dest] = l.append((expe,message))
        else:
            l = list()
            self.bd[dest] = l.append((expe,message))

class Session(object):

    def __init__(self, cli,serveur):
        self.cli = cli
        self.serveur = serveur
        self.continuer = True
        self.f = self.cli.makefile(mode="rw")
    
    def envoyer(self):
        while self.continuer:
            line = self.f.readline().strip()
            if not line:
                self.continuer = False
            cmd, *args = line.split()
            method = "command_%s" % cmd.lower()
            getattr(self, method)(args)

        self.f.close()
        self.cli.shutdown(socket.SHUT_RDWR)
        self.cli.close()
    
    def command_lireMessage(self,expe,dest):
            self.message(self.f,"Lecture des messages entre ",expe," et ",dest)
            self.serveur.lireMessages(expe, dest)

    def command_consulterBoite(self,expe):
            self.message(self.f,"Lecture des messages de ",expe)
            self.serveur.consulterBoite(expe)
        
    def command_effacerMessage(self,expe,dest):
            self.message(self.f,"Effacement des messages entre ",expe," et ",dest)
            self.serveur.effacerMessage(expe,dest)

    def command_envoyerMessage(self,expe,dest,message):
        self.serveur.envoyerMessage(expe,dest, message)
        self.message(self.f,"Message envoyé à ",dest)

    def message(self,f,msg):
            f.write(msg)
            f.flush()


Serveur(5555).recevoir()