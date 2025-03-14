#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from socket import *
from struct import *

version = 4


def checksum(x):
    """Retourne le checksum de la chaîne de bytes x."""
    if len(x) % 2 == 1:
        x += b"\x00"
    y = sum([int.from_bytes(x[i : i + 2], "big") for i in range(0, len(x), 2)])
    while y >= (1 << 16):
        y = (y // (1 << 16)) + (y % (1 << 16))
    return (1 << 16) - 1 - y


class ABpacket:
    """Définition abstraite de paquet pour le protocole AB."""

    def __init__(self, data="", psrc=0, pdst=0, ABver=version, ABtype=0, ABseq=0):
        self.psrc = psrc
        self.pdst = pdst
        self.ABver = ABver
        self.ABtype = ABtype
        self.ABseq = ABseq
        self.ABlen = 12 + len(data)
        self.ABchk = 0
        self.data = data

    def affiche(self, full=False):
        if full:
            d = self.data
        else:
            d = self.data[: min(40, len(self.data))] + "..."
        print(
            """Port source : %d
Port destination : %d
Version : %d
Type : %d
Numéro de séquence : %d
Longueur : %d
Checksum : %s
Contenu : %s"""
            % (
                self.psrc,
                self.pdst,
                self.ABver,
                self.ABtype,
                self.ABseq,
                self.ABlen,
                self.ABchk,
                d,
            )
        )

    def tostr(self, calcchk=False):
        """Construit une chaîne de bytes à partir d'un paquet AB."""
        if calcchk:
            x = pack(
                "!HHBBHHH" + str(len(self.data)) + "s",
                self.psrc,
                self.pdst,
                self.ABver,
                self.ABtype,
                self.ABseq,
                self.ABlen,
                self.ABchk,
                self.data.encode(),
            )
            self.ABchk = checksum(x)
        return pack(
            "!HHBBHHH" + str(len(self.data)) + "s",
            self.psrc,
            self.pdst,
            self.ABver,
            self.ABtype,
            self.ABseq,
            self.ABlen,
            self.ABchk,
            self.data.encode(),
        )

    @classmethod
    def fromstr(cls, dump):
        """Remplit les champs du paquet AB en lisant la chaîne de bytes."""
        psrc, pdst, ABver, ABtype, ABseq, ABlen, ABchk = unpack("!HHBBHHH", dump[:12])
        data = unpack("!" + str(ABlen - 12) + "s", dump[12:])[0].decode()
        p = cls(data, psrc, pdst, ABver, ABtype, ABseq)
        p.ABchk = ABchk
        return p


class ABsocket:
    """Sockets RAW utilisant le protocole 240."""

    def __init__(self):
        self.sock = socket(AF_INET, SOCK_RAW, 240)

    async def create_ABsocket(self):
        """Configure l'ABsocket (mode non bloquant et taille du buffer de réception)."""
        self.sock.setblocking(0)
        self.sock.setsockopt(SOL_SOCKET, SO_RCVBUF, 1152)

    def bufsize(self):
        print(
            "Taille du buffer de réception : %d"
            % self.sock.getsockopt(SOL_SOCKET, SO_RCVBUF)
        )
        print(
            "Taille du buffer d'émission : %d"
            % self.sock.getsockopt(SOL_SOCKET, SO_SNDBUF)
        )

    async def ABreceivefrom(self):
        """Reçoit un paquet IP et retourne (payload IP,addr src)."""
        loop = asyncio.get_event_loop()
        dump = await loop.sock_recv(self.sock, 4096)
        return (
            dump[20:],
            (".".join([str(i) for i in unpack("!IIIBBBB", dump[:16])][3:]), 0),
        )

    def ABsend(self, packet, addr):
        """Envoie le paquet AB à l'adresse addr."""
        if len(packet) > 2000:
            print("""
%s EXCEPTION PAQUET LONG %s
Ce paquet contient des données trop grandes, je refuse de l'envoyer !\n Découpez-le ou attendez qu'une solution pour les grandes quantités de données soit implémentée.""" % (20*'*',20*'*') )
            return 0
        self.sock.sendto(packet, addr)
        return 1

    def close(self):
        self.sock.close()
