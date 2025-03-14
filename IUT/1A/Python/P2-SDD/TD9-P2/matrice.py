#!/usr/buin/python3

from matriceAPI2 import *

# Affichage d'une matrice
def afficheLigneSeparatrice(matrice,tailleCellule=4):
    ''' 
    fonction annexe pour afficher les lignes séparatrices
    paramètres: matrice la matrice à afficher
                tailleCellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''
    print()
    for i in range(getNbColonnes(matrice)+1):
        print('-'*tailleCellule+'+',end='')
    print()

def afficheMatrice(matrice,tailleCellule=4):
    '''
    affiche le contenue d'une matrice présenté sous le format d'une grille
    paramètres: matrice la matrice à afficher
                tailleCellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''

    nbColonnes=getNbColonnes(matrice)
    nbLignes=getNbLignes(matrice)
    print(' '*tailleCellule+'|',end='')
    for i in range(nbColonnes):
        print(str(i).center(tailleCellule)+'|',end='')
    afficheLigneSeparatrice(matrice,tailleCellule)
    for i in range(nbLignes):
        print(str(i).rjust(tailleCellule)+'|',end='')
        for j in range(nbColonnes):
            print(str(getVal(matrice,i,j)).rjust(tailleCellule)+'|',end='')
        afficheLigneSeparatrice(matrice,tailleCellule)
    print()

#-----------------------------------------
# AJOUTER ICI LE CODE DES FONCTIONS DEMANDEES DANS L'EXERCICE 1
#-----------------------------------------

def isNulle(matrice):
    '''
    Teste si la matrice est nulle
    Paramètres: matrice
    Résulat: Nulle (bool)
    '''
    Nulle = True
    for i in range(getNbLignes(matrice)):
        for j in range(getNbColonnes(matrice)):
            if getVal(matrice,i,j) != 0:
                Nulle = False
    return Nulle

def isCarre(matrice):
    '''
    Teste si la ml (__main__.TestMatrices) ... ok
atrice est une matrice carrée
    Paramètres: matrice
    Résulat: Carre (bool)
    '''
    if getNbColonnes(matrice) == getNbLignes(matrice):
        Carre = True
    else:
        Carre = False
    return Carre

def moyenne(matrice):
    '''
    Calcule la moyenne des valeurs de la matrice
    Paramètres: matrice
    Résulat: moy (int)
    '''
    somme = 0
    sommeTotale = 0
    for i in range(getNbLignes(matrice)):
        for j in range(getNbColonnes(matrice)):
            somme += getVal(matrice,i,j)
        sommeTotale += somme
        somme = 0
    return sommeTotale / (getNbLignes(matrice)*(getNbColonnes(matrice)))

def additionMat(matrice1, matrice2):
    '''
    Calcule la somme de deux matrice en donnant une nouvelle matrice
    Paramètres: matrice1 (tuple)
                matrice2 (tuple)
    Résulat: sumMatrice (tuple)
    '''
    sumMatriceVal = []

    for i in range(getNbLignes(matrice1)):
        for j in range(getNbColonnes(matrice1)):
            sumMatriceVal.append(getVal(matrice1,i,j) + getVal(matrice2,i,j))

    sumMatrice = (getNbLignes(matrice1),getNbColonnes(matrice1),sumMatriceVal)
    return sumMatrice
