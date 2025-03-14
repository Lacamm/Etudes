#!/usr/bin/python3

import score

class classement(object):
    def __init__(self,nbPlacesClassement):
        """
        Constructeur
        """
        self._nbPlacesClassement = nbPlacesClassement
        self._resultat = []


    def getNbPlacesClassement(self):
        return self._nbPlacesClassement

    def getScore(self,i):
        return self._resultat[i]

    def ajouter(self,score):
        modifClassement = False
        i = 1
        while modifClassement == False or i > self.getNbPlacesClassement():
            if score.getPoints() > self.getScore(i).score.getPoints() or self.getScore(i) == None:
                self._resultat.insert(i, score)
                modifClassement = True
            i += 1
        if modifClassement ==True:
            del self.resultat[-1]

#    def affiche(self):

