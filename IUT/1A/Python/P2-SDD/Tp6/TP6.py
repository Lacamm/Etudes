#!/usr/bin/python3

######################################################################
# Feuille de TP6
# NOM : ALLAIN Lucas
#######################################################################

#######################################################################
print("==========================================")
print("Exercice 1 - Fonctions paramétrées par des fonctions")

def fonctionPoids(listeP):
    """
    Renvoie la somme des deux éléments dans un tuple de la liste
    """
    return listeP[0]+listeP[1]

def maxiParam(liste, fonction):
    """
    Renvoie l'élément le plus lourd de la liste
    """
    maxi = liste[0]
    valeur = fonction(maxi)
    for elem in liste:
        if fonction(elem) > valeur:
            maxi = elem
            valeur = fonction(maxi)
    return maxi

assert(maxiParam([(0,0),(10,0),(6,6,),(0,10)], fonctionPoids)) == (6,6)
assert(maxiParam([('E.T'),('téléphone'),('maison')],len)) == ('téléphone')


def taille(couple):
    """
    Renvoie la somme des deux éléments dans un tuple de la liste
    """
    return couple[0] + couple[1]

def sommePara(liste,fonction):
    """
    Renvoie la somme de des éléments de la liste
    """
    somme = 0
    for elem in liste:
        somme += fonction(elem)
    return somme

assert(sommePara([(0,10),(10,20),(1,1)], taille)) == 42
assert(sommePara([('E.T'),('téléphone'),('maison')],len)) == 18


print(" Exercice 1 fait")

print("==========================================")
print("Exercice 2 - Programme Télé")

dicoTV1 = {"Tout est bon dans le cochon":(20*60+45, 22*60+30),"Méga Cyclone":(20*60+50, 22*60+50), "Météo": (19*60+45, 20*60+00)}
dicoTV2 = {"Pimp my ride": (17*60+00, 20*60+00), "Man vs Wild":(18*60+30, 19*60+30), "Le 19:45": (19*60+45, 20*60+20), "On n'est pas réveillés": (4*60+00, 6*60+00)}

def heureDebut(progTV):
    """
    Trie Toutes les émissions du programme par heure de début
    """
    def triD(NomProg):
        return progTV[NomProg][0]
    return sorted(progTV.keys(), key= triD)


def heureFin(progTV):
    """
    Trie Toutes les émissions du programme par heure de fin
    """
    def triF(NomProg):
        return progTV[NomProg][1]
    return sorted(progTV.keys(), key= triF)

assert(heureDebut(dicoTV1)) == ['Météo', 'Tout est bon dans le cochon', 'Méga Cyclone']
assert(heureDebut(dicoTV2)) == ['On n\'est pas réveillés', 'Pimp my ride', 'Man vs Wild', 'Le 19:45']

assert(heureFin(dicoTV1)) == ['Météo', 'Tout est bon dans le cochon', 'Méga Cyclone']
assert(heureFin(dicoTV2)) == ['On n\'est pas réveillés', 'Man vs Wild', 'Pimp my ride', 'Le 19:45']


def enCours(heure, prog):
    """
    Renvoie l'ensemble des émissions en cours
    """
    res = set()
    for (emission,(debut, fin)) in prog.items():
        if debut < heure and fin > heure:
            res.add(emission)
    return res

#assert()


def premiereEmission(prog):
    """
    Renvoie la première émission de la journée
    """
    def Debut(NomProg):
        return prog[NomProg][0]
    return min(prog, key= Debut)

assert(premiereEmission(dicoTV2)) == "On n'est pas réveillés"

print(" Exercice 2 à faire + tests")

print("==========================================")
print("Exercice 3 - Approximations")


print(" Exercice 3 à faire + tests")