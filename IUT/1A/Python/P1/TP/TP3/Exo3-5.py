def nombres_consecutifs(nombres, taille):
    """
    Objectif: Cette fonction a pour objectif de déterminer la longeur de la plus
    grande suite de nombres consécutifs
    Paramètres:
        Param1: Une liste
    Résultat: Un int
    """
    grd_suite = 1
    prec = ''
    res = 0
    for i in nombres:
        if i == prec:
            grd_suite += 1
            if grd_suite > res:
                res = grd_suite
        else:           
            grd_suite = 1 
        prec = i
    return res

taille = int(input("Taille de la liste: "))
nombres = []
for n in range(taille):
    nombres.append(int(input("Un nombre: ")))

print(nombres_consecutifs(nombres,taille))
