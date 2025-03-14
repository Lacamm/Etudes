from scapy.all import *

def display(z):
    print(z.summary())


def repondreARP(pa):
    parp=ARP(hwsrc='00:06:5B:12:00:04',
    hwdst=pa.hwsrc, psrc=pa.pdst, pdst=pa.psrc, op=2)
    peth=Ether(dst=pa.src, src='00:06:5B:12:00:04')/parp
    return peth


def reponseFantome(pa):
    if (ARP in pa):
        if (pa.op==1) and (pa.pdst=='172.18.0.39'):
            sendp(repondreARP(pa))

sniff(prn=reponseFantome)