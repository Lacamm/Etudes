class Espece:
    def __init__(self, nom, adn):
        self._nom = nom
        self._adn = adn
    

    def mutations(self, espece2):
        lettre = ["A","T","C","G"]
        res = 0
        for i in range(len(self._adn)):
            if espece2._adn[i] in lettre and self._adn[i] in lettre:
                if espece2._adn[i] != self._adn[i]:
                    res +=1

        return res

class EspeceHypothetique(Espece):



def lire_adn(f):
    fichier = open(f,"r")
    contenu = fichier.read()
    fichier.close()
    return contenu

if __name__ == "__main__":
    abeille = Espece("abeille", lire_adn("abeille.adn"))
    humain = Espece("humain", lire_adn("humain.adn"))
    eponge = Espece("eponge", lire_adn("eponge.adn"))
    lapin = Espece("lapin", lire_adn("lapin.adn"))
    roadrunner = Espece("roadrunner", lire_adn("roadrunner.adn"))
    trex = Espece("trex", lire_adn("trex.adn"))

    print("abeille/eponge : "+ str(abeille.mutations(eponge)))
    print("humain/eponge : "+ str(humain.mutations(roadrunner)))
    print("trex/roadrunner : "+ str(trex.mutations(roadrunner)))
    print("lapin/trex : "+ str(lapin.mutations(trex)))
    print("Abeille/roadrunner : "+ str(abeille.mutations(roadrunner)))
    print("trex/humain : "+ str(trex.mutations(humain)))




