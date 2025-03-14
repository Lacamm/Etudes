def somme_entiers(entier):
    """
    Objectif: Cette fonction a pour objectif de faire la somme de tout les
    premiers entiers d'un nombre
    Paramètres:
        Param1: un entier
    Résultat: Un int qui est la somme des premiers entiers du nombre
    """
    resultat = 0
    for n in range(entier+1):
        resultat = resultat + n
    return resultat

entier = int(input("Un entier: "))

print(somme_entiers(entier))
