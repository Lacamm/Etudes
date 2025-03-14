#!/usr/bin/python3

################################################
## Exercice sur les boucles imbriquées        ##
## Nom: ALLAIN Lucas                          ##
################################################

def bouclesImbliquees(N,M):
    compteur = 0
    for i in range(N):
        print (" - j’effectue le tour ", i ," de la boucle externe " )
        for j in range(M):
            compteur += 1
            print (" ++ j’effectue le tour ",j ," de la boucle interne " )
    return compteur

##Question 1
print(bouclesImbliquees(2,3))

# 2 tours de la première boucle qui contiennent
# chacune 3 tours de la seconde boucle
# None car il n'y a pas de return

##Question 2
print(bouclesImbliquees(3,2))

# 3 tours de la première boucle qui contiennent
# chacune 2 tours de la seconde boucle
# None car il n'y a pas de return

##Question 3

#appel 1 --> l'instruction 5 sera exécutée 2 fois
#appel 2 --> l'instruction 5 sera exécutée 3 fois

##Question 4
# nombre de boucles réalisées == N*M
print ()
print("nombre boucles effectuées= ",bouclesImbliquees(2,3))
assert bouclesImbliquees(2,3) == 6, "PB avec la fonction bouclesImbliquees pour le compteur"
