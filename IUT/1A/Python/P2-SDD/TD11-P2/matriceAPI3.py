#!/usr/bin/python3

'''
   -----------------------------------------
   Une troisième implémentation des matrices 2D en python
   en utilisant des dictionnaires
   -----------------------------------------
'''

def newMatrice(nbLignes,nbColonnes,valeurParDefaut=0):
    '''
    Crée une matrice de nbLignes lignes et nbColonnes colonnes
    contenant toute la valeur valeurParDefaut
    paramètres: le nombre de lignes, le nomvbre de colonnes et la valeur par défaut
    résultat: un dictionnaire
    '''
    return {'lignes': nbLignes, 'colonnes': nbColonnes, 'valeurs': [valeurParDefaut]*(nbLignes*nbColonnes)}
    

def getNbLignes(matrice):
    '''
    Permet de connaitre le nombre de lignes d'une matrice
    paramètre: une matrice sous forme de dictionnaire
    resultat: le nombre de ligne
    '''
    return matrice['lignes']

def getNbColonnes(matrice):
    '''
    Permet de connaitre le nombre de colonnes d'une matrice
    paramètre:une matrice sous forme de dictionnaire
    resultat: le nombre de colonne
    '''
    return matrice['colonnes']

def getVal(matrice,lig,col):
    '''
    retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
    paramètres:une matrice sous forme de dictionnaire, la ligne et la colonne voulue
    resultat: la valeur sélectionnée   
    '''
    return matrice['valeurs'][lig*matrice['colonnes']+col]

def setVal(matrice,lig,col,val):
    '''
    place la valeur val à la ligne lig colonne col de la matrice
    paramètres:une matrice sous forme de dictionnaire, la ligne et la colonne voulue
    resultat: cette fonction ne retourne rien mais modifie la matrice
    '''
    matrice['valeurs'][lig*matrice['colonnes']+col] = val