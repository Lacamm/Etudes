#!/usr/bin/python3

'''
   -----------------------------------------
   Une implémentation des matrices 2D en python
   -----------------------------------------
'''

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    '''
    Crée une matrice de nbLignes lignes et nbColonnes colonnes
    contenant toute la valeur valeurParDefaut
    paramètres: nbLignes (int)
                nbColonnes (int)
                valeurParDefaut (int)
    résultat: matrice (tuple)
    '''

    matrice = (nbLignes,nbColonnes,[valeurParDefaut]*(nbLignes*nbColonnes))
    return matrice


def getNbLignes(matrice):
    '''
    Permet de connaitre le nombre de lignes d'une matrice
    paramètre: matrice (tuple)
    resultat: nbLignes (int)
    '''
    nbLignes = matrice[0]
    return nbLignes 



def getNbColonnes(matrice):
    '''
    Permet de connaitre le nombre de colonnes d'une matrice
    paramètre:matrice (tuple)
    resultat: nbColonnes (int) 
    '''
    nbColonnes = matrice[1]
    return nbColonnes


def getVal(matrice,lig,col):
    '''
    retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
    paramètres: matrice (tuple)
                lig (int)
                col (int)
    resultat: val(int)     
    '''
    val = matrice[2][lig*matrice[1]+col]
    return val


def setVal(matrice,lig,col,val):
    '''
    place la valeur val à la ligne lig colonne col de la matrice
    paramètres: matrice (tuple)
                lig (int)
                col (int)
                val (int)
    resultat: cette fonction ne retourne rien mais modifie la matrice
    '''
    matrice[2][lig*matrice[1]+col] = val
