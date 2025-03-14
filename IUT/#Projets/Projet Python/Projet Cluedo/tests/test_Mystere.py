#!/usr/bin/python3
import unittest

import mystere

class TestCase(unittest.TestCase):
    def setUp(self):
        self.m1=mystere.Mystere(3,4,3)
        self.m2=mystere.Mystere(5,1,9)


    def test_getProfesseur(self):
        self.assertEqual(mystere.getProfesseur(self.m1),3,"Problème avec l'appel à getProfesseur("+str(self.m1)+")")
        self.assertEqual(mystere.getProfesseur(self.m2),5,"Problème avec l'appel à getProfesseur("+str(self.m2)+")")
    
    def test_getMatiere(self):
        self.assertEqual(mystere.getMatiere(self.m1),4,"Problème avec l'appel à getMatiere("+str(self.m1)+")")
        self.assertEqual(mystere.getMatiere(self.m2),1,"Problème avec l'appel à getMatiere("+str(self.m2)+")")
    
    def test_getSalle(self):
        self.assertEqual(mystere.getSalle(self.m1),3,"Problème avec l'appel à getSalle("+str(self.m1)+")")
        self.assertEqual(mystere.getSalle(self.m2),9,"Problème avec l'appel à getSalle("+str(self.m2)+")")


if __name__ == '__main__':
    unittest.main()