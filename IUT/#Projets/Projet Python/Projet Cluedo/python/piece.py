# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module piece.py
   ~~~~~~~~~~~~~~~
   
   Ce module gère les pièces dans lesquelles peuvent se dérouler un cours. 
   Une pièce possède un numéro, une liste d'entrées, un contenu
   une liste de numeros de joueurs et éventuellement un passage secret 
"""

import entree


#-----------------------------------------
# contructeur
#-----------------------------------------
def Piece(_numPiece):
    """
    retourne une nouvelle pièce vide dont on ne connait que le numéro
    les autres informations seront remplies grâces au setters
    _numPiece : le numéro de la pièce créée 
    """
    return (_numPiece,[],[],[None,[None,None]])
############_numPiece,liste des entrées,liste des num joueurs,passage secret,(la pièce destination du passage,la position du passage sur le plateau)
#-----------------------------------------
# getters
#-----------------------------------------

def getNumPiece(piece):
    """
    retourne le numéro de la pièce
    piece : une piece
    """
    return piece[0]

def getListeEntrees(piece):
    """
    retourne la liste des entrées d'une pièce
    piece : une piece
    """
    return piece[1]

def getContenu(piece):
    """
    retourne le contenu de la pièce la liste des numéros des joueurs qui s'y trouvent
    piece : une piece
    """
    return piece[2]

def getPassage(piece):
    """
    retourne le numéro de la pièce vers laquelle on peut aller grâce au passage secret de la pièce
              None si la pièce ne possède pas de passage secret
    piece : une piece
    """
    return piece[3][0]

def getEntreesDirection(piece,direction):
    """
    retourne la liste des entrées de la pièce qui permettent
    d'y entrer dans la direction indiquée en paramètre
    piece : une piece
    direction: direction par où on essaie d'entrer
    """
    res=[]
    entrees = getListeEntrees(piece)
    for elem in entrees:
        if direction == entree.getDirection(elem):
            res.append(elem)
    return res

#-------------------------
# setters et modificateurs
#-------------------------
def setPassage(piece,pieceDestination, lig, col):
    """
    modifie le passage secret de la pièce
    piece            : une piece
    pieceDestination : le numero de la pièce que l'on accède via le passage secret
    lig              : le numéro de la ligne où se trouve le passage secret
    col              : le numéro de la colonne où se trouve le passage secret
    """
    piece[3][0] = pieceDestination
    piece[3][1][0] = lig
    piece[3][1][1] = col
    
def addEntree(piece,entree):
    """
    ajoute une entrée à la pièce
    piece  : une piece
    entree : une entree (du type décrit dans le fichier entree.py)
    """
    piece[1].append(entree)

def addJoueur(piece,numJoueur):
    """
    ajoute un joueur au contenu de la pièce
    piece  : une piece
    numJoueur : un numéro de joueur
    """
    piece[2].append(numJoueur)

def enleverJoueur(piece,numJoueur):
    """
    enlève un joueur du contenu de la pièce. Si le joueur n'existe pas peut provoquer une erreur
    piece  : une piece
    numJoueur : un numéro de joueur
    """
    piece[2].remove(numJoueur)

def estEntree(piece,lig,col):
    """
    indique si une des entrées de la pièce se trouve en lig,col
    piece  : une piece
    lig    : un numéro de ligne
    col    : un numéro de colonne
    """
    ok = False
    entrees = getListeEntrees(piece)
    for elem in entrees:
        if entree.getLigne(elem) == lig and entree.getColonne(elem) == col:
            ok = True
    return ok
    
def estPassage(piece,lig,col):
    """
    indique si le passage secret se trouve en lig,col
    la fonction retourne 0 si ce n'est pas le cas et 
    le numéro de la  pièce destination sinon
    piece  : une piece
    lig    : un numéro de ligne
    col    : un numéro de colonne
    """
    ok = 0
    if piece[3][1][0] == lig and piece[3][1][1] == col:
        ok = piece[3][0]
    return ok 
