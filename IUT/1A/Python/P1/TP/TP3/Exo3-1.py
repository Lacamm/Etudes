def nombres_pairs(nombres,taille):
    """
    Objectif: Cette fonction a pour objectif de trier les nombres pairs dans une liste et
    dans faire la somme
    Paramétres:
        Param1: liste des nombres à trier
    Résultat: Un int qui est la somme des nombres pairs
    """
    resultat = 0
    for i in range(taille):
        if nombres[i]%2 == 0:
            resultat = resultat + nombres[i]
    return resultat

taille = int(input("Taille de la liste: "))
nombres = []
for n in range(taille):
    nombres.append(int(input("Un nombre: ")))

print(nombres_pairs(nombres,taille))
