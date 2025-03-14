#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from sys import argv
from ABproto import *

numseq = 0

fstmsg = "The primroses were over."

sndmsg = "Toward the edge of the wood, where the ground became open and sloped down to an old fence and a brambly ditch beyond, only a few fading patches of pale yellow still showed among the dog's mercury and oak tree roots."

thirdmsg = "On the other side of the fence, the upper part of the field was full of rabbit holes."


async def sndrcv(s, data, psrc, pdst, dst):
    """Envoie un paquet AB et exécute le protocole."""
    global numseq
    p = ABpacket(data, psrc, pdst, ABseq=(numseq)%2)
    if s.ABsend(p.tostr(calcchk=True), dst):
        print("\n" + 30 * "*" + "\r\nPaquet envoyé :\n")
        p.affiche()  # demander un affichage complet avec p.affiche(full=True)

        #reception ACK ou NACK
        try:
            dump, addr = await asyncio.wait_for(s.ABreceivefrom(),timeout=2)
            p_NACKorACK = ABpacket.fromstr(dump)

            if p_NACKorACK.ABtype==2: #NACK
                await sndrcv(s, data, psrc, pdst, dst)
            elif p_NACKorACK.ABtype==1 and p.ABseq==(numseq)%2:
                numseq = numseq+1

        except asyncio.TimeoutError:
            print("Timeout")
            await sndrcv(s, data, psrc, pdst, dst)

    else:
        print("Échec lors de l'envoi.")
        return 0

async def main(server):
    s = ABsocket()
    await s.create_ABsocket()
    dst = (server, 0)
    await sndrcv(s, fstmsg, 6666, 5555, dst)
    await sndrcv(s, 6*sndmsg, 6666, 5555, dst)
    await sndrcv(s, 10*thirdmsg, 6666, 5555, dst)
    s.close()


if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: {scriptname} server".format(scriptname=argv[0]))
        exit(1)
    asyncio.run(main(argv[1]))
