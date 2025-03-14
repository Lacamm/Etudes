#!/usr/bin/python3

def majusculesConsécutives(mot):
    """
        Cette fonction détermine si un mot contient 2 majuscules consécutives
        Paramètre : Un mot (str)
        Résultat : Un booléen (bool)
    """
    precedent = ""
    res = False

    for lettre in mot:
        if lettre.isupper() and precedent.isupper():
            res = True
    return res

mot = 'Mot'
print(majusculesConsécutives(mot))

assert majusculesConsécutives('MOt')
assert majusculesConsécutives('Mot') == False