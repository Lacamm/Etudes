#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exemple d'utilisation de msocket et simpleroute, ensemble.
Agrège les réseaux connus d'un bloc et les envoie périodiquement.
"""

import asyncio
from msocket import msocket
from socket import gethostname
from simpleroute import *
from time import time


def mastr(mmap):
    """transforme 'mmap' en une chaîne de caractères"""
    l = []
    for net in mmap:
        l.append("%s: %s" % (net, mmap[net][0]))
    return "\n".join(l)


def maparse(mmap, s,qui,msock):
    """parse la chaîne de caractère 's' et met à jour 'mmap'"""
    ss = s.strip().split("\n")
    print("Parsing '%s'" % (ss[0],))
    for l in ss[1:]:
        [net, hop] = l.strip().split(": ")
        hop = int(hop)
        if net not in mmap:
            mmap[net] = (hop + 1,qui,msock.ifname, time())
            setroute(net,qui)
        elif (mmap[net][1] == qui):
            mmap[net] = (hop + 1,qui, msock.ifname,time())
            delroute(net, mmap[net][1])
            mmap[net] = (hop + 1,qui, msock.ifname,time())
            setroute(net,qui)



async def send_mmap(msocks, mmap):
    """envoie la map aux sockets de 'msocks' toutes les 5 secondes"""
    host = gethostname()
    while True:
        print("Envoi de la map aux voisins :")
        s = mastr(mmap)
        for ms in msocks:
            print("\t - Envoi sur %s" % (ms.ifname,))
            ms.msend(("de %s vers %s\n" % (host, ms.ifname) + s).encode("utf-8"))
        await asyncio.sleep(5)


async def recv_mmap(msock, mmap):
    """réception des données et mise à jour de la map"""
    ch = "*****  Map actuelle  *****"
    while True:
        data, qui = await msock.mrecv()
        print("Reçu des données de %s via %s" % (qui[0], msock.ifname))
        maparse(mmap, data.decode("utf-8"),qui[0],msock)
        print(ch, mastr(mmap), "*" * len(ch), sep="\n")


async def rip_server(mgrp, mport, bloc):
    """serveur mmap"""

    # récupère le nom du routeur et les réseaux auxquels il est connecté
    host = gethostname()
    conet = [(net, eif) for (net, gw, eif) in getroutes() if gw is None]

    # crée une msocket pour chaque réseau connecté et initialise mmap avec les réseaux de [bloc]
    mmap = {}
    msocks = []

    for (net, eif) in conet:
        mip = getaddr(eif)
        mmap[net] = (0,mip,eif,time())
        print((net, eif, mip))

        ms = msocket(mgrp, mport, mip, eif)
        await ms.create_socket()

        ms.ifname = eif
        msocks.append(ms)

    print("Bonjour, j'ai %d interfaces et ma map courante est :" % (len(msocks),))
    print(mastr(mmap))

    # envoi périodique de la map sur toutes les interfaces :
    send_task = asyncio.create_task(send_mmap(msocks, mmap))

    # réception des données :
    recv_tasks = []
    for msock in msocks:
        recv_tasks.append(asyncio.create_task(recv_mmap(msock, mmap)))

    # attente que toutes les tâches soient terminées
    aws = [send_task] + recv_tasks
    await asyncio.gather(*aws)


if __name__ == "__main__":
    mgrp = "239.0.0.54"
    mport = 5454
    bloc = "192.168.0.0/16"

    loop = asyncio.get_event_loop()
    loop.create_task(rip_server(mgrp, mport, bloc))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("\nAu revoir !")
