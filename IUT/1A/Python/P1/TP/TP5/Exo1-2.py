def Oalpha(mot1, mot2):
    """
    Cette fonction a pour but de déterminer l'odre des 2 mots dans l'alphabet
    Paramètres: para1: mot1(str), contient le premier mot
                para2: mot2(str), contient le deuxième mot
    Résultat: res(int)
    """
    n = 0
    res = 0
    
    while res == 0:
        if len(mot1) < n and res == 0:
            res = -1
        elif len(mot2) < n and res == 0:
            res = 1
        elif len(mot2) < n and len(mot1) < n and res == 0:
            res = 0
        else:
            if mot1[n] < mot2[n]:
                res = -1
            elif mot1[n] > mot2[n]:
                res = 1
            else:
                res = 0
        n += 1
        
    return res

mot1 = str(input("Mot1= "))
mot2 = str(input("Mot2= "))

print(Oalpha(mot1, mot2))