#!/usr/bin/python3
import unittest

'''
Cas de tests pour le fichier labyrinthe.py
'''

from labyrinthe import *

class TestLabyrinthe(unittest.TestCase):
    def annexe(self,nomFic, strm):
        fic=open(nomFic,"w")
        fic.write(strm)
        fic.close()
        return chargeMatrice(nomFic)
        
    def setUp(self):
        strm1="9,9\n"\
            +"2,1,1,1,1,1,1,1,1\n"\
            +"0,0,0,1,1,1,1,1,1\n"\
            +"1,1,0,1,0,0,0,0,1\n"\
            +"1,1,0,1,0,1,1,0,1\n"\
            +"1,1,0,0,0,0,0,0,1\n"\
            +"1,1,1,0,1,1,1,0,1\n"\
            +"1,1,1,0,1,1,1,0,1\n"\
            +"1,1,1,0,0,0,0,0,1\n"\
            +"1,1,1,1,1,1,1,0,3\n"
        
        strm2="9,9\n"\
            +"2,1,1,1,1,1,1,1,1\n"\
            +"0,0,0,1,1,1,1,1,1\n"\
            +"1,1,0,1,0,0,0,0,1\n"\
            +"1,1,0,1,0,1,1,0,1\n"\
            +"1,1,0,0,1,0,0,0,1\n"\
            +"1,1,1,0,1,1,1,0,1\n"\
            +"1,1,1,0,1,1,1,0,1\n"\
            +"1,1,1,0,1,0,0,0,1\n"\
            +"1,1,1,1,1,1,1,0,3\n"

        strm3="9,9\n"\
            +"2,1,1,1,1,1,1,1,1\n"\
            +"0,0,0,1,0,0,0,1,1\n"\
            +"1,1,0,1,0,1,0,0,1\n"\
            +"1,1,0,1,0,1,1,0,1\n"\
            +"1,1,0,0,0,1,0,1,1\n"\
            +"1,1,1,0,1,1,0,1,1\n"\
            +"1,1,1,0,1,1,0,1,1\n"\
            +"1,1,1,0,1,0,0,0,1\n"\
            +"1,1,1,1,1,1,1,0,3\n"
        
        self.m1=self.annexe("_mat.txt",strm1)
        self.m2=self.annexe("_mat.txt",strm2)
        self.m3=self.annexe("_mat.txt",strm3)

    def test_labyrintheValide(self):
        self.assertTrue(labyrintheValide(self.m1),"Pb Validité de "+str(self.m1))
        self.assertFalse(labyrintheValide(self.m2),"Pb Validité de "+str(self.m2))
        self.assertFalse(labyrintheValide(self.m3),"Pb Validité de "+str(self.m3))
        

    def test_marquageDirect(self):
        c=newMatrice(9,9,0)
        setVal(c,4,4,6)
        marquageDirect(c,self.m1,6,7)
        self.assertEqual(getVal(c,4,3),7,"Pb test marquageDirect voisin non marqué")
        self.assertEqual(getVal(c,4,5),7,"Pb test marquageDirect voisin non marqué")
        self.assertEqual(getVal(c,3,4),7,"Pb test marquageDirect voisin non marqué")
        self.assertEqual(getVal(c,5,4),0,"Pb test marquageDirect voisin marqué non souhaité")
        c=newMatrice(9,9,0)
        setVal(c,8,7,6)
        marquageDirect(c,self.m3,6,7)
        self.assertEqual(getVal(c,8,8),7,"Pb test marquageDirect voisin non marqué")
        self.assertEqual(getVal(c,7,7),7,"Pb test marquageDirect voisin non marqué")
        self.assertEqual(getVal(c,8,6),0,"Pb test marquageDirect voisin marqué non souhaité")
        


    def test_estAccessible(self):
        self.assertTrue(estAccessible(self.m1,(0,0),(8,8)),"Pb Accessibilité sur la matrice "+str(self.m1)+" entre (0,0) et (8,8)")
        self.assertFalse(estAccessible(self.m2,(8,5),(3,4)),"Pb Accessibilité sur la matrice "+str(self.m2)+" entre (8,5) et (3,4)")
        self.assertTrue(estAccessible(self.m3,(3,4),(3,7)),"Pb Accessibilité sur la matrice "+str(self.m3)+" entre (3,4) et (3,7)")
        self.assertFalse(estAccessible(self.m3,(0,0),(8,8)),"Pb Accessibilité sur la matrice "+str(self.m3)+" entre (0,0) et (8,8)")
        self.assertFalse(estAccessible(self.m2,(0,0),(8,8)),"Pb Accessibilité sur la matrice "+str(self.m3)+" entre (0,0) et (8,8)")
        

    def test_estAccessible2(self):
        self.assertFalse(estAccessible2(self.m1,(0,0),(8,8))==None,"Pb Accessibilité sur la matrice "+str(self.m1)+" entre (0,0) et (8,8)")
        self.assertFalse(estAccessible2(self.m2,(8,5),(3,4))==None,"Pb Accessibilité sur la matrice "+str(self.m2)+" entre (8,5) et (3,4)")
        self.assertFalse(estAccessible2(self.m3,(3,4),(3,7))==None,"Pb Accessibilité sur la matrice "+str(self.m3)+" entre (3,4) et (3,7)")
        self.assertTrue(estAccessible2(self.m3,(0,0),(8,8))==None,"Pb Accessibilité sur la matrice "+str(self.m3)+" entre (0,0) et (8,8)")
        self.assertTrue(estAccessible2(self.m2,(0,0),(8,8))==None,"Pb Accessibilité sur la matrice "+str(self.m3)+" entre (0,0) et (8,8)")
        

    def test_plusCourtChemin(self):
        self.assertEqual(plusCourtChemin(self.m1,(0,0),(4,3)),[(0,0),(1,0),(1,1),(1,2),(2,2),(3,2),(4,2),(4,3)],"Pb plusCourtChemin sur "+str(self.m1)+" entre (0,0) et (4,3)")
        self.assertEqual(plusCourtChemin(self.m1,(2,6),(6,7)),[(2,6),(2,7),(3,7),(4,7),(5,7),(6,7)],"Pb plusCourtChemin sur "+str(self.m1)+" entre (2,6) et (6,7)")


    def test_cheminDecroissant(self):
        strm="9,9\n"\
            +"17,0,0,0,0,0,0,0,0\n"\
            +"16,15,14,0,0,0,0,0,0\n"\
            +"0,0,13,0,11,10,9,8,0\n"\
            +"0,0,12,0,12,0,0,7,0\n"\
            +"0,0,11,10,9,8,7,6,0\n"\
            +"0,0,0,9,0,0,0,5,0\n"\
            +"0,0,0,8,0,0,0,4,0\n"\
            +"0,0,0,7,6,5,4,3,0\n"\
            +"0,0,0,0,0,0,0,2,1\n"
        c1=self.annexe("_mat1.txt",strm)
        chem=cheminDecroissant(c1,(8,8),(0,0))
        print(chem)
        res=  chem==[(8, 8), (8, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (6, 3), (5, 3), (4, 3), (4, 2), (3, 2), (2, 2), (1, 2), (1, 1), (1, 0), (0, 0)]\
           or chem==[(8, 8), (8, 7), (7, 7), (6, 7), (5, 7), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (3, 2), (2, 2), (1, 2), (1, 1), (1, 0), (0, 0)]
        self.assertTrue(res,"Pb chemin décroissant sur le calque "+strm+" entre (8,8),(0,0)")


if __name__ == '__main__':
    unittest.main()

