#!/usr/bin/python3
import unittest


from transport import *

class TestTransport(unittest.TestCase):
    def setUp(self):
        self.p1=Personne("toto",42,"tram")
        self.p2=Personne("titi",35,"vélo")
        self.p3=Personne("tutu",25,"vélo")
        self.p4=Personne("tyty",44,"tram")
        self.p5=Personne("xxx",22,"voiture")
        self.lp=[self.p1,self.p2,self.p3,self.p4,self.p5]
    
    def test_getNom(self):
        self.assertEqual(getNom(self.p1),"toto","Pb avec l'appel getNom("+str(self.p1)+")")
        self.assertEqual(getNom(self.p3),"tutu","Pb avec l'appel getNom("+str(self.p3)+")")
        self.assertEqual(getNom(self.p5),"xxx","Pb avec l'appel getNom("+str(self.p5)+")")


    def test_getAge(self):
        self.assertEqual(getAge(self.p1),42,"Pb avec l'appel getAge("+str(self.p1)+")")
        self.assertEqual(getAge(self.p2),35,"Pb avec l'appel getAge("+str(self.p2)+")")
        self.assertEqual(getAge(self.p4),44,"Pb avec l'appel getAge("+str(self.p4)+")")
        

    def test_getMoyenTransport(self):
        self.assertEqual(getMoyenTransport(self.p1),"tram","Pb avec l'appel getMoyenTransport("+str(self.p1)+")")
        self.assertEqual(getMoyenTransport(self.p3),"vélo","Pb avec l'appel getMoyenTransport("+str(self.p3)+")")
        self.assertEqual(getMoyenTransport(self.p5),"voiture","Pb avec l'appel getMoyenTransport("+str(self.p5)+")")
        

    def test_setNom(self):
        p=Personne("xxx",32,"vélo")
        for nom in ['yyyy','zzzz','wwww']:
            setNom(p,nom)
            self.assertEqual(getNom(p),nom,"Pb avec l'appel setNom("+str(p)+","+nom+")")

    def test_setAge(self):
        p=Personne("xxx",32,"vélo")
        for age in [12,25,55]:
            setAge(p,age)
            self.assertEqual(getAge(p),age,"Pb avec l'appel setAge("+str(p)+","+str(age)+")")

    def test_setMoyenTransport(self):
        p=Personne("xxx",32,"vélo")
        for moyen in ["train","voiture","fusée"]:
            setMoyenTransport(p,moyen)
            self.assertEqual(getMoyenTransport(p),moyen,"Pb avec l'appel setMoyenTransport("+str(p)+","+str(moyen)+")")


    def test_ageMoyenUtilisateurTransport(self):
        res=[("tram",43),("vélo",30),("voiture",22),("fusée",-1)]
        for moyen,age in res:
            self.assertEqual(ageMoyenUtilisateurTransport(self.lp,moyen),age,"Pb avec l'appel setMoyenTransport("+str(self.lp)+','+str(moyen)+")\n")


    def test_listeMoyensTransport(self):
        self.assertEqual(listeMoyensTransport([]),[],"Pb avec l'appel listeMoyensTransport([])")
        res=listeMoyensTransport(self.lp)
        res.sort()
        attendu=["tram","vélo","voiture"]
        attendu.sort()
        self.assertEqual(res,attendu,"Pb avec l'appel listeMoyensTransport("+str(self.lp)+")")
        
        
if __name__ == '__main__':
    unittest.main()