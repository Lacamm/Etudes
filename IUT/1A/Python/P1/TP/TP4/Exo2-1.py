def booleens(taille):
    """
    Cette fonction a pour objectif d'initialiser une liste de booléens
    Paramètres:
        para1: la taille de la liste à créée
    Résultat: une liste de booléenns
    """
    listeB = []

    for n in range(taille):
        if n == 0 or n == 1:
            listeB.append(False)
        else:
            listeB.append(True)

    return listeB

taille = int(input("La taille de la liste de booléens: "))

print(booleens(taille))
