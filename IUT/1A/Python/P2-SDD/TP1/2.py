#!/usr/bin/python3

def majusculesConsécutives(mot):
    """
        Cette fonction détermine si un mot contient 2 majuscules consécutives
        Paramètre : Un mot (str)
        Résultat : Un booléen (bool)
    """
    i = 0
    precedent = ""
    res = False

    while not res and i < len(mot):
        if mot[i].isupper() and precedent.isupper():
            res = True
        precedent = mot[i]
        i += 1

    return res

mot = 'MOt'
print(majusculesConsécutives(mot))

assert majusculesConsécutives('MOt')
assert not majusculesConsécutives('Mot')