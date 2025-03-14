#!/usr/bin/python3

######################################################################
# Feuille de TP5
# NOM : ALLAIN Lucas
#######################################################################

#######################################################################
print("==========================================")
print("Exercice 1 - Utilisation de max et sorted avec clés")

liste = ['bonjour','au_revoir','bienvenue','ambulancier']


def le_plus_long(chaine):
    return max(liste, key=len)

assert le_plus_long(liste) == 'ambulancier'


def tri_couple(couple):
    return couple[1]

def tri_liste_couple(liste):
    return sorted(liste, key=tri_couple)

assert tri_liste_couple([(1,5),(2,9),(3,2)]) == [(3,2),(1,5),(2,9)]

print(" Exercice 1 fait !!!")

print("==========================================")
print("Exercice 2 - Fonctions locales")

def f(liste, ensemble):
    """
    Trie une liste suivant les valeurs d'un ensemble
    """
    def est_dans_ensemble(x):
        if x in ensemble:
            return 0
        else:
            return 1

    return sorted(liste, key=est_dans_ensemble)

l1 = [1,2,6,4,5,3]
l2 = [5,2,3,8,9]

e1 = set()
e1.add(6)

e2 = set()
e2.add(3)
e2.add(1)
e2.add(5)
e2.add(8)

assert f(l1,e1) == [6, 1, 2, 4, 5, 3]
assert f(l2,e2) == [5, 3, 8, 2, 9]


def tri_dico(dico):
    """
    Trie un dictionnaire en fonction de ses valeurs
    """
    def à_faire ():
        """
        Inutile ici car len() est une
        fonction  déjà présente dans python
        """
        pass

    return sorted(dico,key=len)

assert tri_dico({'un':1, 'trois':3})


def tri_ensemble(essais,cible):
    """
    Renvoie l'entier de l'ensemble
    le plus proche de la cible
    """
    def à_faire(x):
        return cible-x

    return sorted(essais,key=à_faire)[0]

ensemble = set()

ensemble.add(5)
ensemble.add(6)
ensemble.add(8)
ensemble.add(3)

entier = 10

assert tri_ensemble(ensemble, entier) == 8


def tri_liste(essais,cible):
    """
    Renvoie la liste triée de l'entier plus
    proche de la cible au plus éloigné
    """
    def à_faire(x):
        return cible-x

    return sorted(essais,key=à_faire)

liste_essais = [5,6,8,3]
entier = 10

assert tri_liste(liste_essais,entier) == [8, 6, 5, 3]


def tri_liste_mot(liste_mot, cible):
    """
    Renvoie le mot le plus proche
    du mot cible depuis une liste
    """
    def à_faire(mot):
        cpt = len(cible)
        for lettre in range(len(cible)):
            if mot[lettre] == cible[lettre]:
                cpt -= 1
        return cpt
    
    return sorted(liste_mot,key=à_faire)[0]

assert tri_liste_mot(["tulas","slaut","bonjour"],"salut") == "slaut"

        
def les_petits_puis_les_grands (liste, pivot):
    """
    Retourne une liste des éléments les plus petits
    jusqu'au plus grand par rapport à un autre élément
    """
    def compare (a):
        if a < pivot:
            return -1
        elif a == pivot:
            return 0
        else:
            return 1
    return sorted (liste, key=compare)

assert les_petits_puis_les_grands([8,6,4,2,3,7,1,2,5],5) == [4, 2, 3, 1, 2, 5, 8, 6, 7]

# Message d'erreur: "compare() missing 1
#  required positional argument: 'b'"

## La clé remplie est mauvaise


def mystere (liste):
    """
    Renvoie la position de l'élément le plus grand
    """
    def get(i):
        return liste[i]
    return max(range(len(liste)), key=get)
    
assert mystere([8,247,9,55558485,3]) == 3


print(" Exercice 2 fait !!!")


print("==========================================")
print("Exercice 3 - Bricolage")


plan_assemblage_guitare={'manche':1,'caisse':1,'corde':6}
plan_assemblage_ukulele={'manche':1,'caisse':1,'corde':4}
plan_assemblage_instrument_bizarre={'manche':2,'caisse':3,'pied':2}

inventaire_atelier_Florent={'manche':2,'caisse':2,'corde':8}
inventaire_atelier_Celine={'manche':1,'caisse':4,'pied':3,'corde':5}
inventaire_atelier_Sophie={'manche':15,'caisse':40,'pied':32,'corde':57}


    
print("   Avez-vous pensé à écrire des tests pour l'exercice 3 ?")

print("==========================================")
print("Exercice 4 -Ultimate Frisbee - le retour !")

matches = {
    ('Orléans', 'Champignac') : (17,11),
    ('Tours', '0rléans') : (7, 0),
    ('Champignac', 'Tours') : (10,8),
    ('Caen', 'Orléans') : (3, 13),
    ('Caen', 'Tours') : (6, 2),
    ('Champignac', 'Caen') : (0,0),
    ('Champignac', 'Orléans') : (0,0),
    ('Orléans', 'Tours') : (7, 5),
    ('Tours', 'Champignac') : (4, 0),
    ('Orléans', 'Caen') : (5, 4),
    ('Tours', 'Caen') : (8, 11),
    ('Caen', 'Champignac') : (11, 12),
}
  
