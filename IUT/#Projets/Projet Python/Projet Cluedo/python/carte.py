# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module carte.py
   ~~~~~~~~~~~~~~~
   
   Ce module gère les cartes du Cluedo. Une carte fait partie d'une des trois catégorie (professeur,matière,salle)
   Elle porte un nom et elle possède une description et une image
"""

# constantes permettant de définir les trois catégorie de carte
PROFESSEUR=1
MATIERE=2
SALLE=3

# Dictionaire qui contient les noms des catégories
nomCategorie={PROFESSEUR:"Professeurs",MATIERE:"Matières",SALLE:"Salles"}

#-----------------------------------------
# contructeur
#-----------------------------------------
def Carte(_num,_nom,_categorie,_description,_distribuable=True):
    """
    retourne une carte du CLuedo
    _num        : numéro de la carte
    _nom        : nom de la carte
    _categorie  : catégorie de la carte (parmi PROFESSEUR, MATIERE, SALLE
    _description: une chaine de caractères contenant la description de la carte
    _distribuable: un booléen indiquant si la carte est distribuable ou non
    """
    return [_num,_nom,_categorie,_description,_distribuable]

#-----------------------------------------
# accesseurs
#-----------------------------------------
def getNum(carte):
    """
    retourne le numéro d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    return carte[0]

def getNom(carte):
    """
    retourne le nom d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    return carte[1]

def getCategorie(carte):
    """
    retourne la catégorie d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    return carte[2]

def getNomCategorie(carte): 
    """
    retourne le nom de la catégorie d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    nom=''
    numcat = getCategorie(carte)
    if numcat == 1:
        nom ='Professeurs'
    if numcat == 2:
        nom ='Matières'
    if numcat == 3:
        nom ='Salles'
    return nom

def getDescription(carte):
    """
    retourne la description d'une carte du Cluedo
    carte: une carte du Cluedo
    """
    return carte[3]

def estDistribuable(carte):
    """
    indique si une carte est distribuable ou non
    carte: une carte du Cluedo
    """
    return carte[4]


#-------------------------
# fonctions annexes
#-------------------------
def categorieFromNom(nomCat):
    """
    retourne l'identifiant d'un nom de catégorie 
    nomCart: un nom de catégorie
    """
    res=None
    if nomCat == 'Professeurs':
        res = 1
    if nomCat == 'Matières':
        res = 2
    if nomCat == 'Salles':
        res = 3
    return res

def categorieFromNum(numCat):
    """
    retourne le nom d'une categorie
    numCat: un identifiant de catégorie
    """
    nom=None
    if numCat == 1:
        nom ='Professeurs'
    if numCat == 2:
        nom ='Matières'
    if numCat == 3:
        nom ='Salles'
    return nom

def estNomCategorie(nomCat):
    """
    indique si une chaine de caractères est un nom de catégorie ou non
    nomCat: un nom de catégorie
    """
    ok = False
    for noms in nomCategorie.values():
        if nomCat == noms:
            ok = True
    return ok

#-------------------------
# transformer une carte en chaine de caractères
#-------------------------
def string(carte):
    """
    retourne une chaine de caractères représentant une carte du Cluedo
    carte: une carte du Cluedo
    """
    return '-'*10+'\ncarte '+getNomCategorie(carte)+' numéro: '+str(getNum(carte))+'\nnom: '+getNom(carte)+'\ndescription: '+getDescription(carte)+'\n'
