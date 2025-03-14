#!/usr/bin/python3
import unittest

import carte
import jeucarte
import joueur
import ficheIndices


class TestCase(unittest.TestCase):
    def setUp(self):
        self.cartes=[
            carte.Carte(1,"carte1",carte.PROFESSEUR,"info1",True),
            carte.Carte(1,"carte2",carte.SALLE,"info2",True),
            carte.Carte(1,"carte3",carte.MATIERE,"info3",True),
            carte.Carte(2,"carte4",carte.PROFESSEUR,"info4",True),
            carte.Carte(2,"carte5",carte.SALLE,"info5",True),
            carte.Carte(2,"carte6",carte.MATIERE,"info6",True),
            carte.Carte(3,"carte7",carte.PROFESSEUR,"info7",True),
            carte.Carte(3,"carte8",carte.SALLE,"info8",True),
            carte.Carte(3,"carte9",carte.MATIERE,"info9",True)
        ]
        self.listeJoueurs=[
            joueur.Joueur(1,'joueur1'),
            joueur.Joueur(2,'joueur2',True),
            joueur.Joueur(3,'joueur3',False),
            joueur.Joueur(4,'joueur4')
            ]
        self.jeu=jeucarte.JeuCarte()
        for c in self.cartes:
            jeucarte.addCarte(self.jeu,c)
        self.fi=ficheIndices.FicheIndices(self.listeJoueurs,self.jeu)

    def test_creerIndications(self):
        self.assertDictEqual(ficheIndices.creerIndications([1,2,3,4]),{1:ficheIndices.NESAISPAS,\
                                                                   2:ficheIndices.NESAISPAS,\
                                                                   3:ficheIndices.NESAISPAS,\
                                                                   4:ficheIndices.NESAISPAS},\
                             "Problème avec l'appel à ficheIndices.creerIndications([1,2,3,4])")
        self.assertDictEqual(ficheIndices.creerIndications([4,6]),{4:ficheIndices.NESAISPAS,\
                                                                   6:ficheIndices.NESAISPAS},\
                             "Problème avec l'appel à creerIndications([4,6])")

    def test_getJeuCartes(self):
        self.assertEqual(ficheIndices.getJeuCartes(self.fi),self.jeu,"Problème avec l'appel à getJeuCartes("\
                         +str(self.fi)+")")
        
    
    def test_getListeNumJoueurs(self):
        self.assertEqual(ficheIndices.getListeNumJoueurs(self.fi),[1,2,3,4],"Problème avec l'appel à getListeNumJoueurs("\
                         +str(self.fi)+")")
    

if __name__ == '__main__':
    unittest.main()