class Espece(object):
    def __init__(self, nom, adn):
        self._nom = nom
        self._adn = adn

    def getAdn(self):
        return self._adn
    
    def lireFichier(f):
        fichier = open(f,"r")
        contenu = fichier.read()
        fichier.close()
        return contenu
    
    def mutations(self,e1):
        res = 0
        for i in range(len(self.getAdn())):
            if self._adn[i] != e1._adn[i]:  
                res += 1
        return res

