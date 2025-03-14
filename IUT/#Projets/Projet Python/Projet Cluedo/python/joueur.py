# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module joueur.py
   ~~~~~~~~~~~~~~~~
   
   Ce module gère les joueurs du Cluedo. 
"""

import jeucarte
import carte
import ficheIndices
import random
import mystere

#-----------------------------------------
# contructeur
#-----------------------------------------
def Joueur(_num,_nom,_humain=False,_elimine=False):
    """
    retourne un joueur de cluedo. Un joueur est identifié par un numéro strictement positif, 
    il posède un  nom et il peut être humain ou non. Il possèdera aussi des cartes et une fiche indice. 
    Le constructeur ne donne aucune carte au joueur et met la fiche indice à vide
    paramètres: _num un entier strictement positif identifiant le joueur
                _nom une chaine de caractère fournissant le nom du joueur
                _humain un booléen indiquant si le joueur est humain ou non
                _elimine indique si un joueur a tenté une réponse qui n'était pas correcte
    """
    return [_num,_nom,_humain,_elimine,[],dict()]

#-----------------------------------------
# getters
#-----------------------------------------
def getNum(joueur):
    """
    retourne le numéro du joueur
    paramètre: joueur le joueur considéré
    """ 
    return joueur[0]

def getNom(joueur):
    """
    retourne le nom du joueur
    paramètre: joueur le joueur considéré
    """    
    return joueur[1]

def getCartes(joueur):
    """
    retourne sous la forme d'un jeu de cartes, les cartes possédées par le joueur
    paramètre: joueur le joueur considéré
    """ 
    return joueur[4]

def getFiche(joueur):
    """
    retourne la fiche du joueur
    paramètre: joueur le joueur considéré
    """
    return joueur[5]

def estHumain(joueur):
    """
    indique si le joueur est humain ou non
    paramètre: joueur le joueur considéré
    """
    return joueur[2]

def estElimine(joueur):
    """
    indique si le joueur est éliminé non
    paramètre: joueur le joueur considéré
    """
    return joueur[3]

#-----------------------------------------
# setters
#-----------------------------------------
def setHumain(joueur,humain):
    """
    permet de positionner l'indicateur humain du joueur
    paramètres: joueur le joueur considéré
                humain un booléen à True si le joueur est humain
    cette fonction ne retourne rien mais modifie le joueur
    """    
    joueur[2] = True
    
def setElimine(joueur,elimine):
    """
    permet de positionner l'indicateur elimine du joueur
    paramètres: joueur le joueur considéré
                elimine un booléen indiquant si le joueur est éliminé ou non
    cette fonction ne retourne rien mais modifie le joueur
    """ 
    joueur[3] = True
    
def ajouterCarte(joueur,carte):
    """
    donne une nouvelle carte à un joueur
    paramètres: joueur le joueur considéré
                carte la carte à attribuer au joueur
    cette fonction ne retourne rien mais modifie le joueur    
    """
    joueur[4].append(carte)

def initialiseFiche(joueur,listeJoueurs,jeuCartes):
    """
    initialise la fiche d'un joueur en fonction des cartes qu'il possède
    paramètres: joueur le joueur considéré
                listeJoueurs la liste des joueurs
                jeuCartes le jeu de cartes qui sont distribuées
    cette fonction ne retourne rien mais modifie le joueur (sa fiche)
    """    
    FicIndice = ficheIndices.FicheIndices(listeJoueurs,jeuCartes)
    joueur[5]=FicIndice
    ficheIndices.initFicheIndices(FicIndice,getNum(joueur),getCartes(joueur))
    

#-----------------------------------------
# observateurs
#-----------------------------------------
def possede(joueur,carte):
    """
    indique si un joueur possède une carte ou non
    paramètres: joueur le joueur considéré
                carte une carte 
    résultat un booléen indiquant si le joueur possède la carte ou non
    """    
    return (carte in joueur[4])

def possedeParNum(joueur,cat,num):
    """
    indique si un joueur possède une carte identifiée par sa catégorie et son numéro
    paramètres: joueur le joueur considéré
                cat le numéro de la catégorie
                num le numéro de la carte
    résultat: None si le joueur ne possède pas la carte ou la carte concernée s'il la possède
    """
    for cartes in joueur[4]:
        if cartes[0] == num and cartes[2] == cat:
            return cartes
    return None

def cartesPossedees(joueur,hypothese):
    """
    retourne les cartes de l'hypothèse que le joueur possède.
    Le résultat est rendu sous la forme d'une liste d'identifiants de carte 
    paramètres: joueur le joueur considéré
                hypothese une hypothèse
    resultat la liste des cartes définie ci dessus
    """
    res = []
    if possedeParNum(joueur,1,hypothese[0]) != None:
        res.append(possedeParNum(joueur,1,hypothese[0]))
    if possedeParNum(joueur,2,hypothese[1]) != None:
        res.append(possedeParNum(joueur,2,hypothese[1]))
    if possedeParNum(joueur,3,hypothese[2]) != None:
        res.append(possedeParNum(joueur,3,hypothese[2]))
    return res

def reponseHypothese(joueur,hypothese):
    """
    retourne une des cartes choisie au hasard
    de l'hypothèse possédée par le joueur
    Si le joueur ne possède aucune carte le fonction retourne None
    paramètres: joueur le joueur considéré
                hypothese une hypothèse
    resultat une des cartes de l'hypothèse ou None    
    """
    CartePoss = cartesPossedees(joueur,hypothese)
    random.shuffle(CartePoss)
    if CartePoss == []:
        return None
    return CartePoss[0]

#----------------------------------------
# Entrées-sorties
#----------------------------------------
def lireJoueurs(ficJoueur):
    """
    permet de lire la liste des joueurs d'une partie dans un fichier de texte
    paramètres: ficJoueur le nom du fichier contenant les joueurs
    resultat : une liste de joueurs
    """
    res=[]
    try:
        fic=open(ficJoueur)
        contenu=fic.read().split('\n')
        fic.close()
    except:
        print("Problème de lecture du fichier",ficJoueur)
        return res
    
    i=1
    numJoueur=['1','2','3','4','5','6']
    for ligne in contenu:
        j=ligne.split(',')
        if len(j)!=3:
            if j!=['']:
                print('ligne',i,"ignorée car pas le bon nombre d'information\n")
        else:
            if j[0] not in numJoueur:
                print('ligne',i,"ignorée car le numero de joueur n'est pas correct\n")
            else:
                res.append(Joueur(int(j[0]),j[1],j[2]=='humain'))
                numJoueur.remove(j[0])
        i+=1
    return res

def string(joueur):
    """
    transforme un joueur sous la forme d'une chaine de caractères en vue d'affichage
    paramètres: joueur le joueur considéré
    resultat une chaine de caractère contenant les informations sur le joueur
    """
    if estHumain(joueur):
        humain=" humain"
    else:
        humain=" ordinateur"
    if estElimine(joueur):
        elimine="eliminé"
    else:
        elimine=""
        
    return '-'*10+'\nnum: '+str(getNum(joueur))+' nom: '+getNom(joueur)+humain+" "+elimine+'\nCartes:\n'+\
           jeucarte.string(getCartes(joueur))+ficheIndices.string(getFiche(joueur))

