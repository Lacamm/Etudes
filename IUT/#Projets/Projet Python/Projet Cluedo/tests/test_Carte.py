#!/usr/bin/python3
import unittest

import carte

class TestCase(unittest.TestCase):
    def setUp(self):
        self.c1=carte.Carte(1,"carte1",carte.PROFESSEUR,"info1",True)
        self.c2=carte.Carte(4,"carte2",carte.SALLE,"info2",False)
        self.c3=carte.Carte(6,"carte3",carte.MATIERE,"info3",True)
        
    def test_getNum(self):
        self.assertEqual(carte.getNum(self.c1),1,"Problème avec l'appel à getNum("+str(self.c1)+")")
        self.assertEqual(carte.getNum(self.c2),4,"Problème avec l'appel à getNum("+str(self.c2)+")")
        self.assertEqual(carte.getNum(self.c3),6,"Problème avec l'appel à getNum("+str(self.c3)+")")
    
    def test_getNom(self):
        self.assertEqual(carte.getNom(self.c1),"carte1","Problème avec l'appel à getNom("+str(self.c1)+")")
        self.assertEqual(carte.getNom(self.c2),"carte2","Problème avec l'appel à getNom("+str(self.c2)+")")
        self.assertEqual(carte.getNom(self.c3),"carte3","Problème avec l'appel à getNom("+str(self.c3)+")")
    
    def test_getCategorie(self):
        self.assertEqual(carte.getCategorie(self.c1),carte.PROFESSEUR,"Problème avec l'appel à getCategorie("+str(self.c1)+")")
        self.assertEqual(carte.getCategorie(self.c2),carte.SALLE,"Problème avec l'appel à getCategorie("+str(self.c2)+")")
        self.assertEqual(carte.getCategorie(self.c3),carte.MATIERE,"Problème avec l'appel à getCategorie("+str(self.c3)+")")
    
    def test_getNomCategorie(self): 
        self.assertEqual(carte.getNomCategorie(self.c1),carte.nomCategorie[carte.PROFESSEUR],"Problème avec l'appel à getNomCategorie("+str(self.c1)+")")
        self.assertEqual(carte.getNomCategorie(self.c2),carte.nomCategorie[carte.SALLE],"Problème avec l'appel à getNomCategorie("+str(self.c2)+")")
        self.assertEqual(carte.getNomCategorie(self.c3),carte.nomCategorie[carte.MATIERE],"Problème avec l'appel à getNomCategorie("+str(self.c3)+")")
        

    def test_getDescription(self):
        self.assertEqual(carte.getDescription(self.c1),"info1","Problème avec l'appel à getDescription("+str(self.c1)+")")
        self.assertEqual(carte.getDescription(self.c2),"info2","Problème avec l'appel à getDescription("+str(self.c2)+")")
        self.assertEqual(carte.getDescription(self.c3),"info3","Problème avec l'appel à getDescription("+str(self.c3)+")")
    
    def test_estDistribuable(self):
        self.assertTrue(carte.estDistribuable(self.c1),"Problème avec l'appel à estDistribuable("+str(self.c1)+")")
        self.assertFalse(carte.estDistribuable(self.c2),"Problème avec l'appel à estDistribuable("+str(self.c2)+")")
        self.assertTrue(carte.estDistribuable(self.c3),"Problème avec l'appel à estDistribuable("+str(self.c3)+")")
        
    def test_categorieFromNom(self):
        self.assertEqual(carte.categorieFromNom(carte.nomCategorie[carte.MATIERE]),carte.MATIERE,"Problème avec l'appel à categorieFromNom('"+carte.nomCategorie[carte.MATIERE]+"')")
        self.assertEqual(carte.categorieFromNom(carte.nomCategorie[carte.PROFESSEUR]),carte.PROFESSEUR,"Problème avec l'appel à categorieFromNom('"+carte.nomCategorie[carte.PROFESSEUR]+"')")
        self.assertEqual(carte.categorieFromNom(carte.nomCategorie[carte.SALLE]),carte.SALLE,"Problème avec l'appel à categorieFromNom('"+carte.nomCategorie[carte.SALLE]+"')")
    
    def test_categorieFromNum(self):
        self.assertEqual(carte.categorieFromNum(carte.MATIERE),carte.nomCategorie[carte.MATIERE],"Problème avec l'appel à categorieFromNum('"+str(carte.MATIERE)+"')")
        self.assertEqual(carte.categorieFromNum(carte.PROFESSEUR),carte.nomCategorie[carte.PROFESSEUR],"Problème avec l'appel à categorieFromNum('"+str(carte.PROFESSEUR)+"')")
        self.assertEqual(carte.categorieFromNum(carte.SALLE),carte.nomCategorie[carte.SALLE],"Problème avec l'appel à categorieFromNum('"+str(carte.SALLE)+"')")
    
    def test_estNomCategorie(self):
        self.assertTrue(carte.estNomCategorie(carte.nomCategorie[carte.MATIERE]),"Problème avec l'appel à estNomCategorie('"+str(carte.nomCategorie[carte.MATIERE])+"')")
        self.assertTrue(carte.estNomCategorie(carte.nomCategorie[carte.PROFESSEUR]),"Problème avec l'appel à estNomCategorie('"+str(carte.nomCategorie[carte.PROFESSEUR])+"')")
        self.assertTrue(carte.estNomCategorie(carte.nomCategorie[carte.SALLE]),"Problème avec l'appel à estNomCategorie('"+str(carte.nomCategorie[carte.SALLE])+"')")
        self.assertFalse(carte.estNomCategorie('zzzz'),"Problème avec l'appel à estNomCategorie('zzzz')")
        self.assertFalse(carte.estNomCategorie('lksdqjlkcjmq'),"Problème avec l'appel à estNomCategorie('lksdqjlkcjmq')")
        
if __name__ == '__main__':
    unittest.main()
