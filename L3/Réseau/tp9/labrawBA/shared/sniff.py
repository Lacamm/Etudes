#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import *
from random import randint,seed
from time import time

seed(time())

class AB(Packet):
    name = "AB"
    fields_desc = [ ShortField("psrc",0),
                    ShortField("pdst",0),
                    XByteField("version",0),
                    XByteField("type",0),
                    ShortField("seqnum",0),
                    ShortField("length",0),
                    ShortField("chksum",0)]

def transmet(pa,x):
    send(pa,verbose=0)
    print("""
Paquet transmis :
    src : %s, dst : %s, type : %s""" % (pa.src,pa.dst,['DATA','ACK','NACK'][x.type]))
    if len(x)==12:
        print("    Pas de payload")
    else:
        print("    Début du payload envoyé : %s" % AB(pa.load).load.decode()[:min(20,len(x.load))])
    
def modifie(pa,x):
    print("""
Paquet transmis avec erreur :
    src : %s, dst : %s, type : %s""" % (pa.src,pa.dst,['DATA','ACK','NACK'][x.type]))
    if len(x)==12:
        print("    Pas de payload")
    else:
        print("    Début du payload envoyé : %s" % x.load.decode()[:min(20,len(x.load))])
        l=len(x.load)
        n=randint(l//2,l-1)
        for i in range(n//4,3*n//4):
            a = randint(0,l-1)
            x.load = x.load[:a]+b'X'+x.load[a+1:]
        print("    Début du payload reçu : %s" % x.load.decode()[:min(20,len(x.load))])
    pa.load=raw(x)
    send(pa,verbose=0)

def perd(pa,x):
    x=AB(pa.load)
    print("""
Paquet perdu :
    src : %s, dst : %s, type : %s""" % (pa.src,pa.dst,['DATA','ACK','NACK'][x.type]))
    if len(x)==12:
        print("    Pas de payload")
    else:
        print("    Début du payload envoyé : %s" % x.load.decode()[:min(20,len(x.load))]) 
    
def mitm0(pa,x):
    transmet(pa,x)
    
def mitm1(pa,x):
    transmet(pa,x)
                                                       
def mitm2(pa,x):
    if randint(0,2)>1 or x.type>0:
        transmet(pa,x)
    else:
        modifie(pa,x)
        
def mitm3(pa,x):
    if randint(0,2)>1 or x.type>0:
        transmet(pa,x)
    else:
        perd(pa,x)
            
def mitm4(pa,x):
    if randint(0,2)>1 or x.type!=1:
        transmet(pa,x)
    else:
        perd(pa,x)

def mitm5(pa,x):
    r=randint(0,2)
    if r==0:
        transmet(pa,x)
    if r==1:
        perd(pa,x)
    if r==2:
        modifie(pa,x)

def applied_func(fr):
    mitm=[mitm0,mitm1,mitm2,mitm3,mitm4,mitm5]
    pa = fr.getlayer(IP)
    if pa.src not in [get_if_addr('eth0'),get_if_addr('eth1')] and pa.dst not in [get_if_addr('eth0'),get_if_addr('eth1')]:
        pa.ttl = pa.ttl - 1
        del(pa.chksum)
        x=AB(pa.load)
        mitm[min(x.version,5)](pa,x)
    
if __name__ == '__main__':
    sniff(prn=applied_func,lfilter=lambda x:(x.haslayer(IP) and x[Ether].src not in [get_if_hwaddr('eth0'),get_if_hwaddr('eth1')]))

