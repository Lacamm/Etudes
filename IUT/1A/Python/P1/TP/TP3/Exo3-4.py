def lettres_consecutives(mot):
    """
    Objectif: Cette fonction a pour objectif de déterminer si un mot a 2 lettres
    identiques consécutives
    Paramètres:
        Param1: Un str
    Résultat: Un str
    """
    phrase = ""
    oui = ""
    for n in range(len(mot)-1):
        if mot[n] == mot[n+1]:
            oui = "oui"
    if oui == "oui":
        phrase = "Le mot contient 2 lettres identiques consécutives"
    else:
        phrase = "Le mot ne contient pas 2 lettres identiques consécutives"
    return phrase

mot = input("Un mot: ")

print(lettres_consecutives(mot))

