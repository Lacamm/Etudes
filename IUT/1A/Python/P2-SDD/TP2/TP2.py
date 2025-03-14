#!/usr/bin/python3

#######################################################################
# Feuille de TP 2
# NOM : Allain Lucas
#######################################################################

#######################################################################
print("==========================================")
print("Exercice 1")

def tousMultiplesDe (listeEntiers, n):
    """
    Renvoie un booléen qui indique si tous les éléments de
    'listeEntiers' sont multiples de 'n'
    """
    ok = True
    for valeur in listeEntiers:
        if (valeur % n != 0):
            ok = False
    return ok

listeExemple = [3, 15, 18, 9]
multiple = 3
tousMultiplesDe(listeExemple,multiple)

assert tousMultiplesDe(listeExemple, 3)
assert not tousMultiplesDe(listeExemple, 5)
assert tousMultiplesDe([],5)



def passeModulo(listeEntiers, n):
    for i in range(len(listeEntiers)):
        listeEntiers[i] = listeEntiers[i] % n
  
def tousMultiplesDe2(listeEntiers, n):
    ok = True
    liste=listeEntiers.copy()
    passeModulo(liste,n)
    for valeur in liste:
        if (valeur != 0):
            ok = False
    return ok

listeExemple = [3, 15, 18, 9]
multiple = 3
print(tousMultiplesDe2(listeExemple, multiple))

assert tousMultiplesDe2(listeExemple, 3)
assert not tousMultiplesDe2(listeExemple, 5)
assert tousMultiplesDe2([],5)




#######################################################################
print("==========================================")
print("Exercice 2 : Dictionnaires")


def premieres_occurences(liste):
    """ 
    résultat : un dictionnaire dont les clés sont les éléments de
    'liste' et les valeurs l'indice de la première occurence de chaque élément
    """
    occurence = {}
    for i in range (len(liste)):
        if liste[i] not in occurence.keys():
            occurence[liste[i]] = i
    return occurence

liste=['a','b','b','a','!']
premieres_occurences(liste)

assert premieres_occurences(liste)=={'a':0, 'b':1, '!':4}
assert premieres_occurences([])=={}
print("Bravo ! Vous avez terminé la première question de cet exercice")
print('')


def dernieres_occurences(liste):
    """ 
    résultat : un dictionnaire dont les clés sont les éléments de
    de 'liste' et les valeurs l'indice de la dernière occurence de chaque élément
    """
    occurence = {}
    for i in range (len(liste)):
        if liste[i] in occurence.keys():
            occurence[liste[i]] = i
    return occurence

liste=['a','b','b','a','!']
print(dernieres_occurences(liste))

assert dernieres_occurences(liste)=={'a':3, 'b':2, '!':4}
assert dernieres_occurences([])=={}
print("Félicitation ! Vous avez brillamment terminé cet exercice")


#######################################################################
print("==========================================")
print("Exercice 3 : les Avengers")



def intelligenceMoyenne(dico):
    """
    paramètre : un dictionnaire (non vide) dont les clefs sont le nom de personnages,
    et les valeurs des tuples contenant la force (int), 
    l'intelligence (int) et la description (str) de ce personnage
    résultat : l'intelligence moyenne des personnages (float)
    """
    pass

# exemple de dictionnaire bidon pour faire des tests :
superHero={ 
    'Spiderman' : (5, 5, 'araignée à quatre pattes'),
    'Hulk':(4,7,"Grand homme vert"),
    'Agent 13':(2,3,'agent 13'),
    'M Becker':(2, 9, 'Expert en graphes'),
}

# N OUBLIEZ PAS D ECRIRE AU MOINS UN TEST PAR FONCTION


def kikelplusfort(dico):
    """
    paramètre : un dictionnaire (non vide) dont les clefs sont le nom de personnages,
    et les valeurs des tuples contenant la force (int), 
    l'intelligence (int) et la description (str) de ce personnage
    résultat : le nom du personnage le plus fort (str)
    """
    pass



def lesCretins(dico):
    """
    paramètre : un dictionnaire (non vide) dont les clefs sont le nom de personnages,
    et les valeurs des tuples contenant la force (int), 
    l'intelligence (int) et la description (str) de ce personnage
    résultat : l'ensemble des noms des personnages dont l'intelligence est inférieure à la moyenne.
    """
    pass


print("Avez-vous pensé à écrire au moins un test par fonction ?")

#######################################################################
print("==========================================")
print("Exercice 4 : la maison qui rend fou")


mqrf1 = {
    "Abribus":"Astus",
    "Jeancloddus":"Abribus",
    "Plexus":"Gugus",
    "Astus":None,
    "Gugus":"Plexus",
    "Saudepus":None
    }

mqrf2 = {
    "Abribus":"Astus",
    "Jeancloddus":None,
    "Plexus":"Jeancloddus",
    "Astus":"Gugus",
    "Gugus":"Plexus",
    "Saudepus":"Bielorus",
    }

mqrf3 = {
    "Abribus":"Astus",
    "Jeancloddus":None,
    "Plexus":"Saudepus",
    "Astus":"Gugus",
    "Gugus":"Plexus",
    "Saudepus":None,
    }
    
def verifieCoherence(mqrf):
    """
    cette fonction vérifie que chaque guichet donne le formulaire ou renvoie vers un guichet qui existe.
    paramètre : une "maison qui rend fou"
    résultat : un booleen
    """
    pass




def conditionDeCesar(mqrf):
    """
    cette fonction vérifie que la mqrf vérifie la condition de César : un guichet qui ne donne pas le formulaire doit renvoyer vers un guichet dont le nom est plus loin dans l'ordre alphabétique
    paramètre : une "maison qui rend fou"
    résultat : un booleen
    """
    pass





def quelGuichet(mqrf, guichet):
    """
    paramètres :
      - mqrf est une maison qui rend fou qui vérifie la condition de César
      - guichet est le nom d'un guichet de la mqrf
    résultat : le nom du guichet qui finit par donner le formulaire
    """
    pass




def possible(mqrf, guichet):
    """
    paramètres :
      - mqrf est une maison qui rend fou
      - guichet est le nom d'un guichet de la mqrf
    résultat : un booléen indiquant s'il est possible d'obtenir le formulaire A-38 dans la mqrf en commençant par s'adresser au guichet
    """
    pass


print("Avez-vous pensé à écrire au moins un test par fonction ?")
