#!/usr/bin/python3

class scrore(object):
    def __init__(self,nomJ,nbPoints):
        """
        Conctructeur
        """
        self._nomJ = nomJ
        self._nbPoints = nbPoints
    
    def getNom(self):
        return self._nomJ
    
    def getPoints(self):
        return self._nbPoints

s = scrore('nadal', 11)

assert s.getNom() == 'nadal'
assert s.getPoints() == 11

