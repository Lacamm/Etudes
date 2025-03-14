# -*- coding: utf-8 -*-
"""
Ce module fournit quelques fonctions pratiques pour manipuler la table de routage Linux.
Il offre une interface simplifiée à la bibliothèque pyroute2.
"""
from pyroute2 import IPRoute

ipr = IPRoute()


def ifname(idx):
    "nomme une interface à partir de son index [idx]"
    return ipr.link("get", index=idx)[0].get_attr("IFLA_IFNAME")


def getaddr(eif):
    "retourne l'adresse IP associée à l'interface nommée [eif]"
    return ipr.get_addr(label=eif, family=2)[0].get_attr("IFA_ADDRESS")


def setroute(net, gw):
    "remplace ou ajoute une règle de routage pour [net] via [gw]"
    ipr.route("replace", dst=net, gateway=gw)


def delroute(net, gw):
    "efface une règle de routage pour [net] via [gw]"
    ipr.route("del", dst=net, gateway=gw)


def getroutes():
    "liste les règles de routage IPv4 sous la forme (net,gw,if)"
    l = []
    for x in ipr.get_routes(family=2, table=254):
        dst = x.get_attr("RTA_DST")
        dst_len = x["dst_len"]
        gw = x.get_attr("RTA_GATEWAY")
        eif = ifname(x.get_attr("RTA_OIF"))
        if dst_len == 0:
            net = "0.0.0.0/0"
        else:
            net = "%s/%d" % (dst, dst_len)
        l.append((net, gw, eif))
    return l


def intofaddr(addr):
    "convertit une adresse IP en nombre"
    r = 0
    for s in addr.split("."):
        r = (r << 8) + int(s)
    return r


def addrinnet(addr, net):
    "teste si l'adresse [addr] appartient au réseau [net]"
    (dst, dst_len) = net.split("/")
    shift = 32 - int(dst_len)
    addr = intofaddr(addr)
    dst = intofaddr(dst)
    return (addr >> shift) == (dst >> shift)


if __name__ == "__main__":
    # affiche la table de routage :
    print("Destination        Gateway         Interface")
    for (net, gw, eif) in getroutes():
        print("%-18s %-15s %s" % (net, gw, eif))

    # affiche la liste des réseaux auxquels nous sommes directement connectés :
    print("\nConnected networks : ")
    for (net, gw, eif) in getroutes():
        if gw is None:
            print("  %s via %s (%s)" % (net, eif, getaddr(eif)))
