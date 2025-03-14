#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from ABproto import *
from time import sleep

numseq = 0

async def rcvsnd(s):
    """Reçoit un paquet AB et applique le protocole."""
    global numseq
    dump, addr = await s.ABreceivefrom()
    p = ABpacket.fromstr(dump)
    print("\r\n" + 30 * "*" + ("\nPaquet reçu de: %s\n" % addr[0]))
    p.affiche()  # demander un affichage complet avec p.affiche(full=True)

    if checksum(dump) != 0:
        print("Paquet erroné\n")
        p_NACK = ABpacket("",6666,5555,ABtype=2, ABseq=(numseq)%2)
        s.ABsend(p_NACK.tostr(calcchk=True), addr)
    else:
        if p.ABseq!=numseq:
            p_ACK = ABpacket("",6666,5555,ABtype=1,ABseq=(numseq-1)%2)
            s.ABsend(p_ACK.tostr(calcchk=True), addr)
        # envoyer un ACK
        else:
            p_ACK = ABpacket("",6666,5555,ABtype=1, ABseq=(numseq)%2)
            s.ABsend(p_ACK.tostr(calcchk=True), addr)
            numseq = (numseq)%2+1


    sleep(0.5)


async def main():
    s = ABsocket()
    await s.create_ABsocket()
    s.bufsize()  #Décommenter si on souhaite afficher les tailles des buffers
    while True:
        await rcvsnd(s)
    s.close()


if __name__ == "__main__":
    asyncio.run(main())
