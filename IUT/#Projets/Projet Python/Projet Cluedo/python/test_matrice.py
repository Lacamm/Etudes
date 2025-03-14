import matrice

matrice1 = matrice.Matrice(4,4,1)
matrice2 = matrice.Matrice(2,3,0)


assert matrice.getNbLignes(matrice1) == 4
assert matrice.getNbColonnes(matrice1) == 4
assert matrice.getVal(matrice1,2,3) == 1

matrice11 = matrice1
matrice.setVal(matrice11,2,2,5)
assert matrice.getVal(matrice11,2,2) == 5


assert matrice.getNbLignes(matrice2) == 2
assert matrice.getNbColonnes(matrice2) == 3
assert matrice.getVal(matrice2,1,2) == 0
matrice21 = matrice2
matrice.setVal(matrice2,0,0,10)
assert matrice.getVal(matrice2,0,0) == 10