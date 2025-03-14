from random import randint
from time import time

# Variables
nbr_essai = int(input("Nombre essais: "))
nbr_Max = int(input("Nombre maximal: "))
a = randint(0,nbr_Max)
n = randint(0,nbr_Max)
compteur = 0
t = time()

#On fait le test
for i in range(nbr_essai):
  print(a,'x',n,'=',end='')
  resultat = int(input())
  vrai = a*n
  while resultat != vrai:
    compteur += 1
    print('Mavaise réponse')
    print(a,'x',n,'=', end='')
    resultat = int(input())
  a = randint(0,15)
  n = randint(0,15)

#On affiche les résultats
temps = '{:.2f}'.format(time()-t)
print("Vous avez fait", temps,"secondes et",compteur,"fautes")
