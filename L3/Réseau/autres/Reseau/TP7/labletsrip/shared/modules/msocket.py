# -*- coding: utf-8 -*-

"""
Ce module simplifie le déploiement de sockets multicast en IPv4 avec asyncio.
"""

import asyncio
import socket
import struct
import sys


class MulticastDatagramProtocol(asyncio.DatagramProtocol):
    def __init__(self, loop, ms, mgrp, mport, mip, eif):
        """crée une socket multicast pour le groupe [mgrp] port [mport]
        sur l'interface de nom [eif] et d'adresse [mip]."""
        self.loop = loop
        self.ms = ms
        self.mgrp = mgrp
        self.mport = mport
        self.mip = mip
        self.eif = eif

    def connection_made(self, transport):
        self.transport = transport

        sock = self.transport.get_extra_info("socket")
        sock.settimeout(3)
        addrinfo = socket.getaddrinfo(self.mgrp, None)[0]

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        mreq = socket.inet_aton(self.mgrp) + socket.inet_aton(self.mip)
        sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 0)
        ttl = struct.pack("@i", 1)
        sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, ttl)
        sock.setsockopt(
            socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(self.mip)
        )
        SO_BINDTODEVICE = 25  # seulement sous linux
        sock.setsockopt(
            socket.SOL_SOCKET, SO_BINDTODEVICE, str(self.eif + "\0").encode("utf-8")
        )

        sock.bind(("", self.mport))

    def datagram_received(self, data, addr):
        self.ms.add_datagram(data, addr)

    def error_received(self, exc):
        print("Error received:", exc)

    def connection_lost(self, exc):
        self.ms.close()


class msocket:
    def __init__(self, broadcast_addr, broadcast_port, local_ip, local_eif):
        addrinfo = socket.getaddrinfo(broadcast_addr, None)[0]
        self.sock = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
        self.queue = asyncio.Queue()

        self.mgrp = broadcast_addr
        self.mport = broadcast_port
        self.mip = local_ip
        self.eif = local_eif

    async def create_socket(self):
        loop = asyncio.get_event_loop()

        self.transport, self.protocol = await loop.create_datagram_endpoint(
            lambda: MulticastDatagramProtocol(
                loop, self, self.mgrp, self.mport, self.mip, self.eif
            ),
            sock=self.sock,
        )

        self.r = asyncio.StreamReader(loop=loop)
        self.r.set_transport(self.transport)
        self.w = asyncio.StreamWriter(self.transport, self.protocol, self.r, loop)
        self.w.write = lambda data: self.transport.sendto(
            data, (broadcast_addr, self.mport)
        )

        return (self.r, self.w)  # retourne un (StreamReader, StreamWriter)

    def add_datagram(self, data, addr):
        """add a datagram to the queue"""
        self.queue.put_nowait((data, addr))

    def msend(self, data):
        """send 'data' using multicast socket"""
        self.transport.sendto(data, (self.mgrp, self.mport))

    async def mrecv(self):
        """Wait for a datagram and return it with the corresponding address"""
        (data, addr) = await self.queue.get()
        return (data, addr)
