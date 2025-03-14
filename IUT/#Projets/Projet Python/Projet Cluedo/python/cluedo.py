# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module cluedo.py
   ~~~~~~~~~~~~~~~~
   
   Ce module gère le jeu du cluedo. 
"""
import joueur
import plateau
import jeucarte
import carte
import ficheIndices
import mystere
import piece
import random
import entree

NESAISPAS='?'
POSSEDE='+'
NEPOSSEDEPAS='-'

testlistejoueur=[(1,'MAXBUTTY'),(2,'MAMADOU'),(3,'JESAISPAS'),(4,'BONJOUR'),(5,'ADEMAIN')]
testlistenumjoueur=[1,2,3,4,5]
testjeucarte=[(1,'salle1',2,'une salle','oui'),(2,'salle2',2,'une autre salle','oui'),(1,'prof1',0,'un prof','oui'),(2,'prof2',0,'une prof','oui'),(1,'mat1',1,'une matiere','oui'),(2,'mat2',1,'une AUTRE matiere','oui')]

listeJ = [[1,'MAXBUTTY',True,False,[],{'jeudecarte':testjeucarte,'listenumjoueur':testlistenumjoueur,0:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},1:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},2:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}}}],[2,'MAMADOU',False,False,[],None],[3,'JESAISPAS',True,False,[],None],[4,'BONJOUR',False,False,[],None],[5,'ADEMAIN',False,False,[],None]]

cluedo_test = {'jeuCarte': [(1,'Salle à manger',3,'mangeeer',True),(2,'SDD',2,'SE PENDRE',True),(3,'i23',3,'TRAVAILLLER',True)], 'plateau': [[[0,0],[0,0]],[(1,[(1,2),(2,2)],[1,4,5,2],[None,[None,None]],[(2,[(0,2),(1,0)],[3],[None,[None,None]])])]], 'listeJoueurs': listeJ,
            'solution': (1,3,2), 'joueurCourant': listeJ[0], 'numTour': 1}

def distribuerCartes(jeuCarte,listeJoueurs):
    """
    distribue les carte d'un jeu de carte aux joueurs
    paramètres jeuCarte un jeu de carte mélangé
               listeJoueurs la liste des joueurs participant au jeu
    """
    NombreTotalCartes = 0
    for cartes in jeuCarte:
        if carte.estDistribuable(cartes):
            NombreTotalCartes += 1
    cptD = 0
    for joueurs in listeJoueurs:
        for i in range(cptD,NombreTotalCartes,len(listeJoueurs)):
            if carte.estDistribuable(jeuCarte[i]):
                joueur.ajouterCarte(joueurs,jeuCarte[i])
        cptD += 1    

def joueurPrincipal(listeJoueurs):
    """
    retourne le joueur principal c'est à dire le premier joueur humain
    ou si aucun joueur est humain, c'est le premier joueur
    paramètre: listeJoueurs la liste des joueurs participant au jeu
    résultat le joueur principal
    """
    if listeJoueurs==[]:
        return None
    for joueurs in listeJoueurs:
        if joueur.estHumain(joueurs):
            return joueurs
    return listeJoueurs[0]

#print(joueurPrincipal(cluedo_test['listeJoueurs']))

#-----------------------------------------
# contructeur
#-----------------------------------------

def Cluedo(ficJoueurs, ficCartes, ficPlateau):
    """
    Construit un nouveau jeu de cluedo à partir de trois fichiers: les joueurs, les cartes et le plateau
    paramètres: ficJoueurs le nom du fichier des joueurs
                ficCartes le nom du fichier contenant la description des cartes
                ficPlateau le nom du fichier contenant l'état du plateau
    Cette fonction retourne un nouveau jeu de cluedo (une nouvelle partie), elle va donc initialiser les joueurs,
    le plateau le jeu de carte, tirer au hasard une énigme et distribuer les cartes au joueurs.
    Les fiches indices de chaque joueur seront initialisées et les pions des joueurs seront placés sur leur départ
    Le joueur principal (celui dont on voit la fiche indice) est soit le joueur humain s'il y en a un, le premier joueur sinon
    """
    plat = plateau.lirePlateau(ficPlateau)
    listeJoueurs = joueur.lireJoueurs(ficJoueurs)
    listenumJ = []
    for elem in listeJoueurs:
        listenumJ.append(joueur.getNum(elem))

    plateau.poserPionCaseDepart(plat,listenumJ)
    jeuCarte = jeucarte.lireJeuCarte(ficCartes)
    jeuCarteSansMystere =jeucarte.lireJeuCarte(ficCartes)
    mystere = jeucarte.definirMystere(jeuCarteSansMystere)
    distribuerCartes(jeuCarteSansMystere, listeJoueurs)

    for cartes in jeuCarte:
        if carte.getNum(cartes) == 10 and carte.getCategorie(cartes) == 3:
            cartes[4] = False

    for i in range(len(listeJoueurs)):
        jeucartesjoueur = joueur.getCartes(listeJoueurs[i])
        joueur.initialiseFiche(listeJoueurs[i],listeJoueurs,jeuCarte)

    return {'jeuCarte': jeuCarte, 'plateau': plat, 'listeJoueurs': listeJoueurs,
            'solution': mystere, 'joueurCourant': joueurPrincipal(listeJoueurs), 'numTour': 1}


def getJoueurCourant(cluedo):
    """
    retourne le joueur courant (c-à-d celui à qui c'est le tour de jouer)
    paramètre: cluedo le jeu de cluedo
    resultat: le joueur 
    """
    try:
        return cluedo['joueurCourant']
    except :
        return None

assert getJoueurCourant(cluedo_test) == [1,'MAXBUTTY',True,False,[],{'jeudecarte':testjeucarte,'listenumjoueur':testlistenumjoueur,0:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},1:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}},2:{1:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS},2:{1:NESAISPAS,2:NESAISPAS,3:NESAISPAS,4:NESAISPAS,5:NESAISPAS}}}]

def getIndiceJoueurCourant(cluedo):
    """
    retourne l'indice dans l'ordre des joueurs du courant (c-à-d celui à qui c'est le tour de jouer)
    paramètre: cluedo le jeu de cluedo
    resultat: un entier représentant le numéro d'ordre du joueur
    """
    cpt = 0
    while cpt < len(cluedo['listeJoueurs']):
        if cluedo['listeJoueurs'][cpt] == getJoueurCourant(cluedo):
            return cpt
        cpt += 1

def getSolution(cluedo):
    """
    retourne la solution à trouver sous la forme d'un Mystere
    paramètre: cluedo le jeu de cluedo
    resultat: une structure de type Mystere solution de l'énigme
    """
    return cluedo['solution']

def getNbJoueurs(cluedo):
    """
    retourne le nombre de joueurs engagés dans la partie (éliminés ou non)
    paramètre: cluedo le jeu de cluedo
    """
    return len(cluedo['listeJoueurs'])

def getNbJoueursActifs(cluedo):
    """
    retourne le nombre de joueurs engagés dans la partie qui ne sont pas éliminés
    paramètre: cluedo le jeu de cluedo
    """
    cpt = 0
    for joueurs in cluedo['listeJoueurs']:
        if not joueur.estElimine(joueurs):
            cpt +=1
    return cpt

def getJoueurPrincipal(cluedo):
    """
    retourne le joueur principal (c-à-d celui dont on voit le jeu)
    paramètre: cluedo le jeu de cluedo
    resultat: le joueur 
    """
    return joueurPrincipal(cluedo['listeJoueurs'])

def getNumTour(cluedo):
    """
    retourne le numéro du tour actuel
    paramètre: cluedo le jeu de cluedo
    resultat: le numéro du tour actuel 
    """
    return cluedo['numTour']

def getPlateau(cluedo):
    """
    retourne le plateau du cluedo
    paramètre: cluedo le jeu de cluedo
    resultat: le plateau associé au cluedo 
    """
    return cluedo['plateau']

def getJeuCartes(cluedo):
    """
    retourne le jeu de cartes du cluedo
    paramètre: cluedo le jeu de cluedo
    resultat: le jeu de cartes associé au cluedo 
    """
    return cluedo['jeuCarte']

def getListeJoueurs(cluedo):
    """
    retourne la liste desjoueurs participant à la partie de cluedo
    paramètre: cluedo le jeu de cluedo
    resultat: la liste des joueurs participant à la partie 
    """
    return cluedo['listeJoueurs']

def getNumPieceHypothese(cluedo):
    """
    retourne le numéro de la salle ou on dépose les hypothèse.
    paramètre: cluedo le jeu de cluedo
    resultat: la liste des joueurs participant à la partie 
    """
    return mystere.getSalle(getSolution(cluedo))
    
def incNumTour(cluedo):
    """
    ajoute 1 au numéro de tour et change le joueur courant.
    Attention il faut tenir compte des joueurs éliminés
    paramètre: cluedo le jeu de cluedo
    cette fonction ne retourne rien mais modifie le cluedo
    """
    trouver = False
    cluedo['numTour'] += 1
    indice = getIndiceJoueurCourant(cluedo)
    while not trouver:
        indice += 1
        if indice >= getNbJoueurs(cluedo):
            indice = 0
        nouveauJoueurCourant = cluedo['listeJoueurs'][indice]
        if not joueur.estElimine(nouveauJoueurCourant):
            trouver = True
            cluedo['joueurCourant'] = nouveauJoueurCourant

def elimineJoueurCourant(cluedo):
    """
    elimine le joueur courant
    paramètre: cluedo le jeu de cluedo
    cette fonction ne retourne rien mais modifie le cluedo
    """
    joueur.setElimine(getJoueurCourant(cluedo), True)
   
def distancePieces(cluedo,listePieces,listeDest):
    """
    retourne sous la forme d'un dictionnaire la case la plus proche de chacune des pièces
    paramètres: cluedo le jeu de cluedo
                listesPieces la liste des pièces du jeu
                listeDest une liste de coordonnées de case données sous la forme (lig,col)
    resultat: un dictionnaire dont les clés sont les numéros de pièce et les valeurs un triplé 
              (dist,lig,col) indiquant la case la plus proche de la pièce a les coordonnée lig,col
              qui se situe à une distance dist de la pièce
    """
    dico_distance_piece={}
    for pieces in listePieces:
        liste_entrees=piece.getListeEntrees(pieces)
        distance_min=None
        destination_bonne=None
        for (lignes,colonnes) in listeDest:
            for entrees in liste_entrees:
                distance=abs(entree.getLigne(entrees)-lignes)+abs(entree.getColonne(entrees)-colonnes)
                if distance_min==None or distance<distance_min:
                    distance_min=distance
                    destination_bonne=(lignes,colonnes)
            dico_distance_piece[piece.getNumPiece(pieces)]=(distance_min,destination_bonne[0],destination_bonne[1])
    return dico_distance_piece


def choixPieceOrdinateur(cluedo,distances):
    """
    retourne les coordonnées de la case choisie par le joueur ordinateur parmi une liste de destinations possibles
    paramètres: cluedo le jeu de cluedo
                distances un dictionnaire résultat de la fonction distancePieces
                          les clés sont les numéros des pièces et les valeur un triplet (dist,lig,col)
    résultat les coordonnées de la case choisie sous la forme (lig,col)
    """
    for (lig,col) in distances.values():
        return (lig,col)
        
def reponsePassageOrdinateur(cluedo,numP):
    """
    retourne la réponse d'un joueur ordinateur à la question souhaitez vous prendre le passage secret
    cette fonction peut être complètement aléatoire ou tenir compte d'une stratégie (voir les fonctions
    de la structure ficheIndices
    paramètres: cluedo le jeu de cluedo
               numP le numéro de la pièce destination
    résultat: 'O' ou 'N'
    """
    return (random.choice('O','N'))

def passageSecretJoueurCourant(cluedo):
    """
    retourne soit None si le joueur courant ne se trouve pas dans une pièce où il y a un passage secret
    soit un triplet numPieceDest,lig,col indiquant le numéro de la pièce destination du passage
    la postion du passage dans la pièce où se trouve le joueur courant
    paramètre: cluedo le jeu de cluedo
    """
    plato = getPlateau(cluedo)
    ligneu = plateau.posJoueur(plato,joueur.getNum(getJoueurCourant(cluedo)))[0]
    colonneu = plateau.posJoueur(plato,joueur.getNum(getJoueurCourant(cluedo)))[1]
    catCaseJCourant = plateau.getCategorieP(plato,ligneu,colonneu)
    if catCaseJCourant < 1 :
        return None
    else:
        for piaisse in plateau.getPieces(plato):
            if piaisse["num"] == catCaseJCourant:
                passaje = piece.getPassage(piaisse)
                return (passaje["pieceDestination"],passaje["pos"][0],passaje["pos"[1]])

def choixProfMatOrdinateur(cluedo,numPiece):
    """
    retourne sous la forme d'un couple numProf,numMat le choix du joueur courant géré par un ordinateur
    cette fonction se sert de la fonction creerUneHypothese de la structure ficheIndices
    paramètres: cluedo le jeu de cluedo
                numPiece le numéro de la pièce où se trouve le joueur courant
    résultat un couple numProf,numMat
    """
    ficheindices=joueur.getFiche(getJoueurCourant(cluedo))
    return creerUneHypothese(ficheindices,joueur.getNum(getJoueurCourant(cluedo)),numPiece)

def choixSolutionOrdinateur(cluedo):
    """
    retourne sous la forme d'une structure Mystere la solution proposée par le joueur courant géré par un ordinateur
    cette fonction se sert la fonction hypothesesSures de la structure ficheIndices
    paramètre: cluedo le jeu de cluedo
    résultat un mystere
    """
    res = {}
    FicCourant = joueur.getFiche(getJoueurCourant(cluedo))
    hypo = hypothesesSures(FicCourant)
    for (cat,carte) in hypo.items():
        if cat == 1:
            res['Prof'] = carte
        elif cat == 2:
            res['Matiere'] = carte
        else:
            res['Salle'] = carte
    return res

def demanderJoueurOrdinateur(cluedo,joueurInterroge,hypothese):
    """
    donne la réponse d'un joueur géré par l'ordinateur à une hypothèse proposée par le joueur courant
    cette fonction utilise la fonction reponseHypothese de joueur
    paramètres: cluedo          : le jeu de cluedo
                joueurInterroge : le joueur interrogé
                hypothese       : l'hypothèse formée par le joueur courant sous la forme d'une structure mystere
    résulat: None si le joueur interrogé ne possède aucune carte, sinon une des cartes que le joueur interrogé possède
    """
    return joueur.reponseHypothese(joueurInterroge,hypothese)
    
def jouerDe(cluedo):
    """
    lance les dés (c-à-d choisit aléatoirement un entier compris entre 2 et 12) puis calcule pour chaque pièce
    la distance à laquelle le joueur courant peut s'approcher en fonction des points obtenus sur les dés
    paramètres: cluedo          : le jeu de cluedo
    résultat: un couple de,distances où de est le nombre de points obtenus aux dés et distances est un dictionnaire
              dont les clés sont les numéros de pièce et les valeurs la distance à laquelle le joueur peut s'approcher 
              de la pièce grâce aux points obtenus aux dés (voir fonction distancePieces)
    """
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d = d1 + d2
    dico = {}
    liste=[]
    liste.append(plateau.posJoueur(getPlateau(cluedo), cluedo['joueurCourant']))
    print(plateau.posJoueur(getPlateau(cluedo), cluedo['joueurCourant']))
    listepiece=plateau.getPieces(getPlateau(cluedo))
    listepiece=listepiece.values()
    listdest=plateau.casesAccessibles(getPlateau(cluedo),liste,de)
    distance=distancePieces(cluedo, listepiece, listdest)
    for piece, valeurs in distance.items():
        dico[piece] = valeurs
    return (d, dico)


def deplacerJoueurCourant(cluedo,lig,col):
    """
    cette fonction modifie le plateau du cluedo en enlevant le pion du joueur courant de son emplacement actuel
    et le positionnant sur la case destination. Elle retourne de plus la catégorie de la case destination
    paramètres: cluedo          : le jeu de cluedo
                lig: le numéro de la ligne destination
                col: le numéro de la colonng destination
    resultat: catégorie de la case destination (numero de la pièce ou couloir)
    """ 
    joue_heure = getJoueurCourant(cluedo)
    plateau = getPlateau(cluedo)
    ligneu = plateau.posJoueur(plato,joueur.getNum(getJoueurCourant(cluedo)))[0]
    colonneu = plateau.posJoueur(plato,joueur.getNum(getJoueurCourant(cluedo)))[1]
    plateau.enleverPion(plateau,ligneu,colonneu)
    plateau.mettrePion(plateau,lig,col,joueur.getNum(joue_heure))
# ---------------------------------------------
# Fonction d'affichage
# ---------------------------------------------

def afficherCluedo(cluedo,information):
    """
    affiche la vue du cluedo c'est-à-dire le plateau ainsi que la fiche indice du joueur principal et le message d'information
    paramètres: cluedo le jeu de cluedo
                information le message à afficher avec le jeu
    """
    #print()
    joueurCourant=getJoueurCourant(cluedo)
    debutInformation="--------- Tours numéro "+str(getNumTour(cluedo))+"\n"+\
    "    c'est au joueur "+str(joueur.getNum(joueurCourant))+" appelé "+joueur.getNom(joueurCourant)+ " de jouer\n"
    plateau.afficherPlateau(getPlateau(cluedo),(debutInformation+information).split('\n'))
    print(ficheIndices.string(joueur.getFiche(getJoueurPrincipal(cluedo))))