#!/usr/bin/python3

################################################
## Exercice de tri                            ##
## Nom: ALLAIN Lucas                          ##
################################################

def tribulle(liste):
    """
    tri une liste en suivant l'algorithme du tri à bulle
    parametre:
    resultat: Attention cette fonction ne retourne aucun résultat mais modifie la liste
    N'oubliez le print(liste) à la fin de chaque itération de la grande boucle
    """

    while not sort(liste) :
        for i in :
            if liste[i] <liste[i+1]:
                liste[i],liste[i+1] = liste[i+1],liste[i]


l=[15,2,78,5,34,1]
print(tribulle(l))
assert l==[1,2,5,15,34,78],"Pb Appel tribulle("+str(l)+")"
