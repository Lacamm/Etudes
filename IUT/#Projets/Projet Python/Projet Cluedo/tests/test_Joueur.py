#!/usr/bin/python3
import unittest


import jeucarte
import carte
import mystere
import random
import joueur


#-----------------------------------------
# contructeur
#-----------------------------------------
class TestCase(unittest.TestCase):
    def setUp(self):
        self.joueur1=joueur.Joueur(1,'joueur1')
        self.joueur2=joueur.Joueur(2,'joueur2',True)
        self.joueur3=joueur.Joueur(3,'joueur3',False)
        
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
        joueur.ajouterCarte(self.joueur1,self.cartes[0])
        joueur.ajouterCarte(self.joueur1,self.cartes[2])
        joueur.ajouterCarte(self.joueur1,self.cartes[4])
        joueur.ajouterCarte(self.joueur2,self.cartes[5])
        joueur.ajouterCarte(self.joueur2,self.cartes[1])
        joueur.ajouterCarte(self.joueur2,self.cartes[3])

    def test_getNum(self):
        self.assertEqual(joueur.getNum(self.joueur1),1,"Problème avec l'appel à getNum("+str(self.joueur1)+")")
        self.assertEqual(joueur.getNum(self.joueur2),2,"Problème avec l'appel à getNum("+str(self.joueur2)+")")
        self.assertEqual(joueur.getNum(self.joueur3),3,"Problème avec l'appel à getNum("+str(self.joueur3)+")")

    def test_getNom(self):
        self.assertEqual(joueur.getNom(self.joueur1),'joueur1',"Problème avec l'appel à getNom("+str(self.joueur1)+")")
        self.assertEqual(joueur.getNom(self.joueur2),'joueur2',"Problème avec l'appel à getNom("+str(self.joueur2)+")")
        self.assertEqual(joueur.getNom(self.joueur3),'joueur3',"Problème avec l'appel à getNom("+str(self.joueur3)+")")
  
    def test_estHumain(self):
        self.assertFalse(joueur.estHumain(self.joueur1),"Problème avec l'appel à estHumain("+str(self.joueur1)+")")
        self.assertTrue(joueur.estHumain(self.joueur2),"Problème avec l'appel à estHumain("+str(self.joueur2)+")")
        self.assertFalse(joueur.estHumain(self.joueur3),"Problème avec l'appel à estHumain("+str(self.joueur3)+")")
    
    def test_elimine(self):
        j=joueur.Joueur(4,'joueur4')
        self.assertFalse(joueur.estElimine(j),"Problème avec l'appel à estElimine("+str(j)+")")
        joueur.setElimine(j,True)
        self.assertTrue(joueur.estElimine(j),"Problème avec l'appel à estElimine("+str(j)+") ou la fonction setElimine ne marche pas")
        joueur.setElimine(j,False)
        self.assertFalse(joueur.estElimine(j),"Problème avec l'appel à estElimine("+str(j)+") ou la fonction setElimine ne marche pas")
   
    def test_setHumain(self):
        j=joueur.Joueur(4,'joueur4')
        joueur.setElimine(j,False)
        self.assertFalse(joueur.estHumain(j),"Problème avec l'appel à estHumain("+str(j)+") ou la fonction setHumain ne marche pas")
        joueur.setHumain(j,True)
        self.assertTrue(joueur.estHumain(j),"Problème avec l'appel à estHumain("+str(j)+") ou la fonction setHumain ne marche pas")
            
    def test_possede(self):
        self.assertFalse(joueur.possede(self.joueur1,self.cartes[1]),"Problème avec l'appel à possede("+str(self.joueur1)\
                         +","+str(self.cartes[1])+")")
        self.assertFalse(joueur.possede(self.joueur3,self.cartes[1]),"Problème avec l'appel à possede("+str(self.joueur3)\
                         +","+str(self.cartes[1])+")")
        self.assertTrue(joueur.possede(self.joueur1,self.cartes[4]),"Problème avec l'appel à possede("+str(self.joueur1)\
                         +","+str(self.cartes[4])+") Attention le pb peut venir de ajouterCarte")
        self.assertTrue(joueur.possede(self.joueur2,self.cartes[5]),"Problème avec l'appel à possede("+str(self.joueur2)\
                         +","+str(self.cartes[5])+") Attention le pb peut venir de ajouterCarte")
    
    
        
    def test_possedeParNum(self):
        self.assertEqual(joueur.possedeParNum(self.joueur1,carte.SALLE,1),None,"Problème avec l'appel à possedeParNum("+str(self.joueur1)\
                         +","+str(carte.SALLE)+"1,)")
        self.assertEqual(joueur.possedeParNum(self.joueur3,carte.SALLE,1),None,"Problème avec l'appel à possedeParNum("+str(self.joueur3)\
                         +","+str(carte.SALLE)+"1,)")
        self.assertEqual(joueur.possedeParNum(self.joueur1,carte.SALLE,2),self.cartes[4],"Problème avec l'appel à possedeParNum("+str(self.joueur1)\
                         +","+str(carte.SALLE)+",2) Attention le pb peut venir de ajouterCarte")
        self.assertEqual(joueur.possedeParNum(self.joueur2,carte.MATIERE,2),self.cartes[5],"Problème avec l'appel à possedeParNum("+str(self.joueur2)\
                         +","+str(carte.MATIERE)+",2) Attention le pb peut venir de ajouterCarte")
    
    def test_cartesPossedees(self):
        hp=mystere.Mystere(1,2,1)
        self.assertEqual(joueur.cartesPossedees(self.joueur3,hp),[],"Problème avec l'appel à cartesPossedees("+\
                         str(self.joueur3)+","+str(hp)+")")
        l=joueur.cartesPossedees(self.joueur2,hp)
        ok=len(l)==2 and self.cartes[1] in l and self.cartes[5] in l   
        self.assertEqual(ok,True,"Problème avec l'appel à cartesPossedees("+\
                         str(self.joueur2)+","+str(hp)+")        ")
        self.assertEqual(joueur.cartesPossedees(self.joueur1,hp),[self.cartes[0]],"Problème avec l'appel à cartesPossedees("+\
                         str(self.joueur1)+","+str(hp)+")        ")
    
    def test_reponseHypothese(self):
        hp=mystere.Mystere(1,2,1)
        self.assertIn(joueur.reponseHypothese(self.joueur3,hp),[None],"Problème avec l'appel à reponseHypothese("+\
                         str(self.joueur3)+","+str(hp)+")")
        self.assertIn(joueur.reponseHypothese(self.joueur2,hp),[self.cartes[1],self.cartes[5]],"Problème avec l'appel à reponseHypothese("+\
                         str(self.joueur2)+","+str(hp)+")")
        self.assertIn(joueur.reponseHypothese(self.joueur1,hp),[self.cartes[0]],"Problème avec l'appel à reponseHypothese("+\
                         str(self.joueur1)+","+str(hp)+")")

if __name__ == '__main__':
    unittest.main()