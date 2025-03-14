#!/usr/bin/python3

######################################################################
# Feuille de TP5
# NOM : ALLAIN Lucas
#######################################################################

#######################################################################
print("==========================================")
print("Exercice 1 ")

def ecart(couple):
    return abs(couple[1]-couple[0])

def paire_plus_etendue(liste):    
    return max(liste, key=ecart)


assert paire_plus_etendue([(6,2), (4,1), (2,7)]) == (2,7)





def ecart2(valeurs):
    return max(valeurs)-min(valeurs)

def liste_la_plus_etendue(liste):
    return max(liste, key=ecart2)


assert liste_la_plus_etendue([[3,-3],[1,2,3],[1]]) == [3, -3]