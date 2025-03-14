#!/usr/bin/python3

import unittest

from matrice import *

class TestMatrices(unittest.TestCase):
    def setUp(self):
        self.m1=(3,4,[0,1,2,3,
                      4,5,6,7,
                      8,9,10,11])
        self.m2=(2,5,['a','b','c','d','e',
                      'f','g','h','i','j'])
        self.m3=(4,4,[0]*16)
        self.m4=(3,3,[1,2,3,
                      2,4,5,
                      3,5,6])
        self.m5=(3,3,[6,5,4,
                      5,3,2,
                      4,2,1])
        self.m6=(3,3,[7,7,7,
                      7,7,7,
                      7,7,7])
        self.m7=(3,4,[1]*12)
        self.m8=(3,4,[1,2,3,4,
                      5,6,7,8,
                      9,10,11,12])


    def test_Matrice(self):
        self.assertEqual(Matrice(3,4),(3,4,[0]*12),"Pb avec l'appel Matrice(3,4)")
        self.assertEqual(Matrice(5,2,'a'),(5,2,['a']*10),"Pb avec l'appel Matrice(5,2,'a')")

    def test_getNbLignes(self):
        self.assertEqual(getNbLignes(self.m1),3,"Pb avec l'appel getNbLignes("+str(self.m1)+")")
        self.assertEqual(getNbLignes(self.m2),2,"Pb avec l'appel getNbLignes("+str(self.m2)+")")

    def test_getNbColonnes(self):
        self.assertEqual(getNbColonnes(self.m1),4,"Pb avec l'appel getNbColonnes("+str(self.m1)+")")
        self.assertEqual(getNbColonnes(self.m2),5,"Pb avec l'appel getNbColonnes("+str(self.m2)+")")

    def test_getVal(self):
        self.assertEqual(getVal(self.m1,1,3),7,"Pb avec l'appel getVal("+str(self.m1)+"1,3)")
        self.assertEqual(getVal(self.m2,1,3),'i',"Pb avec l'appel getVal("+str(self.m2)+"1,3)")

    def test_setVal(self):
        setVal(self.m1,2,0,100)
        self.assertEqual(self.m1,(3,4,[0,1,2,3,4,5,6,7,100,9,10,11]),"Pb avec l'appel setVal("+str(self.m1)+"2,0,100)")
        setVal(self.m2,0,4,'z')
        self.assertEqual(self.m2,(2,5,['a','b','c','d','z','f','g','h','i','j']),"Pb avec l'appel setVal("+str(self.m2)+"0,4,'z')")

    def test_isNulle(self):
        self.assertFalse(isNulle(self.m1),"Pb avec l'appel isNulle("+str(self.m1)+")")
        self.assertFalse(isNulle(self.m2),"Pb avec l'appel isNulle("+str(self.m2)+")")
        self.assertTrue(isNulle(self.m3),"Pb avec l'appel isNulle("+str(self.m3)+")")

    def test_isCarre(self):
        self.assertFalse(isCarre(self.m1),"Pb avec l'appel isCarre("+str(self.m1)+")")
        self.assertFalse(isCarre(self.m2),"Pb avec l'appel isCarre("+str(self.m2)+")")
        self.assertTrue(isCarre(self.m3),"Pb avec l'appel isCarre("+str(self.m3)+")")
        self.assertTrue(isCarre(self.m4),"Pb avec l'appel isCarre("+str(self.m4)+")")

    def test_moyenne(self):
        self.assertEqual(moyenne(self.m1),66/12,"Pb avec l'appel moyenne("+str(self.m1)+")")
        self.assertEqual(moyenne(self.m3),0.,"Pb avec l'appel moyenne("+str(self.m3)+")")
        self.assertEqual(moyenne(self.m4),31/9,"Pb avec l'appel moyenne("+str(self.m4)+")")
        
    def test_additionMat(self):
        self.assertEqual(additionMat(self.m1,self.m7),self.m8,"Problème avec l'addition")
        self.assertEqual(additionMat(self.m4,self.m5),self.m6,"Problème avec l'addition")
        

if __name__ == '__main__':
    unittest.main()
