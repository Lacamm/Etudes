# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module case.py
   ~~~~~~~~~~~~~~
   
   Ce module gère les cases du plateau du CLUEDO. 
"""


# constantes gérant les categories de case
# VIDE indique que cet emplacement du plateau n'est pas une case
# COULOIR indique les cases sont des couloirs.
# les cases dont la catégorie est supérieur à 0 sont des pièces 
# et l'entier est le numéro de la pièce en question
# les cases dont la catégorie est inférieur à 0 sont les points de départ 
# des joueurs, la valeur absolue de cette catégorie correspond au numéro du joueur
VIDE=None
COULOIR=0

# --------------------
# Constructeur
# --------------------

def Case(_categorie, _contenu):
    """
    retourne une nouvelle case
    _categorie : la catégorie de la case
    _contenu   : indique le contenu de la case. None si il n'y a pas de pion
                 sinon c'est un entier indiquant le numéro du joueur 
    """
    return[_categorie, _contenu]

# --------------------
# getter
# --------------------

def getCategorie(case):
    """
    retourne la catégorie de la case
    case : une case du plateau de CLUEDO 
    """ 
    return case[0]

def getContenu(case):
    """
    retourne le contenu de la case
    case : une case du plateau de CLUEDO 
    """ 
    return case[1]

def estLibre(case):
    """
    indique si la case est libre ou non
    case : une case du plateau de CLUEDO 
    """ 
    return (getContenu(case) == None)

def estDepart(case):
    """
    retourne un entier 0 si la case n'est pas une case départ
    et le numéro du joueur dont c'est la case départ sinon
    case : une case du plateau de CLUEDO 
    """ 
    if getCategorie(case) != None and getCategorie(case) < 0:
        return -getCategorie(case)
    return 0

# --------------------
# setters
# -------------------- 

def setContenu(case,contenu):
    """
    change le contenu de la case
    case    : une case du plateau de CLUEDO
    contenu : le nouveau contenu de la case
    """ 
    case[1] = contenu
    

def setCategorie(case, categorie):
    """
    change la catégorie de la case
    case      : une case du plateau de CLUEDO
    categorie : la nouvelle catégorie de la case
    """ 
    case[0] = categorie