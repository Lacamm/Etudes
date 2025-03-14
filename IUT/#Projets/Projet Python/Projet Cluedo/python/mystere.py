# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module mystere.py
   ~~~~~~~~~~~~~~~
   
   Ce module gère un mystère c'est à dire les trois cartes à deviner.
"""
import carte

#------------------
# constructeur
#------------------
def Mystere(_numProf,_numMat,_numSalle):
    """
    retourne un nouveau mystère défini par les trois numéros de cartes passés paramètres
    _numProf  : numero du professeur
    _numMat   : numéro de la matière
    _numSalle : numéro de la salle
    """
    return (_numProf,_numMat,_numSalle)

#------------------
# getters
#------------------

def getProfesseur(mystere):
    """
    retourne le numéro du professeur du mystère
    mystere: un mystere
    """
    return mystere[0]


def getMatiere(mystere):
    """
    retourne le numéro de la matières du mystère
    mystere: un mystere
    """
    return mystere[1]


def getSalle(mystere):
    """
    retourne le numéro de la salle du mystère
    mystere: un mystere
    """
    return mystere[2]
