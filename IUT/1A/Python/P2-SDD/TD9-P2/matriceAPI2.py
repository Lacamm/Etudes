'''
   -----------------------------------------
   Une deuxième implémentation des matrices 2D en python
   -----------------------------------------
'''

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    '''
    Crée une matrice de nbLignes lignes et nbColonnes colonnes
    contenant toute la valeur valeurParDefaut
    paramètres: nbLignes (int)
                nbColonnes (int)
                valeurParDefaut (int)
    résultat: matrice(list of list)
    '''
    matrice = []
    ligne = []

    for n in range(nbLignes):
        for i in range(nbColonnes):
            ligne.append(valeurParDefaut)
        matrice.append(ligne)
        ligne = []
    return matrice

def getNbLignes(matrice):
    '''
    Permet de connaitre le nombre de lignes d'une matrice
    paramètre: matrice(list of list)
    resultat: nbLignes (int)
    '''
    return len(matrice)

def getNbColonnes(matrice):
    '''
    Permet de connaitre le nombre de colonnes d'une matrice
    paramètre: matrice(list of list)
    resultat: nbColonnes (int)
    '''
    return len(matrice[0])

def getVal(matrice,lig,col):
    '''
    retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
    paramètres: matrice(list of list)
                lig (int)
                col (int)
    resultat: val (int)   
    '''
    val = matrice[lig][col]
    return val

def setVal(matrice,lig,col,val):
    '''
    place la valeur val à la ligne lig colonne col de la matrice
    paramètres: matrice(list of list)
                lig (int)
                col (int)
    resultat: cette fonction ne retourne rien mais modifie la matrice
    '''
    matrice[lig][col] = val
