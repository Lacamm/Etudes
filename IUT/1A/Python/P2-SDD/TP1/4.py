#!/usr/bin/python3

def syracuse(nombreDepart):
    """
    Cette fonction réalise la suite de Sycaruse
    Paramètre : le nombre de départ (int)
    Résultat : la suite (list)
    """
    res = [nombreDepart]

    while res[-1] != 1:
        if res[-1] %2 == 0:
            res.append(res[-1]//2)
        else:
            res.append((res[-1]*3)+1)
    return res

nombreDepart = 5
print(syracuse(nombreDepart))

assert syracuse(3) == [3,10,5,16,8,4,2,1]
assert syracuse(5) == [5,16,8,4,2,1]