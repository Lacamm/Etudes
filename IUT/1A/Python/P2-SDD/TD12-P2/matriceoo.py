#!/usr/bin/python3

#-----------------------------------------
# Une implémentation en orienté objet des matrices 2D en python
#-----------------------------------------
class Matrice(object):

    def __init__(self,nbLignes,nbColonnes,valeurParDefaut=0):
        """
        constructeur
        """
        self._nbLignes=nbLignes
        self._nbColonnes=nbColonnes
        self._listeDesValeurs=[valeurParDefaut]*(nbLignes*nbColonnes)

    def getNbLignes(self):
        return self._nbLignes

    def getNbColonnes(self):
        return self._nbColonnes

    def getVal(self,lig,col):
        return self._listeDesValeurs[lig*self._nbColonnes+col]

    def setVal(self,lig,col,val):
        self._listeDesValeurs[lig*self._nbColonnes+col]=val

    def afficheLigneSeparatrice(self,tailleCellule=4):
        print()
        for i in range(self.getNbColonnes()+1):
            print('-'*tailleCellule+'+',end='')
        print()
   
    def affiche(self,tailleCellule=4):
        nbColonnes=self.getNbColonnes()
        nbLignes=self.getNbLignes()
        print(' '*tailleCellule+'|',end='')
        for i in range(nbColonnes):
            print(str(i).center(tailleCellule)+'|',end='')
        self.afficheLigneSeparatrice(tailleCellule)
        for i in range(nbLignes):
            print(str(i).rjust(tailleCellule)+'|',end='')
            for j in range(nbColonnes):
                print(str(self.getVal(i,j)).rjust(tailleCellule)+'|',end='')
            self.afficheLigneSeparatrice(tailleCellule)
        print()

#fonctions à transformer en méthodes
# ATTENTION CES FONCTIONS SONT ECRITES AVEC L'API NON OBJET

    def estSymetrique(self):
        ok=True
        i=0
        while i < self.getNbLignes() and ok:
            j=i+1
            while j<self.getNbColonnes() and ok:
                ok=self.getVal(i,j)==self.getVal(j,i)
                j+=1
            i+=1
        return ok


# fait l'addition de m1 avec m2

    def addition(self,m2):
        if self.getNbColonnes()!=m2.getNbColonnes() or self.getNbLignes()!=m2.getNbLignes():
            return None
        m3=Matrice(self.getNbLignes(), self.getNbColonnes(),0)
        for i in range(self.getNbLignes()):
            for j in range(self.getNbColonnes()):
                m3.setVal(i,j)+self.getVal(i,j)+m2.getVal(i,j)
        return m3

            

#### programme de test
if __name__=='__main__':
    m=Matrice(5,4,0)
    k=0
    for i in range(m.getNbLignes()):
        for j in range(m.getNbColonnes()):
            m.setVal(i,j,k)
            k+=1
    m.affiche()

assert not m.estSymetrique()

#print(m.addition(m2))