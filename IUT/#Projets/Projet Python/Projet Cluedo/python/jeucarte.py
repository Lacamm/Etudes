    # -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module 
   ~~~~~~~~~~~~~~~
   
   Ce module gère un jeu de cartes de cluedo.
   ATTENTION !!!
        il y a une carte particulière: il s'agit de la carte de
        la salle où l'on peut tenter de gagner (la salle des archives)
        En effet cette carte est là pour permettre d'avoir les informations
        sur cette pièce mais elle ne doit pas être distribuée
              
"""
from carte import *
from mystere import *
from random import *

#-----------------------------------------
# contructeur
#-----------------------------------------
def JeuCarte():
    """
    retourne un jeu de cartes vide
    """
    return []

def addCarte(jeucarte,carte):
    """
    ajoute une carte au jeu de carte
    jeuCarte : un jeu de carte 
    carte : une carte telle que définie dans carte.py
    """
    jeucarte.append(carte)
    

def enleverCarte(jeucarte,carte):
    """
    enlève une carte au jeu de carte
    jeuCarte : un jeu de carte 
    carte : une carte telle que définie dans carte.py
    """
    jeucarte.remove(carte)


def melangerJeu(jeuCarte):
    """
    mélange de manière aléatoire un jeu de carte
    jeuCarte : un jeu de carte
    """
    random.shuffle(listeCartes(jeuCarte))

    
def listeCartes(jeuCarte):
    """
    retourne le jeu de cartes sous la forme d'une liste de cartes
    jeuCarte : un jeu de carte
    résultat: la liste des cartes du jeu
    """
    return jeuCarte

def definirMystere(jeucarte):
    """
    retourne un mystère constitué de cartes du jeu
    ces cartes sont enlevées du jeu
    jeuCarte : un jeu de carte considéré comme mélangé
    """
    numProf, numSalle, numMat = 0,0,0
    for carte in jeucarte:
        if getCategorie(carte) == 1 and numProf == 0:
            numProf = getNum(carte)
            carteProf = carte
        elif getCategorie(carte) == 2 and numSalle == 0:
            numSalle = getNum(carte)
            carteSalle = carte
        elif getCategorie(carte) == 3 and numMat == 0:
            numMat = getNum(carte)
            carteMat = carte
    enleverCarte(jeucarte, carteProf)
    enleverCarte(jeucarte, carteSalle)
    enleverCarte(jeucarte, carteMat)
    return Mystere(numProf, numMat, numSalle)
    
def estDans(jeucarte,carte):
    """
    indique si une carte fait partie d'un jeu de carte
    jeuCarte : un jeu de carte
    carte : une carte telle que définie dans carte.py
    """
    return (carte in jeucarte)

def cartesDistribuables(jeucarte):
    """
    retourne un jeu carte copie de celui passé en paramètre 
    mais ne contenant pas la carte de la pièce qui permet au
    joueur de donner leur réponse à l'énigme
    jeuCarte : un jeu de carte
    """
    jeu = jeuCarte()
    for cartes in jeucarte:
        if carte.estDistribuable(cartes) == True :
            addCarte(jeu, cartes)
    return jeu

def getCartePieceHypothese(jeuCarte):
    """
    retourne la carte salle qui sert au joueur à faire leur hypothèse (c'est la seule carte non distribuable du jeu)
    jeuCarte : un jeu de carte
    """
    for cartes in jeuCarte:
        if not carte.estDistribuable(cartes):
            return cartes

def getCarteParNum(jeuCarte,cat,numCarte):
    """
    recherche une carte dans le jeu à partir des numéros de
    catégorie et de carte
    jeuCarte : un jeu de carte
    cat      : le numéro de la catégorie (PROFESSEUR, MATIERE, SALLE)
    numCarte : le numéro de la carte 
    """
    for carte in jeuCarte:
        if getCategorie(carte) == cat and getNum(carte) == numCarte:
            return carte

def getNomCarteParNum(jeuCarte,cat,numCarte):
    """
    recherche le nom d'une carte dans le jeu à partir des numéros de
    catégorie et de carte
    jeuCarte : un jeu de carte
    cat      : le numéro de la catégorie (PROFESSEUR, MATIERE, SALLE)
    numCarte : le numéro de la carte 
    """
    for carte in jeuCarte:
        if getCategorie(carte) == cat and getNum(carte) == numCarte:
            return getNom(carte)

def getListeNumCarteCategorie(jeuCarte,cat):
    """
    retourne la liste des numéros de carte du jeu qui sont dans
    catégorie passée en paramètre
    jeuCarte : un jeu de carte
    cat      : le numéro de la catégorie (PROFESSEUR, MATIERE, SALLE)
    """
    listeNum = []
    for carte in jeuCarte:
        if getCategorie(carte) == cat:
            listeNum.append(getNum(carte))
    return listeNum
# -----------------------------------------
#  Fonctions servant à l'affichage
# -----------------------------------------

def string(jeuCarte):
    """
    retourne une chaine de caractères représentant un jeu de cartes
    jeuCarte : un jeu de carte
    """
    return ",".join(jeuCarte)

def stringCat(jeuCarte,categorie):
    """
    retourne une chaine de caractères donnant les numéros et noms des cartes
    d'une catégorie par exemple pour les professeurs on souhaite obtenir une chaine
    qui s'affiche comme ci-dessous:
    1. Edgar Codd
    2. John von Neuman
    3. Allan Turing
    4. JCR Licklider
    5. Ada Lovelace
    6. Grace Hopper
    paramètres:
    jeuCarte : un jeu de carte
    categorie : le numéro de la catégorie
    """ 

    res = ""
    for carte in jeuCarte:
        if getCategorie(carte) == categorie:
            res += (" " + str(getNum(carte)) + ". "+ getNom(carte) + "\n")
    return res

# -----------------------------------------
#  Fonction permettant de lire un jeu de cartes dans un fichier
# -----------------------------------------


def lireJeuCarte(nomFic):
    """
    retourne une liste de cartes en lisant un fichier texte
    chaque ligne du fichier contient les informations suivantes:
            num carte;nom carte;description carte;nom fic image
            Les catégories de cartes sont séparée par une ligne vide
    nomFic le nom du fichier où se trouve la description des cartes
    """
    texte=""
    try:
        fic=open(nomFic)
        texte=fic.read()
        fic.close()
    except:
        print("probleme de lecture du fichier")
        return []
    lignes=texte.split("\n")
    i=1
    res=JeuCarte()
    for ligne in lignes:
        erreur=False
        elements=ligne.split(";")
        if len(elements)!=5:
            print("ligne",i,"ignorée car nombre d'éléments incorrects")
        else:
            try:
                num=int(elements[0])
                nom=elements[1]
                nomcat=elements[2]
                info=elements[3]
                if carte.estNomCategorie(nomcat):
                    cat=carte.categorieFromNom(nomcat)
                else:
                    print("ligne",i,"ignorée car le nom du type de la carte n'est pas correcte")
                    erreur=True
                if not erreur:
                    if nom.endswith('!'):
                        addCarte(res,carte.Carte(num,nom,cat,info,False))
                    else:
                        addCarte(res,carte.Carte(num,nom,cat,info,True))
            except:
                print("ligne",i,"ignorée car le numéro n'a pas le bon format")
                
        i=i+1
    return res
