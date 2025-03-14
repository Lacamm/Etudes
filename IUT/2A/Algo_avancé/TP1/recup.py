#!/usr/bin/env python3

class Arbre:
    def __init__(self, etiquette, enfants):
        self.__etiquette = etiquette
        self.__enfants = enfants

    def etiquette(self):
        return self.__etiquette

    def enfants(self):
        return self.__enfants

    @classmethod
    def Feuille(cls_arbre, etiquette): #méthode statique
        return cls_arbre(etiquette, [])

    def add(self, nourisson):
        """
        ajoute un enfant à l'arbre
        """
        self.__enfants.append(nourisson)

    def __repr__(self):
        repr_enfants = ",".join(("%r" % e) for e in self.enfants())
        return "%r<%s>" % (self.etiquette(), repr_enfants)

    def isLeaf(self):
        return self.enfants() == []

    def leafNumber(self):
        res = 0
        for e in self.enfants():
            res += e.leafNumber()
        if self.isLeaf():
            return 1
        return res

    def nodeNumber(self):
        res = 0
        for e in self.enfants():
            res += e.nodeNumber()
        if not self.isLeaf():
            res += 1
        return res

    def have(self,name):
        res = True
        if self.etiquette == name:
            return True
        else:
            for e in self.enfants():
                if e.have(name):
                    return True
            return False

    def height(self):
        res = 0
        high = 0
        for e in self.enfants():
            if res < e.height():
                res = e.height()
            high = 1
        return res + high

    def degree(self):
        res = 0
        high = 0
        for e in self.enfants():
            if res < e.degree():
                res = e.degree()
            high += 1
        return high

    #symboles +, * ou entiers
    def check(self):
        # listeCheck = list(self.enfants())
        for e in self.enfants():
            if type(e.etiquette()) == int:
                if not e.isLeaf():
                    return False
            elif type(e.etiquette()) == str:
                if not e.isLeaf():
                    if len(e.enfants()) != 2:
                        print("pass")
                        return False
            return True

arbre8 = Arbre.Feuille(8)
arbre7 = Arbre.Feuille(7)
arbre6 = Arbre.Feuille(6)
arbre5 = Arbre.Feuille(5)
arbre4 = Arbre.Feuille(4)

arbre3 = Arbre(3, [arbre6, arbre7, arbre8])
# arbre2 = Arbre(2, [arbre4, arbre5, arbre8])
arbre1 = Arbre(1, [ arbre3])
#---------------------------------
arbre14 = Arbre.Feuille(4)
arbre15 = Arbre.Feuille(5)

arbre17 = Arbre.Feuille(7)

arbre13 = Arbre(3, [arbre14, arbre15])
arbre16 = Arbre(6, [arbre17])
arbre12 = Arbre(2, [arbre16])
arbre11 = Arbre(1, [arbre12, arbre13])

#---------------------------------
tree7 = Arbre.Feuille(7)
tree6 = Arbre.Feuille(6)
tree5 = Arbre.Feuille(5)
tree4 = Arbre.Feuille(4)
tree8 = Arbre.Feuille(8)

tree3 = Arbre("+", [tree6, tree7, tree8])
tree2 = Arbre("+", [tree4, tree5])
tree1 = Arbre("*", [tree2, tree3])

#---------------------------------

print(arbre1)
print(arbre1.leafNumber())
print(arbre1.nodeNumber())
print(arbre8.height())
#--------------------------------
print("------------------------------")
print(arbre11)
print(arbre11.leafNumber())
print(arbre11.nodeNumber())
print(arbre11.height())
print(arbre11.degree())

#--------------------------------
print("------------------------------")
print(tree1)
print(tree1.leafNumber())
print(tree1.nodeNumber())
print(tree1.height())
print(tree1.degree())
print(tree1.check())