#!/usr/bin/python3
import socket
import threading
from threading import Thread


class Serveur(object):

    def __init__(self,port):
        self.port = port
        self.cpt = 0
        self.lock = threading.Lock()
    
    def recevoir(self):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
        sock.bind(("0.0.0.0", self.port))
        sock.listen(10)
        while True:
            cli, addr = sock.accept()
            Session(cli, self).envoyer()
        
    def getCpt(self):
        return self.cpt
    
    def incr(self):
        self.cpt+=1
    
    def decr(self):
        self.cpt-=1
    
    def add(self, val):
        self.cpt+=val


class Session(Thread):

    def __init__(self, cli,serveur):
        Thread.__init__(self)
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
    

    def command_get(self, args):
        with self.serveur.lock:
            self.message(self.f,"val %d\n" % self.serveur.getCpt())

    def command_quit(self, args):
        with self.serveur.lock:
            self.message(self.f,"quit\n")
            self.continuer = False
    
    def command_incr(self, args):
        with self.serveur.lock:
            if len(args)>0:
                self.message(self.f,"Cette commande ne prend pas d'arguments !\n")
            else:
                self.serveur.incr()
                self.message(self.f,"Compteur incrémenté\n")

    def command_decr(self, args):
        with self.serveur.lock:
            if len(args)>0:
                self.message(self.f,"Cette commande ne prend pas d'arguments !\n")
            else:
                self.serveur.decr()
                self.message(self.f,"Compteur décrémenté\n")
    
    def command_add(self, args):
        with self.serveur.lock:
            if len(args)!=1:
                self.message(self.f,"Le nombre d'arguments n'est pas valide !\n")
            else:
                try:
                    self.serveur.add(int(args[0]))
                    self.message(self.f,args[0]+" ajouté au compteur\n")
                except ValueError:
                    self.message(self.f,"Ceci n'est pas un nombre!\n")

    def message(self,f,msg):
        with self.serveur.lock:
            f.write(msg)
            f.flush()


Serveur(4444).recevoir()