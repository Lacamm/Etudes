def booleens(liste, nombre):
    """
    Cette fonction a pour objectif d'initialiser une liste de booléen suivant un
    multiple
    Paramètres:
        para1: la taille de la liste à créée
    Résultat: une liste de booléenns
    """
    listeB = []

    for n in range(len(liste)):

        if n%nombre == 0 and n != nombre:
            listeB.append(False)
        else:
            listeB.append(True)

    return listeB

nombre = int(input("Un mutiple: "))

print(booleens([True, True, False, True, True, True, False],nombre))
