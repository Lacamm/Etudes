#!/usr/bin/env python3

class Piece:
    def __init__(self, nom, cout, duree):
        self.nom = nom;
        self.cout = cout;
        self.duree = duree;
    
    def getNom(self):
        return self.nom;
    
    def getCout(self):
        return self.cout;
    
    def getDuree(self):
        return self.duree;

class Assemblage:
    def __init__(self, etiquette, enfants):
        self.__etiquette = etiquette
        self.__enfants = enfants

    def etiquette(self):
        return self.__etiquette

    def enfants(self):
        return self.__enfants

    @classmethod
    def Feuille(cls_assemblage, etiquette): #méthode statique
        return cls_assemblage(etiquette, [])

    def add(self, nourisson):
        """
        ajoute un enfant à l'assemblage
        """
        self.__enfants.append(nourisson)
    
    def estFeuille(self):
        return self.enfants() == []

    def __repr__(self):
        repr_enfants = ",".join(("%r" % e) for e in self.enfants())
        return "%r<%s>" % (self.etiquette(), repr_enfants)


def guitare():
    assemblage = Assemblage(Piece("guitare",100,1),[])
    assemblage.add(Piece("cordes",10,0))
    corps = Assemblage(Piece("corps",50,1),[])
    corps.add(Piece("caisse",100,5))
    corps.add(Piece("manche",50,3))
    assemblage.add(corps)
    print(guitare)
    return assemblage

def prix(assemblage):
    res = assemblage.etiquette().getCout();
    for n in assemblage.enfants():
        if n.estFeuille():
            res += n.etiquette.getCout()
        else:
            res += n.etiquette.getCout()
            prix(n)
    return res

def tempsAssemblage(assemblage):
    res = assemblage.etiquette().getDuree()
    for n in assemblage.enfants():
        if n.estFeuille():
            res += n.etiquette().duree()
        else:
            res += tempsAssemblage(n)
    return res

def moinsLong(assemblage):
    res = []
    res.append(assemblage.etiquette())
    for n in assemblage.enfants():
        if n.estFeuille():
            if n.etiquette().getDuree() < res[-1].getDuree():
                del res[-1]
                res.append(n.etiquette().getDuree())
        else:
            if n.etiquette().getDuree() < res[-1].getDuree():
                del res[-1]
                res.append(n.etiquette().getDuree())
            moinsLong(n)
    return res




g = guitare()

print(prix(g))

#print(tempsAssemblage(g))

#print(moinsLong(g))