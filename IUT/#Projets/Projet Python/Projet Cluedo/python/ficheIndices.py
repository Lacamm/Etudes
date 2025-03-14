# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module ficheIndices.py
   ~~~~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la fiche indice des joueurs. 
"""
import carte
import jeucarte
import joueur
import random

# constantes utilisées pour les indications dans la fiche
NESAISPAS='?'
POSSEDE='+'
NEPOSSEDEPAS='-'

#-----------------------------------------
# fonction annexe pour le constructeur
#-----------------------------------------


testlistejoueur=[(1,'randumy'),(2,'randumy'),(3,'randumy'),(4,'randumy'),(5,'randumy')]
testlistenumjoueur=[1,2,3,4,5]
testjeucarte=[(1,'salle1',2,'une salle','oui'),(2,'salle2',2,'une autre salle','oui'),(1,'prof1',0,'un prof','oui'),(2,'prof2',0,'une prof','oui'),(1,'mat1',1,'une matiere','oui'),(2,'mat2',1,'une AUTRE matiere','oui')]
def creerIndications(listeNumJoueurs):
    """
    retourne une dictionnaire dont les clés sont des numéros de joueur et les valeurs NESAISPAS pour toutes les clés
    paramètre: listeJoueurs une liste d'entiers strictement positifs donnant les numéros de joueurs
               engagés dans la partie
    retourne le dictionnaire décrit ci-dessus
    """
    dico={}
    for elem in listeNumJoueurs:
        dico[elem]=NESAISPAS
    return dico
#-----------------------------------------

#-----------------------------------------
assert creerIndications(testlistenumjoueur)=={1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}
#carte =(_num,_nom,_categorie,_description,_distribuable)
def FicheIndices(_listeJoueurs,_jeuCartes):
    """
    retourne une fiche indices
    paramètres: _listeJoueurs: la liste des joueurs participant à la partie
                _jeuCartes: le jeu de cartes qui sera distribué aux joueurs
    """
    dico={}
    listenumjoueur=[]
    dico['jeudecarte']=_jeuCartes
    #print(_jeuCartes)
    for elem in _listeJoueurs:
        listenumjoueur.append(elem[0])
    listenumjoueur=sorted(listenumjoueur)
    dico['listenumjoueur']=listenumjoueur
    for (_num,_nom,_categorie,_description,_distribuable) in _jeuCartes:
        if carte.estDistribuable((_num,_nom,_categorie,_description,_distribuable)):
            if _categorie not in dico.keys():
                dico[_categorie]={}
            dico[_categorie][_num]=creerIndications(listenumjoueur)
    
    return dico

assert(FicheIndices(testlistejoueur,testjeucarte))=={'jeudecarte':testjeucarte,'listenumjoueur':testlistenumjoueur,0:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},1:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},2:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}}}
testficheIndices=FicheIndices(testlistejoueur,testjeucarte)
def getJeuCartes(ficheIndices):
    """
    retourne le jeu de cartes associé à la fiche indice
    ficheIndices : la fiche considérée
    """
    return ficheIndices['jeudecarte']
assert getJeuCartes(testficheIndices)==[(1,'salle1',2,'une salle','oui'),(2,'salle2',2,'une autre salle','oui'),(1,'prof1',0,'un prof','oui'),(2,'prof2',0,'une prof','oui'),(1,'mat1',1,'une matiere','oui'),(2,'mat2',1,'une AUTRE matiere','oui')]

def getListeNumJoueurs(ficheIndices):
    """
    retourne la liste des numéros des joueurs répertoriés dans la fiche
    Cette liste doit être triée dans l'ordre croissant
    ficheIndices : la fiche considérée
    """
    return ficheIndices['listenumjoueur']
assert getListeNumJoueurs(testficheIndices)
def connaissance(ficheIndices,numJoueur,numCarte,numCategorie,indication):
    """
    met à jour la fiche indice d'un joueur en fonction des informations qu'il vient de constater c-à-d
      * soit le joueur numJoueur possède la carte identifiée par numCarte numCategorie
      * soit le joueur numJoueur ne possède pas la carte identifiée par numCarte numCategorie
    paramètres: ficheIndices la fiche considérée
                numJoueur le numéro du joueur qui a montré ou qui a indiqué ne pas avoir la carte
                numCarte le numéro de la carte concernée
                numCategorie le numéro de la catégorie de la carte concernée
                indication soit POSSEDE soit NEPOSSEDEPAS
    cette fonction ne retourne rien mais elle modifie la fiche concernée en fonction des indications
    """
    ficheIndices[numCategorie][numCarte][numJoueur]=indication


connaissance(testficheIndices,5,1,1,NEPOSSEDEPAS)
assert testficheIndices=={'jeudecarte':testjeucarte,'listenumjoueur':testlistenumjoueur,0:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},1:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NEPOSSEDEPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},2:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}}}
testficheIndices=FicheIndices(testlistejoueur,testjeucarte)
def initFicheIndices(ficheIndices,numJoueur,jeuCartes):
    """
    initialise une fiche indice appartenant au joureur numJoueur qui possède les carte contenu dans la liste
    paramètres : ficheIndices la fiche indice du joueur
                 numJoueur un entier strictement positif indiquant le numéro de joueur à qui appartient la fiche
                 jeuCartes les cartes en possession du joueur
    cette fonction ne retourne pas de résultat mais modifie la fiche du joueur de telle sorte qu'elle indique que le joueur
    numJoueur possède chacune des cartes de la liste (et que donc les autres joueurs ne les possèdent pas)
    """
    for  (_num,_nom,_categorie,_description,_distribuable) in jeuCartes:
        for joueur in ficheIndices['listenumjoueur']:
            if joueur==numJoueur:
                connaissance(ficheIndices,joueur,_num,_categorie,POSSEDE)
            else:
                connaissance(ficheIndices,joueur,_num,_categorie,NEPOSSEDEPAS)
                

initFicheIndices(testficheIndices,1,[(1,'salle1',2,'une salle','oui'),(1,'prof1',0,'un prof','oui')])
assert testficheIndices=={'jeudecarte':testjeucarte,'listenumjoueur':testlistenumjoueur,0:{1:{1:POSSEDE,2:NEPOSSEDEPAS,3:NEPOSSEDEPAS,4:NEPOSSEDEPAS,5:NEPOSSEDEPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},1:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},2:{1:{1:POSSEDE,2:NEPOSSEDEPAS,3:NEPOSSEDEPAS,4:NEPOSSEDEPAS,5:NEPOSSEDEPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}}}

# --------------------------------------------------------------#
# La partie ci-dessus doit être implémentée pour le 21 décembre #
# --------------------------------------------------------------#

def getIndication(ficheIndices,numJoueur,numCategorie,numCarte):
    """
    retourne l'indication que l'on possède concernant le joueur numJoueur et la carte numCarte,numCategorie
    paramètres: ficheIndices la fiche considérée
                numJoueur le numéro du joueur qui a montré ou qui a indiqué ne pas avoir la carte
                numCarte le numéro de la carte concernée
                numCategorie le numéro de la catégorie de la carte concernée
    resultat une des trois indications POSSEDE, NEPOSSEDEPAS ou NESAISPAS
    """
    return ficheIndices[numCategorie][numCarte][numJoueur]

assert getIndication(testficheIndices,1,0,1)==POSSEDE
def estConnue(ficheIndices,numCarte,numCategorie):
    """
    indique si pour une carte donnée soit on sait qu'elle appartient à l'un des joueurs
                                     soit on sait qu'elle n'appartient à personne
    paramètres: ficheIndices la fiche considérée
                numCarte le numéro de la carte concernée
                numCategorie le numéro de la catégorie de la carte concernée
    résultat un booléen indiquant si on sait définitivement si la carte appartient à un joueur ou à personne
    """
    i=0
    stk=ficheIndices[numCategorie][numCarte].values()
    for elem in stk:
        if elem == POSSEDE:
            return True
        if elem == NEPOSSEDEPAS:
            i+=1
    if i== len(stk):
        return True
    return False

assert estConnue(testficheIndices,1,2)==True
def estDansLeMystere(ficheIndices,numCarte,numCategorie):
    """
    indique si on est sûr que la carte est dans le mystère
    paramètres: ficheIndices la fiche considérée
                numCarte le numéro de la carte concernée
                numCategorie le numéro de la catégorie de la carte concernée
    résultat un booléen indiquant si on sait définitivement que la carte n'appartient à personne
    """
    for elem in ficheIndices[numCategorie][numCarte].values():
        if elem == POSSEDE or elem == NESAISPAS:
            return False
    return True
assert estDansLeMystere(testficheIndices,1,2)==False
def listeCartesInconnues(ficheIndices,categorie):
    """
    retourne la liste des numéros de cartes d'une certaine catégorie pour lesquelles on n'a pas de certitude
    paramètres: ficheIndices la fiche considérée
                numCategorie le numéro de la catégorie recherchée
    résultat la liste des numéros de carte de la catégorie pour lesquelles on n'a pas de certitude
    """
    res=[]
    for numCarte in ficheIndices[categorie].keys():
        i=0
        stk=ficheIndices[categorie][numCarte].values()
        for elem in stk:
            if elem==NESAISPAS:
                i+=1
                if i==len(stk)-1:
                    res.append(numCarte)
    return res
assert listeCartesInconnues(testficheIndices,1)==[1,2]
assert listeCartesInconnues(testficheIndices,2)==[2]


def listeCartesJoueur(ficheIndices,numCategorie,numJoueur):
    """
    retourne la liste des numéros de cartes d'une catégorie que l'on sait possédées par le joueur numJoueur
    paramètres: ficheIndices la fiche considérée
                numCategorie le numéro de la catégorie cherchée
                numJoueur le joueur dont on recherche les cartes
    résultat la liste des numéros cartes de la catégorie pour lesquelles on a la certitude que le joueur numJoueur la possède
    """
    res=[]
    for elem in ficheIndices[numCategorie].keys():
        if getIndication(ficheIndices,numJoueur,numCategorie,elem)==POSSEDE:
            res.append(elem)
    return res

assert listeCartesJoueur(testficheIndices,1,1)==[]
assert listeCartesJoueur(testficheIndices,0,1)==[1]

def hypothesesSures(ficheIndices):
    """
    retourne un dictionnaire dont les clés sont les catégories de carte et les valeurs la carte de la
    catégorie correspondante que l'on sait être dans la solution. Si on n'a aucune certitude pour une 
    catégorie, la clé ne sera pas présente dans le dictionnaire.
    paramètres: ficheIndices la fiche considérée
    résultat le dictionnaire décrit ci dessus
    """ 
    dico={}
    for elem in range (0,3) :  
        for elem2 in ficheIndices[elem]:
            if estDansLeMystere(ficheIndices,elem2,elem):
                dico[elem]=elem2
                break
    return dico 
        
assert hypothesesSures(testficheIndices)=={}
def choixCartes(ficheIndices,numJoueur,numCategorie):
    """
    retourne une liste de numéros de carte d'une certaine catégorie pouvant être 
    utilisée pour émettre une hypothèse intéressante pour le joueur numJoueur
    paramètres: ficheIndices la fiche considérée
                numJoueur le joueur dont on recherche les cartes
                numCategorie le numéro de la cherchée
    résultat la liste des numéros de cartes de la catégorie intéressant pour le joueur numJoueur
    """
    res=[]
    for carte,_ in ficheIndices[numCategorie].items():
        if ficheIndices[numCategorie][carte][numJoueur]==NESAISPAS:
            res.append(carte)
    return res
assert choixCartes(testficheIndices,5,1)==[1,2]

def creerUneHypothese(ficheIndices,numJoueur,numSalle):
    """
    retourne un couple numProf, numMat indiquant les cartes choisies comme hypothèse. 
    La salle est fixée par numSalle 
    paramètres: ficheIndices la fiche considérée
                numJoueur le joueur qui formule l'hypothèse
                numSalle le numéro de la salle dans laquelle se trouve le joueur
    """
    res=[]
    z=False
    y=False
    for elem in ficheIndices['listenumjoueur']:
        if z==False:
            choixprof=choixCartes(ficheIndices,elem,0)
            if choixprof!=[]:
                z=True
                prof=choixprof[0]
        if y==False:
            choixmat=choixCartes(ficheIndices,elem,1)
            if choixmat!=[]:
                y=True
                mat=choixmat[1]
    return (prof,mat)
            
assert creerUneHypothese(testficheIndices,1,1)==(2,2)
    

#-----------------------------------------
# entrees-sorties
#-------------------------estDansLeMystere()----------------

def string(ficheIndices):
    """
    Transforme une fiche indice en une chaine de caractères
    paramètre:  ficheIndices la fiche considérée 
    """
    jeu=getJeuCartes(ficheIndices)
    listeNumJoueur=getListeNumJoueurs(ficheIndices)
    
    res=" "*34+"Fiche Indices\n"
    res+=carte.categorieFromNum(carte.PROFESSEUR).ljust(38+len(listeNumJoueur)*2)+carte.categorieFromNum(carte.MATIERE).ljust(38)+"\n"
    for x in range(2):
        res+=' '*36
        for n in listeNumJoueur:
            res+=str(n)+' '        
    res+='\n'
    lesNum=jeucarte.getListeNumCarteCategorie(jeu,carte.PROFESSEUR)
    lesNum.sort()
    lesNum2=jeucarte.getListeNumCarteCategorie(jeu,carte.MATIERE)
    lesNum2.sort()
    for x in range(max(len(lesNum),len(lesNum2))):
        if x<len(lesNum):
            res+=(str(lesNum[x]).rjust(2)+'. '+jeucarte.getNomCarteParNum(jeu,carte.PROFESSEUR,lesNum[x])).rjust(34)+': '
            for j in listeNumJoueur:
                res+=getIndication(ficheIndices,j,carte.PROFESSEUR,lesNum[x])+' '
        else:
            res+=' '*(34+len(listeNumJoueur)*2)
        if x<len(lesNum2):
            res+=(str(lesNum2[x]).rjust(2)+'. '+jeucarte.getNomCarteParNum(jeu,carte.MATIERE,lesNum2[x])).rjust(34)+': '
            for j in listeNumJoueur:
                res+=getIndication(ficheIndices,j,carte.MATIERE,lesNum2[x])+' '
        res+='\n'
    
    res+=carte.categorieFromNum(carte.SALLE).ljust(34)+"\n"
    res+=' '*36
    for j in listeNumJoueur:
        res+=str(j)+' '
    res+='\n'
    lesNum=jeucarte.getListeNumCarteCategorie(jeu,carte.SALLE)
    lesNum.sort()
    for i in lesNum:
        res+=(str(i).rjust(2)+'. '+jeucarte.getNomCarteParNum(jeu,carte.SALLE,i)).rjust(34)+': '
        for j in listeNumJoueur:
            res+=getIndication(ficheIndices,j,carte.SALLE,i)+' '
        res+='\n'
    return res
