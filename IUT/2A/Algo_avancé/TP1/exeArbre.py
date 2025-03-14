from arbre import *

#Question 1

a = Arbre(3,[])
b = Arbre(7,[])
c = Arbre(5,[a,b])


#Question 2 & 3

t1 = Arbre("n1",[Arbre("f4",[]),
    Arbre("n2",[Arbre("f5",[]),
    Arbre("n3",[Arbre("f1",[]),
    Arbre("f2",[]),Arbre("f3",[])])])])


#Question 4

def countLeaves(a):
    if a.enfants() == []:
        return 1
    else:
        total = 0
        for n in a.enfants():
            total += countLeaves(n)
    return total

#question 5

def countInternalNodes(a):
    if len(a.enfants()) == 0:
        return 0
    else:
        total = 1
        for n in a.enfants():
            total+=countInternalNodes(n)
    return total


#Question 6

def heightTree(a):
    hauteur = 0
    for n in a.enfants():
        hauteur=max(hauteur,1+heightTree(n))
    return hauteur


#Question 7 

def degree(a):
    if len(a.enfants()) == 0:
        return 0
    else:
        d = len(a.enfants())
        for n in a.enfants():
            d = max(d, degree(a))
    return d


#Tests


arbre8 = Arbre.Feuille(8)
arbre7 = Arbre.Feuille(7)
arbre6 = Arbre.Feuille(6)
arbre5 = Arbre.Feuille(5)
arbre4 = Arbre.Feuille(4)

arbre3 = Arbre(3, [arbre6, arbre7, arbre8])
# arbre2 = Arbre(2, [arbre4, arbre5, arbre8])
arbre1 = Arbre(1, [ arbre3])
#---------------------------------
arbre14 = Arbre.Feuille(4)
arbre15 = Arbre.Feuille(5)

arbre17 = Arbre.Feuille(7)

arbre13 = Arbre(3, [arbre14, arbre15])
arbre16 = Arbre(6, [arbre17])
arbre12 = Arbre(2, [arbre16])
arbre11 = Arbre(1, [arbre12, arbre13])

#---------------------------------
tree7 = Arbre.Feuille(7)
tree6 = Arbre.Feuille(6)
tree5 = Arbre.Feuille(5)
tree4 = Arbre.Feuille(4)
tree8 = Arbre.Feuille(8)

tree3 = Arbre("+", [tree6, tree7, tree8])
tree2 = Arbre("+", [tree4, tree5])
tree1 = Arbre("*", [tree2, tree3])

#---------------------------------

print(arbre1)
print(countLeaves(arbre1))
print(countInternalNodes(arbre1))
print(heightTree(arbre8))
#--------------------------------
print("------------------------------")
print(arbre11)
print(countLeaves(arbre11))
print(countInternalNodes(arbre11))
print(heightTree(arbre11))
print(degree(arbre11))

# #--------------------------------
# print("------------------------------")
# print(tree1)
# print(countLeaves(tree1))
# print(countInternalNodes(tree1))
# print(heightTreeTree(tree1))
# print(degree(tree1))
# print(check(tree1))