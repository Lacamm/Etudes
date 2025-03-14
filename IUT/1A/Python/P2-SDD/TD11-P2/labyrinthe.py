#!/usr/bin/python3

from matriceAPI3 import *

#-----------------------------------------
# entrées sorties sur les matrices
#-----------------------------------------
def sauveMatrice(matrice,nomFic):
    '''
    '''
    fic=open(nomFic,'w')
    ligne=str(getNbLignes(matrice))+','+str(getNbColonnes(matrice))+'\n'
    fic.write(ligne)
    for i in range(getNbLignes(matrice)):
        ligne=''
        for j in range(getNbColonnes(matrice)-1):
            val=getVal(matrice,i,j)
            if val==None:
                ligne+=','
            else:
                ligne+=str(val)+','
                val=getVal(matrice,i,j+1)
            if val==None:
                ligne+='\n'
            else:
                ligne+=str(val)+'\n'
    fic.write(ligne)
    fic.close()

def chargeMatrice(nomFic,typeVal='int'):
    '''
    '''
    fic=open(nomFic,'r')
    ligneLinCol=fic.readline()
    listeLinCol=ligneLinCol.split(',')
    matrice=newMatrice(int(listeLinCol[0]),int(listeLinCol[1]))
    i=0  
    for ligne in fic:
        listeVal=ligne.split(",")
        j=0
        for elem in listeVal:
            if elem=="" or elem=="\n":
                setVal(matrice,i,j,None)
            elif typeVal=='int':
                setVal(matrice,i,j,int(elem))
            elif typeVal=='float':
                setVal(matrice,i,j,float(elem))
            elif typeVal=='bool':
                setVal(matrice,i,j,bool(elem))
            else:
                setVal(matrice,i,j,elem)
            j+=1
        i+=1
    return matrice

def afficheLigneSeparatrice(matrice,tailleCellule=4):
    '''
    Affichage d'une matrice
    fonction annexe pour afficher les lignes séparatrices
    '''
    print()
    for i in range(getNbColonnes(newMatrice)+1):
        print('-'*tailleCellule+'+',end='')
    print()
   
def afficheMatrice(matrice,tailleCellule=4):
    '''
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
   
#--------------------------------
# fonctions sur les labyrinthes
#--------------------------------

def marquageDirect(calque,mat,val,marque):
    '''
    marque avec la valeur marque les éléments du calque tel que la valeur 
    correspondante n'est pas un mur (de valeur differente de 1) et 
    qu'un de ses voisins dans le calque à pour valeur val
    la fonction doit retourner True si au moins une case du calque a été marquée
    '''
    modification = False
    for COL in range(calque['colonnes']):
        for LIG in range(calque['lignes']):
            modif = False

            if getVal(calque,LIG,COL) != marque and getVal(mat,LIG,COL) != 1:

                if (LIG-1)-COL >= 0:
                    if getVal(calque,LIG-1,COL) == val:
                        modif = True
                        setVal(calque,LIG,COL,marque)

                if (LIG+1) < getNbLignes(mat):
                    if getVal(calque,LIG+1,COL) == val:
                        modif = True
                        setVal(calque,LIG,COL,marque)

                if LIG-(COL-1) >= 0:
                    if getVal(calque,LIG,COL-1) == val:
                        modif = True
                        setVal(calque,LIG,COL,marque)

                if (COL+1) < getNbColonnes(mat):
                    if getVal(calque,LIG,COL+1) == val:
                        modif = True
                        setVal(calque,LIG,COL,marque)


            if modif == True:
                modification = True
    return modification

def estAccessible(mat,pos1,pos2):
    '''
    verifie qu'il existe un chemin entre pos1 et pos2 dans la matrice mat
    '''
    pass

def labyrintheValide(mat):
    '''
    verifie qu'il existe un chemin entre la case en haut à gauche et la case
    en bas à droite de la matrice
    '''
    pass

def estAccessible2(mat,pos1,pos2):
    '''
    vérifie l'accessibilité entre deux positions mais en calculant ne nombre de cases
    depuis le point de départ
    la fonction retourne le calque ces les deux cases sont accessibles et None sinon
    '''
    pass

def cheminDecroissant(calque,pos1,pos2):
    '''
    recherche un chemin décroissant à partir de pos1 vers pos2
    le chemin est une liste de positions
    la fonction suppose que le calque contient effectivement les valeurs permettant
    de retrouver ce chemin
    '''
    pass

def plusCourtChemin(matrice,pos1,pos2):
    '''
    recherche le plus court chemin entre pos1 et pos2. 
    s'il n'y pas de chemin entre ces deux positions la fonction retourne None
    sinon elle retourne le chemin
    '''
    pass

