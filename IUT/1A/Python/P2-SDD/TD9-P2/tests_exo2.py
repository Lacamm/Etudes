#!/usr/bin/python3
import unittest
import os

from matrice import *

class TestMatrices(unittest.TestCase):
    def setUp(self):
        self.m21=[[0,1,2,3],
                 [4,5,6,7],
                 [8,9,10,11]]
        self.m22=[['a','b','c','d','e'],
                 ['f','g','h','i','j']]
        self.m23=[[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]]
        self.m24=[[1,2,3],
                 [2,4,5],
                 [3,5,6]]
        self.m25=[[6,5,4],
                 [5,3,2],
                 [4,2,1]]
        self.m26=[[7,7,7],
                  [7,7,7],
                  [7,7,7]]
        self.m27=[[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]
        self.m28=[[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]]
        
    def test_Matrice(self):
        self.assertEqual(Matrice(3,4),[[0,0,0,0],[0,0,0,0],[0,0,0,0]],"Pb avec l'appel Matrice(3,4)")
        self.assertEqual(Matrice(5,2,'a'),[['a','a'],['a','a'],['a','a'],['a','a'],['a','a']],"Pb avec l'appel Matrice(5,2,'a')")
        
    def test_getNbLignes(self):
        self.assertEqual(getNbLignes(self.m21),3,"Pb avec l'appel getNbLignes("+str(self.m21)+")")
        self.assertEqual(getNbLignes(self.m22),2,"Pb avec l'appel getNbLignes("+str(self.m22)+")")
    
    def test_getNbColonnes(self):
        self.assertEqual(getNbColonnes(self.m21),4,"Pb avec l'appel getNbColonnes("+str(self.m21)+")")
        self.assertEqual(getNbColonnes(self.m22),5,"Pb avec l'appel getNbColonnes("+str(self.m22)+")")
    
    def test_getVal(self):
        self.assertEqual(getVal(self.m21,1,3),7,"Pb avec l'appel getVal("+str(self.m21)+"1,3)")
        self.assertEqual(getVal(self.m22,1,3),'i',"Pb avec l'appel getVal("+str(self.m22)+"1,3)")

    def test_setVal(self):
        setVal(self.m21,2,0,100)
        self.assertEqual(self.m21,[[0,1,2,3],[4,5,6,7],[100,9,10,11]],"Pb avec l'appel setVal("+str(self.m21)+"2,0,100)")
        setVal(self.m22,0,4,'z')
        self.assertEqual(self.m22,[['a','b','c','d','z'],['f','g','h','i','j']],"Pb avec l'appel setVal("+str(self.m22)+"0,4,'z')")
        
    def test_isNulle(self):
        self.assertFalse(isNulle(self.m21),"Pb avec l'appel isNulle("+str(self.m21)+")")
        self.assertFalse(isNulle(self.m22),"Pb avec l'appel isNulle("+str(self.m22)+")")
        self.assertTrue(isNulle(self.m23),"Pb avec l'appel isNulle("+str(self.m23)+")")
        
    def test_isCarre(self):
        self.assertFalse(isCarre(self.m21),"Pb avec l'appel isCarre("+str(self.m21)+")")
        self.assertFalse(isCarre(self.m22),"Pb avec l'appel isCarre("+str(self.m22)+")")
        self.assertTrue(isCarre(self.m23),"Pb avec l'appel isCarre("+str(self.m23)+")")
        self.assertTrue(isCarre(self.m24),"Pb avec l'appel isCarre("+str(self.m24)+")")
        
    def test_moyenne(self):
        self.assertEqual(moyenne(self.m21),66/12,"Pb avec l'appel moyenne("+str(self.m21)+")")
        self.assertEqual(moyenne(self.m23),0.,"Pb avec l'appel moyenne("+str(self.m23)+")")
        self.assertEqual(moyenne(self.m24),31/9,"Pb avec l'appel moyenne("+str(self.m24)+")")

    def test_additionMat(self):
        self.assertEqual(additionMat(self.m21,self.m27),self.m28,"Problème avec l'addition")
        self.assertEqual(additionMat(self.m24,self.m25),self.m26,"Problème avec l'addition")

        
if __name__ == '__main__':
    unittest.main()




        
if __name__ == '__main__':
    unittest.main()
