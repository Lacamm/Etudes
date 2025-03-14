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
assert majusculesConsécutives('Mot') == False


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
assert majusculesConsécutives('Mot') == False

# Exercice 3 - Slicing
########################################################################
# Question a
liste[:2]

# Question b

# Question c

# Question d

# Question e


# Exercice 4 - Suite de syracuse
########################################################################


# Exercice 5 - mot de passe
########################################################################
