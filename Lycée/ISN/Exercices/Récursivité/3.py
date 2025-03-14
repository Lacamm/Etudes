def quotient(dividende, diviseur):
    if dividende<diviseur:
        return 0
    else:
        return 1 + quotient(dividende-diviseur,diviseur)

def reste(dividende, diviseur):
    if dividende<diviseur:
        return dividende
    else:
        return reste(dividende-diviseur,diviseur)

from time import time
t = time()
dividende = int(input("dividende: "))
diviseur = int(input("diviseur: "))
t = time()-t
print("quotient= ", quotient(dividende,diviseur))
print("reste= ", reste(dividende,diviseur))
print(round(t,2),'ms')
