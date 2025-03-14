def consecutif(nombre):
    res = False
    unite = 0
    prec = 0
    while nombre != 0:
        prec = unite
        unite = nombre%10
        nombre = (nombre-unite)//10
        if unite == prec:
            res = True
    return res

nombre = 2909

print(consecutif(nombre))