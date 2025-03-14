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
    def __init__(self,_numProf,_numMat,_numSalle):
        self._numProf=_numProf
        self._numMat=_numMat
        self._numSalle=_numSalle

    #------------------
    # getters
    #------------------

    def getProfesseur(self):
        """
        retourne le numéro du professeur du mystère
        mystere: un mystere
        """
        return self._numProf


    def getMatiere(self):
        """
        retourne le numéro de la matières du mystère
        mystere: un mystere
        """
        return self._numMat


    def getSalle(self):
        """
        retourne le numéro de la salle du mystère
        mystere: un mystere
        """
        return self._numSalle