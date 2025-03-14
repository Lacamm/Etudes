#!/usr/bin/python3

from timeit import timeit

######################################################################
# Feuille de TP 3
# NOM : ALLAIN Lucas
#######################################################################

#######################################################################
print("==========================================")
print("Exercice 1 - Performance")
def elements_en_commun_v1(liste1, liste2):
    """
    resultat : la liste des éléments communs à 'liste1' et 'liste2'
    """
    en_commun=[]
    for element in liste1:
        if element in liste2: # lent
            en_commun.append(element)
    return en_commun
    
    
def elements_en_commun_v2(liste1, liste2):
    """
    resultat : l'ensemble des éléments communs à 'liste1' et 'liste2'
    """
    ensemble1 = set(liste1)
    ensemble2 = set(liste2)
    en_commun=set()
    for element in ensemble1:
        if element in ensemble2: #lent
            en_commun.add(element)
    return en_commun


from timeit import timeit

taille_des_listes =60
liste1 = [2*n for n in range(taille_des_listes)]
liste2 = [2*n+1 for n in range(taille_des_listes)]

temps1 = timeit('elements_en_commun_v1(liste1, liste2)', globals=globals(),number=100)*1000
temps2 = timeit('elements_en_commun_v2(liste1, liste2)', globals=globals(),number=100)*1000

print("avec n=",taille_des_listes)
print(temps1)
print(temps2)
    
print("==========================================")
print("Exercice 2 - Fanfare")


candidatures = [('Kim Gordon', 'Apito'),('Superman', 'Trompette'),('Frank Zappa', 'Banjo'),('Chico Science', 'Apito'),('Frank Zappa', 'Trompette')]

def premier_candidat(candidatures, instrument):
    """
    param:
     - candidatures est une liste de tuples (nom, instrum) où nom et instrum sont des str
     - instrument est un str
    return: le nom (str) de la première personne qui a candidaté pour cet instrument
    """
    musicien = None
    for (personne, instru) in candidatures:
        if instru == instrument:
            musicien = personne
            return musicien
    return None

instrument = 'Banjo'
print(premier_candidat(candidatures, instrument))
print(premier_candidat(candidatures, 'Apito'))
print(premier_candidat(candidatures, 'Guitarron'))


# TESTS A COMPLETER ET/OU CORRIGER
assert premier_candidat(candidatures, 'Banjo')== 'Frank Zappa'
assert premier_candidat(candidatures, 'Apito')== 'Kim Gordon'
assert premier_candidat(candidatures, 'Guitarron')== None

print("    Bravo, vous avez terminé la question 2.3 :)")



def tous_candidats(candidatures):
    """
    param: candidatures est une liste de tuples (nom, instrum) où nom et instrum sont des str
    renvoie l'ensemble de toutes les personnes qui ont candidaté pour faire partie de la fanfare.
    """
    ListePersonne = set()
    for (personne, _) in candidatures:
        ListePersonne.add(personne)
    return ListePersonne

print(tous_candidats(candidatures))

# TESTS A COMPLETER ET/OU CORRIGER
assert tous_candidats(candidatures)== {'Frank Zappa','Kim Gordon','Superman','Chico Science'}

print("    Bravo, vous avez terminé la question 2.4 :)")
print()


def compose_fanfare(candidatures):
    """
    param: candidatures est une liste de tuples (nom, instrun) où nom et instrum sont des str
    renvoie un dictionnaire dont les clés sont les personnes qui seront invitées à faire partie de la fanfare, et les valeurs sont les instruments dont ils joueront.
    Pour cela, nous prenons pour chaque instrument la personne qui a candidaté en premier, sauf si elle joue déjà d'un autre instrument dans la fanfare.
    """
    ListeParticipants = {}
    for (personne, instrument) in candidatures:
        if instrument not in ListeParticipants.values() and personne not in ListeParticipants.keys():
            ListeParticipants[personne] = instrument
    return ListeParticipants

print(compose_fanfare(candidatures))
print()

# Un petit lien pour les complexités des opérateurs en Python
# https://wiki.python.org/moin/TimeComplexity

# TESTS A COMPLETER ET/OU CORRIGER
assert compose_fanfare(candidatures)== {'Kim Gordon': 'Apito', 'Superman': 'Trompette', 'Frank Zappa': 'Banjo'}

candidatures2=[('Albert','Apito'), ('Bernard','Trompette'), ('Etienne','Trompette'), ('Carole','Apito'), ('Fanny', 'Apito'), ('Albert','Saxophone'),('Etienne','Trompette'), ('Dalida','Saxophone'), ('Bernard','Piano'), ('Carole','Piano')]
print("    Très bien ! Vous avez terminé la question 2.6")

def candidats_malheureux(candidatures):
    """
    param: candidatures est une liste de tuples (nom, instrun) où nom et instrum sont des str
    renvoie l'ensemble des candidats qui n'ont pas été retenus pour la fanfare
    """
    res = set()
    fanfare=compose_fanfare(candidatures)
    for (personne, instrument) in candidatures:
        if personne not in fanfare.keys():
            res.add(personne)
    return res

print(candidats_malheureux(candidatures))
print()

# TESTS A COMPLETER ET/OU CORRIGER
assert candidats_malheureux(candidatures)== {'Chico Science'}
assert candidats_malheureux(candidatures2)== {'Etienne','Fanny'}
print("    Parfait !! Vous pouvez passer à l'exercice suivant")

print("==========================================")
print("Exercice 3 - Cuisine")

# EXEMPLES A COMPLETER ET/OU CORRIGER

recetteCrepe={'oeufs': 4, 'farine': 0.250, 'lait': 0.450, 'sucre': 0.015 }

magasin1={'oeufs':0.52, 'farine':1.15, 'lait':5, 'sucre':4}
magasin2={'oeufs':1,  'lait':15, 'sucre':6}


def recette_possible(recette, magasin):
    """ 
    Indique si on peut se procurer dans le 'magasin' les ingrédients nécessaires à la 'recette'
	'recette' est un dictionnaire clés=nom des ingrédients valeurs=quantité nécessaire
	'magasin' est un dictionnaire clés=ingrédients disponibles valeurs=prix d'une quantité unitaire de l'ingrédient
	"""
    for (ingredient,_) in recette.items():
        if ingredient not in magasin.keys():
            return False
    return True

print(recette_possible(recetteCrepe, magasin1))
print(recette_possible(recetteCrepe, magasin2))

# TESTS A COMPLETER ET/OU CORRIGER SUIVANT VOS DONNÉES
assert recette_possible(recetteCrepe,magasin1)
assert not recette_possible(recetteCrepe,magasin2)

print("   Bravo, vous avez terminé la première question de cet exercice ")

def prix_recette(recette, magasin):
    """ 
	Calcule et retourne le prix total pour acheter les ingredients de la 'recette' dans un 'magasin'
    Rque : on suppose que recette_possible(recette,magasin)
    'recette' est un dictionnaire clés=nom des ingrédients valeurs=quantité nécessaire
    'magasin' est un dictionnaire clés=ingrédients disponibles valeurs=prix d'une quantité unitaire de l'ingrédient
    """
    
    prix = 0
    for (ingredient, quantité) in recette.items():
        if ingredient in magasin.keys():
            prix_unitaire = magasin.get(ingredient)
            prix += quantité*prix_unitaire
    return prix

print(prix_recette(recetteCrepe, magasin1))
print(prix_recette(recetteCrepe, magasin2))

# TESTS A COMPLETER ET/OU CORRIGER SUIVANT VOS DONNÉES
# ATTENTION ! ON NE FAIT PAS DE TEST D'ÉGALITÉ AVEC DES FLOTTANTS

assert abs(prix_recette(recetteCrepe, magasin1)-4.77)<=0.01

# print("   Parfait :) Vous pouvez passer à l'exercice suivant ! ")
print("========================================================\n")

########################################################################
# Exercice : La fanfare fait un rappel
########################################################################

print("==========================================")
print("Exercice 4 - Le retour de la fanfare")

#  besoins= ??

exemple_candidatures = [ ('Albert','Triangle'), ('Fanny','Triangle'), ('Gérard','Clarinette'), ('Albert','Clarinette'), ('Gérard','Hélicon'), ('Basile','Triangle'), ('Carole','Triangle'), ('David','Triangle'), ('Henri','Hélicon'), ('Basile','Clarinette'), ('Isaline', 'Clarinette')]

def recrute_besooins(candidatures, besoins):
    i = 0
    fanfare = {}
    copie_besoins = besoins.copy()
    while copie_besoins != {}:
        (nom,instrument) = candidatures[i]
        if nom not in fanfare:
            fanfare[nom] = instrumentcopie_besoins[instrument] -= 1
            if copie_besoins[instrument] == 0:
                copie_besoins.popo(indtrument)
        i += 1
    return fanfare

assert rescrute_besoins(exemple_candidature, besoins) = exemple_fanfare
# proposition de modélisation de la fanfare

#  exemple_fanfare= ??



