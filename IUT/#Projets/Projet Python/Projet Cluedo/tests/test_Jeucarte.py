#!/usr/bin/python3
import unittest

import carte
import mystere
import jeucarte

class TestCase(unittest.TestCase):
    def setUp(self):
        self.cartes=[
            carte.Carte(1,"carte1",carte.PROFESSEUR,"info1",True),
            carte.Carte(1,"carte2",carte.SALLE,"info2",True),
            carte.Carte(1,"carte3",carte.MATIERE,"info3",True),
            carte.Carte(2,"carte4",carte.PROFESSEUR,"info4",True),
            carte.Carte(2,"carte5",carte.SALLE,"info5",False),
            carte.Carte(2,"carte6",carte.MATIERE,"info6",True),
            carte.Carte(3,"carte7",carte.PROFESSEUR,"info7",True),
            carte.Carte(3,"carte8",carte.SALLE,"info8",True),
            carte.Carte(3,"carte9",carte.MATIERE,"info9",True)
        ]
        self.distribuables=[
            carte.Carte(1,"carte1",carte.PROFESSEUR,"info1",True),
            carte.Carte(1,"carte2",carte.SALLE,"info2",True),
            carte.Carte(1,"carte3",carte.MATIERE,"info3",True),
            carte.Carte(2,"carte4",carte.PROFESSEUR,"info4",True),
            carte.Carte(2,"carte6",carte.MATIERE,"info6",True),
            carte.Carte(3,"carte7",carte.PROFESSEUR,"info7",True),
            carte.Carte(3,"carte8",carte.SALLE,"info8",True),
            carte.Carte(3,"carte9",carte.MATIERE,"info9",True)            
            ]
        self.jeu=jeucarte.JeuCarte()
        for c in self.cartes:
            jeucarte.addCarte(self.jeu,c)
    
    def appartient(self,listeCarte,numCat,numCarte):
        for c in listeCarte:
            if carte.getNum(c)==numCarte and carte.getCategorie(c)==numCarte:
                return True
        return False
    
    def test_stringCat(self):
        self.assertEqual(jeucarte.stringCat(self.jeu,carte.PROFESSEUR)," 1. carte1\n 2. carte4\n 3. carte7\n",\
                         "Problème avec l'appel à stringCat("+str(self.jeu)+","+str(carte.PROFESSEUR)+")")
        self.assertEqual(jeucarte.stringCat(self.jeu,carte.SALLE)," 1. carte2\n 2. carte5\n 3. carte8\n",\
                         "Problème avec l'appel à stringCat("+str(self.jeu)+","+str(carte.SALLE)+")")
        self.assertEqual(jeucarte.stringCat(self.jeu,carte.MATIERE)," 1. carte3\n 2. carte6\n 3. carte9\n",\
                         "Problème avec l'appel à stringCat("+str(self.jeu)+","+str(carte.MATIERE)+")")
        
    def test_listeCartes(self):
        self.assertEqual(jeucarte.listeCartes(self.jeu),self.cartes,"Problème avec l'appel à listeCartes("+str(self.jeu)+")")
    
    def test_definirMystere(self):
        jeu=jeucarte.JeuCarte()
        for c in self.cartes:
            jeucarte.addCarte(jeu,c)
        myst=jeucarte.definirMystere(jeu)
        prof=mystere.getProfesseur(myst)
        mat=mystere.getMatiere(myst)
        salle=mystere.getSalle(myst)
        ok1= prof in [1,2,3] and  mat in [1,2,3] and salle in [1,2,3]
        listeCartes=jeucarte.listeCartes(jeu)
        ok2 = not (self.appartient(listeCartes,carte.PROFESSEUR,prof) or\
                         self.appartient(listeCartes,carte.MATIERE,mat) or \
                         self.appartient(listeCartes,carte.SALLE,salle))
        self.assertTrue(ok1,"Problème avec l'appel à definirMystere("+str(self.jeu)+") qui semble choisir des cartes inexistantes" +str(mystere))
        self.assertTrue(ok2,"Problème avec l'appel à definirMystere("+str(self.jeu)+") qui n'enlève pas les cartes choisies du jeu"\
                   +str(mystere)+" jeu de cartes après l'appel "+str(jeu))
          
        
    def test_estDans(self):
        self.assertTrue(jeucarte.estDans(self.jeu,self.cartes[3]),"Problème avec l'appel à estDans("+str(self.jeu)+","+str(self.cartes[3])+")")
        c=carte.Carte(13,"carte13",carte.MATIERE,"info13",True)
        self.assertFalse(jeucarte.estDans(self.jeu,c),"Problème avec l'appel à estDans("+str(self.jeu)+","+str(c)+")")
    
    def test_cartesDistribuables(self):
        distribuable=jeucarte.cartesDistribuables(self.jeu)
        self.assertListEqual(self.distribuables,distribuable,"Problème avec l'appel à cartesDistribuables("+str(self.jeu)+")")

    
    def test_getCartePieceHypothese(self):
        self.assertEqual(jeucarte.getCartePieceHypothese(self.jeu),self.cartes[4],\
                         "Problème avec l'appel à getCartePieceHypothese("+str(self.jeu)+")\n"+\
                         "valeur attendue "+str(self.cartes[4]))
    
    def test_getCarteParNum(self):
        self.assertEqual(jeucarte.getCarteParNum(self.jeu,carte.PROFESSEUR,1),self.cartes[0],"Problème avec l'appel à getCarteParNum("\
                             +str(self.jeu)+","+str(carte.PROFESSEUR)+","+str(1)+")\n"+\
                             "valeur attendue "+str(self.cartes[0]))
        self.assertEqual(jeucarte.getCarteParNum(self.jeu,carte.PROFESSEUR,2),self.cartes[3],"Problème avec l'appel à getCarteParNum("\
                             +str(self.jeu)+","+str(carte.PROFESSEUR)+","+str(2)+")\n"+\
                             "valeur attendue "+str(self.cartes[3]))
        self.assertEqual(jeucarte.getCarteParNum(self.jeu,carte.MATIERE,3),self.cartes[8],"Problème avec l'appel à getCarteParNum("\
                             +str(self.jeu)+","+str(carte.MATIERE)+","+str(3)+")\n"+\
                             "valeur attendue "+str(self.cartes[8]))
    
    def test_getNomCarteParNum(self):
        self.assertEqual(jeucarte.getNomCarteParNum(self.jeu,carte.PROFESSEUR,1),"carte1","Problème avec l'appel à getCarteParNum("\
                             +str(self.jeu)+","+str(carte.PROFESSEUR)+","+str(1)+")\n"+\
                             "valeur attendue "+"carte1")
        self.assertEqual(jeucarte.getNomCarteParNum(self.jeu,carte.PROFESSEUR,2),"carte4","Problème avec l'appel à getCarteParNum("\
                             +str(self.jeu)+","+str(carte.PROFESSEUR)+","+str(2)+")\n"+\
                             "valeur attendue "+"carte4")
        self.assertEqual(jeucarte.getNomCarteParNum(self.jeu,carte.MATIERE,3),"carte9","Problème avec l'appel à getCarteParNum("\
                             +str(self.jeu)+","+str(carte.MATIERE)+","+str(3)+")\n"+\
                             "valeur attendue "+"carte9")
    
    def test_getListeNumCarteCategorie(self):
        self.assertListEqual(jeucarte.getListeNumCarteCategorie(self.jeu,carte.PROFESSEUR),[1,2,3],"Problème avec l'appel à getCarteParNum("\
                             +str(self.jeu)+","+str(carte.PROFESSEUR)+")\n")
        self.assertListEqual(jeucarte.getListeNumCarteCategorie(self.jeu,carte.MATIERE),[1,2,3],"Problème avec l'appel à getCarteParNum("\
                             +str(self.jeu)+","+str(carte.MATIERE)+")\n")
        self.assertListEqual(jeucarte.getListeNumCarteCategorie(self.jeu,carte.SALLE),[1,2,3],"Problème avec l'appel à getCarteParNum("\
                             +str(self.jeu)+","+str(carte.SALLE)+")\n")

          
if __name__ == '__main__':
    unittest.main()
