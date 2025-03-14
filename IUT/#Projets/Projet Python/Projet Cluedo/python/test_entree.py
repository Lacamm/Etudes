import entree

entree1 = entree.Entree(3, 5, 2)
entree2 = entree.Entree(0, 1, 18)

assert entree.getDirection(entree1) == "OUEST"
assert entree.getLigne(entree1) == 5
assert entree.getColonne(entree1) == 2

assert entree.getDirection(entree2) == "NORD"
assert entree.getLigne(entree2) == 1
assert entree.getColonne(entree2) == 18
