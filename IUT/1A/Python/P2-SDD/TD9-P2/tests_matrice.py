#!/usr/bin/python3
import unittest
import os

def changerImport(mod,ancien,nouveau,nouveauMod):
    try:
        fic=open(mod+".py")
        cont=fic.read()
        fic.close()
        cont=cont.replace(ancien,nouveau)
        fic=open(nouveauMod+".py","w")
        fic.write(cont) 
        fic.close()
    except:
        pass

changerImport("matrice","matriceAPI2","matriceAPI1","matrice1")
changerImport("matrice1","matriceAPI1","matriceAPI2","matrice2")

import matrice1
import matrice2

class TestMatrices(unittest.TestCase):
    def setUp(self):
        self.m11=(3,4,[0,1,2,3,
                      4,5,6,7,
                      8,9,10,11])
        self.m12=(2,5,['a','b','c','d','e',
                      'f','g','h','i','j'])
        self.m13=(4,4,[0]*16)
        self.m14=(3,3,[1,2,3,
                      2,4,5,
                      3,5,6])
        self.m15=(3,3,[6,5,4,
                       5,3,2,
                       4,2,1])

        self.m16=(3,3,[7,7,7,
                       7,7,7,
                       7,7,7])
        self.m17=(3,4,[1]*12)
        self.m18=(3,4,[1,2,3,4,
                       5,6,7,8,
                       9,10,11,12])
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
                  
                  

    def test_Matrice1(self):
        self.assertEqual(matrice1.Matrice(3,4),(3,4,[0]*12),"Pb avec l'appel Matrice(3,4)")
        self.assertEqual(matrice1.Matrice(5,2,'a'),(5,2,['a']*10),"Pb avec l'appel Matrice(5,2,'a')")

    def test_getNbLignes1(self):
        self.assertEqual(matrice1.getNbLignes(self.m11),3,"Pb avec l'appel getNbLignes("+str(self.m11)+")")
        self.assertEqual(matrice1.getNbLignes(self.m12),2,"Pb avec l'appel getNbLignes("+str(self.m12)+")")

    def test_getNbColonnes1(self):
        self.assertEqual(matrice1.getNbColonnes(self.m11),4,"Pb avec l'appel getNbColonnes("+str(self.m11)+")")
        self.assertEqual(matrice1.getNbColonnes(self.m12),5,"Pb avec l'appel getNbColonnes("+str(self.m12)+")")

    def test_getVal1(self):
        self.assertEqual(matrice1.getVal(self.m11,1,3),7,"Pb avec l'appel getVal("+str(self.m11)+"1,3)")
        self.assertEqual(matrice1.getVal(self.m12,1,3),'i',"Pb avec l'appel getVal("+str(self.m12)+"1,3)")

    def test_setVal1(self):
        matrice1.setVal(self.m11,2,0,100)
        self.assertEqual(self.m11,(3,4,[0,1,2,3,4,5,6,7,100,9,10,11]),"Pb avec l'appel setVal("+str(self.m11)+"2,0,100)")
        matrice1.setVal(self.m12,0,4,'z')
        self.assertEqual(self.m12,(2,5,['a','b','c','d','z','f','g','h','i','j']),"Pb avec l'appel setVal("+str(self.m12)+"0,4,'z')")

    def test_isNulle1(self):
        self.assertFalse(matrice1.isNulle(self.m11),"Pb avec l'appel isNulle("+str(self.m11)+")")
        self.assertFalse(matrice1.isNulle(self.m12),"Pb avec l'appel isNulle("+str(self.m12)+")")
        self.assertTrue(matrice1.isNulle(self.m13),"Pb avec l'appel isNulle("+str(self.m13)+")")

    def test_isCarre1(self):
        self.assertFalse(matrice1.isCarre(self.m11),"Pb avec l'appel isCarre("+str(self.m11)+")")
        self.assertFalse(matrice1.isCarre(self.m12),"Pb avec l'appel isCarre("+str(self.m12)+")")
        self.assertTrue(matrice1.isCarre(self.m13),"Pb avec l'appel isCarre("+str(self.m13)+")")
        self.assertTrue(matrice1.isCarre(self.m14),"Pb avec l'appel isCarre("+str(self.m14)+")")

    def test_moyenne1(self):
#!/bin/usr/python3oyenne(self.m11),66/12,"Pb avec l'appel moyenne("+str(self.m11)+")")
#!/bin/usr/python3oyenne(self.m13),0.,"Pb avec l'appel moyenne("+str(self.m13)+")")
#!/bin/usr/python3oyenne(self.m14),31/9,"Pb avec l'appel moyenne("+str(self.m14)+")")
#!/bin/usr/python3
    def test_additionMat1(self):
        self.assertEqual(matrice1.additionMat(self.m11,self.m17),self.m18,"Problème avec l'addition")
        self.assertEqual(matrice1.additionMat(self.m14,self.m15),self.m16,"Problème avec l'addition")


        
    def test_Matrice2(self):
        self.assertEqual(matrice2.Matrice(3,4),[[0,0,0,0],[0,0,0,0],[0,0,0,0]],"Pb avec l'appel Matrice(3,4)")
        self.assertEqual(matrice2.Matrice(5,2,'a'),[['a','a'],['a','a'],['a','a'],['a','a'],['a','a']],"Pb avec l'appel Matrice(5,2,'a')")
        
    def test_getNbLignes2(self):
        self.assertEqual(matrice2.getNbLignes(self.m21),3,"Pb avec l'appel getNbLignes("+str(self.m21)+")")
        self.assertEqual(matrice2.getNbLignes(self.m22),2,"Pb avec l'appel getNbLignes("+str(self.m22)+")")
    
    def test_getNbColonnes2(self):
        self.assertEqual(matrice2.getNbColonnes(self.m21),4,"Pb avec l'appel getNbColonnes("+str(self.m21)+")")
        self.assertEqual(matrice2.getNbColonnes(self.m22),5,"Pb avec l'appel getNbColonnes("+str(self.m22)+")")
    
    def test_getVal2(self):
        self.assertEqual(matrice2.getVal(self.m21,1,3),7,"Pb avec l'appel getVal("+str(self.m21)+"1,3)")
        self.assertEqual(matrice2.getVal(self.m22,1,3),'i',"Pb avec l'appel getVal("+str(self.m22)+"1,3)")

    def test_setVal2(self):
        matrice2.setVal(self.m21,2,0,100)
        self.assertEqual(self.m21,[[0,1,2,3],[4,5,6,7],[100,9,10,11]],"Pb avec l'appel setVal("+str(self.m21)+"2,0,100)")
        matrice2.setVal(self.m22,0,4,'z')
        self.assertEqual(self.m22,[['a','b','c','d','z'],['f','g','h','i','j']],"Pb avec l'appel setVal("+str(self.m22)+"0,4,'z')")
        
    def test_isNulle2(self):
        self.assertFalse(matrice2.isNulle(self.m21),"Pb avec l'appel isNulle("+str(self.m21)+")")
        self.assertFalse(matrice2.isNulle(self.m22),"Pb avec l'appel isNulle("+str(self.m22)+")")
        self.assertTrue(matrice2.isNulle(self.m23),"Pb avec l'appel isNulle("+str(self.m23)+")")
        
    def test_isCarre2(self):
        self.assertFalse(matrice2.isCarre(self.m21),"Pb avec l'appel isCarre("+str(self.m21)+")")
        self.assertFalse(matrice2.isCarre(self.m22),"Pb avec l'appel isCarre("+str(self.m22)+")")
        self.assertTrue(matrice2.isCarre(self.m23),"Pb avec l'appel isCarre("+str(self.m23)+")")
        self.assertTrue(matrice2.isCarre(self.m24),"Pb avec l'appel isCarre("+str(self.m24)+")")
        
    def test_moyenne2(self):
        self.assertEqual(matrice2.moyenne(self.m21),66/12,"Pb avec l'appel moyenne("+str(self.m21)+")")
        self.assertEqual(matrice2.moyenne(self.m23),0.,"Pb avec l'appel moyenne("+str(self.m23)+")")
        self.assertEqual(matrice2.moyenne(self.m24),31/9,"Pb avec l'appel moyenne("+str(self.m24)+")")

    def test_additionMat2(self):
        self.assertEqual(matrice2.additionMat(self.m21,self.m27),self.m28,"Problème avec l'addition")
        self.assertEqual(matrice2.additionMat(self.m24,self.m25),self.m26,"Problème avec l'addition")

                  
if __name__ == '__main__':
    unittest.main()
