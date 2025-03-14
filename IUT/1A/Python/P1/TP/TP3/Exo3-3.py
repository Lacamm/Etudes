def premiers_pairs(entier):
    """
    Objectif: Cette fonction a pour objectif de faire la somme de tout les
    premiers entiers pairs d'un nombre
    Paramètres:
        Param1: un entier
    Résultat: Un int qui est la somme des premiers entiers pairs du nombre
    """
    resultat = 0
    for n in range(entier+1):
        if n%2 == 0:
            resultat = resultat + n
    return resultat

entier = int(input("Un entier: "))

print(premiers_pairs(entier))
