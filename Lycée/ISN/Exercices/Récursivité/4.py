def PGCD(dividende, diviseur):
    if diviseur == 0:
        return dividende
    else:
        return (PGCD(diviseur,dividende%diviseur))

from time import time
t = time()
dividende = int(input('dividende: '))
diviseur = int(input('diviseur: '))
print(PGCD(dividende, diviseur))
print((time()-t),'ms')
