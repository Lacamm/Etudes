def listeSC(para1,para2):
    """
    Cette fonction a pour objectif de tri dans l'ordre croissant
    la somme de deux listes
    Paramètres: para1: l1(list)
                para2: l2(list)
    Résultat: Un liste triée dans l'ordre croissant
    """
    res = []
    i = 0
    while len(l1) > i or len(l2) > i:
        if l1[i] < l2[i]:
            res.append(l1[i])
            res.append(l2[i])
        else:
            res.append(l2[i])
            res.append(l1[i])
        i+=1
    return res

l1 = [1,3,5,7,9]
l2 = [0,2,4,6,8]

print(listeSC(l1,l2))
