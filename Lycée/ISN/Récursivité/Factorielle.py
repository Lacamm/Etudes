def factorielle(rang):
  if rang == 1:
    return 1
  else:
    return rang*factorielle(rang-1)

from time import time
t = time()
rang = int(input('Nombre= '))
print(factorielle(rang))
print(time()-t,'ms')
