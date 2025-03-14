#!/usr/bin/python3

########################################################################
#   Feuille de TP1
#   NOM : ALLAIN Lucas
########################################################################

# Exercice 1 - Mémoire
########################################################################
# Question 1
def f(a):
    a=a+1
    # ICI
    return a
x=3
y=f(x)
z=f(y)

# Question 2
liste1 = [1, 3, 5, 9]
liste2 = [0, 2, 4]
liste3 = liste1 + liste2
liste2.append (6) # ICI

# Questions 3 et 4
def augmenteTous (liste):
    """
        Cette fonction incrémente de 1 tous les éléments de la liste
        Paramètre : une liste de nombre
        Résultat : None (rien)

    """
    for i in range (len(liste)):
        liste[i] = liste[i]+1 # ICI

maListe = [5, 3, 7, 9]
augmenteTous(maListe)
print(maListe)


# Exercice 2 - Fonction sur les chaînes de caractère
########################################################################

def majusculesConsécutives(mot):
    """
        Cette fonction détermine si un mot contient 2 majuscules consécutives
        Paramètre : Un mot (str)
        Résultat : Un booléen (bool)
    """
    res = False

    for i in range(0,len(mot),1):
        if mot[i].isupper() and mot[i+1].isupper():
            res = True
    return res

mot = 'Mot'
print(majusculesConsécutives(mot))

assert majusculesConsécutives('MOt')
assert not majusculesConsécutives('Mot')


def majusculesConsécutives(mot):
    """
        Cette fonction détermine si un mot contient 2 majuscules consécutives
        Paramètre : Un mot (str)
        Résultat : Un booléen (bool)
    """
    precedent = ""
    res = False

    for lettre in mot:
        if lettre.isupper() and precedent.isupper():
            res = True
    return res

mot = 'Mot'
print(majusculesConsécutives(mot))

assert majusculesConsécutives('MOt')
assert not majusculesConsécutives('Mot')


def majusculesConsécutives(mot):
    """
        Cette fonction détermine si un mot contient 2 majuscules consécutives
        Paramètre : Un mot (str)
        Résultat : Un booléen (bool)
    """
    i = 0
    precedent = ""
    res = False

    while not res and i < len(mot):
        if mot[i].isupper() and precedent.isupper():
            res = True
        precedent = mot[i]
        i += 1

    return res

mot = 'MOt'
print(majusculesConsécutives(mot))

assert majusculesConsécutives('MOt')
assert not majusculesConsécutives('Mot')

# Exercice 3 - Slicing
########################################################################
# Question a
liste[:2]

# Question b
liste[2:-3]

# Question c
liste[:len(liste)//2]

# Question d
liste[len(liste)//2:]

# Question e
liste[len(liste)//2]

# Question f
liste[len(liste)//2:(len(liste)//2)+5]


# Exercice 4 - Suite de syracuse
########################################################################
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

# Exercice 5 - mot de passe
########################################################################

def nombresCaractères(MDP):
    while len(MDP) < 8:
        #modifier le mot de passe
    return MDP

def nombreChiffres(MDP):
    chiffre  = False
    for caractere in  MDP:
        if caractere.isdigit():
            chiffre = True
    while not chiffre:
        #modifier le mot de passe
    return MDP

def nombreEspace(MDP):
    while ' ' in MDP:
        #modifier le mot de passe
    return MDP

def nombreMajuscules(MDP):
    majuscule  = False
    for caractere in  MDP:
        if caractere.isupper():
            majuscule = True
    while not majuscule:
        #modifier le mot de passe
    return MDP

def nombreMajusculesConsecutives(MDP):
    majusculesConsecutives = False
    for indice in range(len(MDP):
        if MDP[indice].isupper() and MDP[indice-1].isupper():
            majusculesConsecutives = True
    while majusculesConsecutives == True:
        #modifier le mot de passe
    return MDP

def ponctuation(MDP):
    ponctuation  = False
    for caractere in  MDP:
        if not caractere.isdigit() or not caractere.isalpha():
            ponctuation = True
    while ponctuation:
        #modifier le mot de passe
    return MDP

#Question 5.2

#!/usr/bin/python

def dialogueMotDePasse():

    ################ Fonctions ################
    def initialisation(MDP):
        motDePasse = str(input("Créez votre mot de passe: "))
        MDP = []
        for n in range(len(motDePasse)):
            MDP.append(motDePasse[n])
        return MDP

    def nombresCaracteres(MDP):
        while len(MDP) < 8:
            print("Votre mot de passe doit contenir au moins 8 caractères")
            initialisation(MDP)
        return MDP

    def nombreChiffres(MDP):
        chiffre  = False
        for caractere in  MDP:
            if caractere.isdigit():
                chiffre = True
        while not chiffre:
            print("Votre mot de passe doit contenir au moins 1 chiffre")
            initialisation(MDP)
        return MDP

    def nombreEspace(MDP):
        while ' ' in MDP:
            print("Votre mot de passe ne doit pas contenir d'espace")
            initialisation(MDP)
        return MDP

    def nombreMajuscules(MDP):
        majuscule  = False
        for caractere in  MDP:
            if caractere.isupper():
                majuscule = True
        while not majuscule:
            print("Votre mot de passe doit contenir au moins 1 majuscule")
            initialisation(MDP)
        return MDP

    def nombreMajusculesConsecutives(MDP):
        majusculesConsecutives = False
        for indice in range(len(MDP)):
            if MDP[indice].isupper() and MDP[indice-1].isupper():
                majusculesConsecutives = True
        while majusculesConsecutives == True:
            print("Votre mot de passe ne doit pas contenir 2 majuscules consécutives")
            initialisation(MDP)
        return MDP

    def ponctuation(MDP):
        ponctuation  = False
        for caractere in  MDP:
            if not caractere.isdigit() or not caractere.isalpha():
                ponctuation = True
        while ponctuation:
            print("Votre mot de passe ne doit pas contenir de ponctuation")
            initialisation(MDP)
        return MDP


    ################ Main  ################

    global MDP
    MDP = []

    initialisation(MDP)
    nombresCaracteres(MDP)
    nombreChiffres(MDP)
    nombreEspace(MDP)
    nombreMajuscules(MDP)
    nombreMajusculesConsecutives(MDP)
    ponctuation(MDP)

    motDePasse = "".join(MDP)
    print(motDePasse)
    print("Votre mot de passe est créé!")

    return motDePasse


dialogueMotDePasse()


## Le programme fonctionne si on utilise pas la fonction
## dialogueMotDePasse() et ce si on écrit le mot de passe
## correctement la première fois sinon il reste bouclé dans
## la boucle qui n'a pas été vérifiée et je ne sais pas
## pourquoi

#Question 5.3


#!/bin/bash
./ motDePasse.py >> liste_mot_de_passe.txt
