# -*- coding: utf-8 -*-
"""
                           Projet CLUED'IUTO 
        Projet Python 2018 de 1ere année DUT Informatique Orléans
        
   Module plateau.py
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu c'est à dire l'endroit où les joueurs
   vont se déplacer. Le plateau sera implémenté à partir d'une matrice de case et va gérer une liste de pièces
"""
import matrice
import case
import piece
import entree
import ansiColor


#-----------------------------------------
# contructeur 
#-----------------------------------------

def Plateau(nbLig,nbCol):
    """
    créer un plateau de nbLig sur nbCol cases vides avec une liste de pièces vide
    paramètres: nbLig et nbCol deux entiers strictement positifs
    """
    return [matrice.Matrice(nbLig,nbCol,0),dict()]

#-----------------------------------------
# accesseurs 
#-----------------------------------------

def getNbLignesP(plateau):
    """
    retourne le nombre de lignes du plateau
    paramètre: plateau le plateau considéré
    """
    return matrice.getNbLignes(plateau[0])
        
def getNbColonnesP(plateau):
    """
    retourne le nombre de colonnes du plateau
    paramètre: plateau le plateau considéré
    """
    return matrice.getNbColonnes(plateau[0])

def getCase(plateau,ligne,colonne):
    """
    retourne la case se trouve en (ligne,colonne) dans le plateau
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice.getVal(plateau[0],ligne,colonne)

def getPieces(plateau):
    """
    retourne la dictionnaire des pièces d'un plateau
    paramètre: plateau le plateau considéré
    """
    return plateau[1]

def getCategorieP(plateau,ligne,colonne):
    """
    retourne la catégorie de la case qui se trouve en (ligne,colonne) dans le plateau
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return case.getCategorie(getCase(plateau,ligne,colonne))

def getContenuP(plateau,ligne,colonne):
    """
    retourne le contenu de la case qui se trouve en (ligne,colonne) dans le plateau
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return case.getContenu(getCase(plateau,ligne,colonne))

def getPassageSecret(plateau,ligne,colonne):
    """
    retourne le numéro de la pièce accessible via un passage secret si on est en position ligne,colonne.
    retourn None s'il n'y a pas de passage secret
    paramètres: plateau le plateau considéré
                ligne la ligne de la case
                colonne la colonne de la case
    cette fonction retourne None ou un numéro de pièce
    """
    res = None
    for Piece in getPieces(plateau):
        if piece.estPassage(Piece,ligne,colonne) != 0:
            res = piece.getNumPiece(Piece)
    return res

#-------------------------
# setters et modificateurs
#-------------------------

def setCase(plateau,ligne,colonne,categorie):
    """
    met une case de type categorie en (ligne,colonne) du plateau (cette case ne contiendra pas de pion)
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                categorie le type de case souhaitée pour cette position
    cette fonction ne retourne rien mais modifie le plateau
    """
    matrice.setVal(plateau[0],ligne,colonne,case.Case(categorie,None))
    
def setPieces(plateau,lesPieces):
    """
    affecte une liste de pièces à un plateau
    paramètres: plateau le plateau considéré
                lesPieces sous la forme d'un dictionnaire dont les clé sont les numéro de pièce et les valeur les pièces elles-même
    cette fonction ne retourne rien mais modifie le plateau
    """
    plateau[1] = lesPieces
    
def enleverPion(plateau,ligne,colonne):
    """
    enlève le pion qui se trouve sur la case considérée du plateau et retourne ce pion
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0
    résultat: un entier indiquant pion qui se trouvait sur la case
    """
    casePion = getCase(plateau,ligne,colonne)
    joueur = case.getContenu(casePion)
    case.setContenu(casePion,None)
    return joueur

def mettrePion(plateau,ligne,colonne,pion):
    """
    met un pion sur la case se trouvant en (ligne,colonne) du plateau. Si case contenait un pion celui-ci sera écrasé
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                pion un entier représentant le pion à mettre
    cette fonction ne retourne rien mais modifie le plateau
    """
    case.setContenu(getCase(plateau,ligne,colonne),pion)

def poserPionCaseDepart(plateau,listeNumJoueur):
    """
    Positionne les pions des joueur sur leur case départ.
    paramètres: plateau le plateau considéré
                listeNumJoueur la liste desnumeros des joueurs participant à la partie
    cette fonction ne retourne rien mais modifie le plateau
    """
    for lig in range(getNbLignesP(plateau)):
        for col in range(getNbColonnesP(plateau)):
            joueur = getCase(plateau,lig,col)
            depart_joueur = -case.estDepart(joueur)
            if depart_joueur in listeNumJoueur:
                case.setContenu(joueur,depart_joueur)

def posJoueur(plateau,numJoueur):
    """
    retourne la position du joueur qui porte le numéro numJoueur sous la forme d'un couple(lig,col)
    paramètres: plateau le plateau considéré
                numJoueur un entier strictement positif
    résultat: un couple (lig,col) donnant la position du joueur numJoueur sur le plateau ou 
              None si le joueur n'est pas sur le plateau
    """
    pos = None
    for lig in range(getNbLignesP(plateau)):
        for col in range(getNbColonnesP(plateau)):
            joueur = getCase(plateau,lig,col)
            if case.getContenu(joueur) == numJoueur:
                pos = (lig,col)
    return pos

def estEntreePiece(plateau,ligne,colonne):
    """
    Permet de savoir si une case est l'entrée d'une pièce ou non.
    paramètres: plateau le plateau considéré
                ligne la ligne de la case
                colonne la colonne de la case
    cette fonction retourne un booléen
    """
    for Piece in getPieces(plateau):
        if piece.estEntree(Piece,ligne,colonne):
            return True
    return False

def estPassageSecret(plateau,ligne,colonne):
    """
    Permet de savoir si une case est un passage secret ou non.
    paramètres: plateau le plateau considéré
                ligne la ligne de la case
                colonne la colonne de la case
    cette fonction retourne un booléen
    """
    return (getPassageSecret(plateau,ligne,colonne) != None)

def passageNord(plateau,ligne,colonne):
    """
    teste si on peut passer de la case  à la case adjacente vers le nord
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    résultat: un booléen indiquant si le passage est possible ou non
    """
    return (ligne - 1 >= 0 and case.estLibre(getCase(plateau,ligne-1,colonne)))

def passageSud(plateau,ligne,colonne):
    """
    teste si on peut passer de la case  à la case adjacente vers le sud
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    résultat: un booléen indiquant si le passage est possible ou non
    """
    return (ligne + 1 >= 0 and case.estLibre(getCase(plateau,ligne+1,colonne)))

def passageEst(plateau,ligne,colonne):
    """
    teste si on peut passer de la case  à la case adjacente vers l'est
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    résultat: un booléen indiquant si le passage est possible ou non
    """
    return (colonne - 1 >= 0 and case.estLibre(getCase(plateau,ligne,colonne+1)))

def passageOuest(plateau,ligne,colonne):
    """
    teste si on peut passer de la case  à la case adjacente vers l'ouest
    paramètres: plateau le plateau considéré
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    résultat: un booléen indiquant si le passage est possible ou non
    """
    return (colonne + 1 >= 0 and case.estLibre(getCase(plateau,ligne,colonne-1)))

def marquageDirect(plateau,calque,ancienneVal,nouvelleVal):
    """
    permet de marquer avec nouvelleVal les cases non marquées adjacentes à
    une case marquée par ancienneVal
    paramètres: plateau le plateau considéré
                calque une matrice de la même dimension que le plateau et qui porte le marquage
                ancienneVal la valeur de marquage recherchée
                nouvelleVal la valeur utilisée pour marquer les nouvelle case
    cette fonction ne retourne rien mais modifie le claque
    """
    ligneMax = getNbLignes(plateau)
    colonneMax = getNbColonnes(plateau)
    for lig in range(ligneMax):
        for col in range(colonneMax):
            couloir = case.getCategorie(getCase(plateau,lig,col)) == 0
            pasMarque = matrice.getVal(calque,lig,col) != nouvelleVal
            if couloir and pasMarque:
                if ligne >0 and matrice.getVal(calque,ligne-1,colonne)== ancienneVal:
                    matrice.setVal(calque,ligne,colonne,nouvelleVal)
                elif ligne<matrice.getNbLignes(calque)-1 and matrice.getVal(calque, ligne+1,colonne)== ancienneVal:
                    matrice.setVal(calque,ligne,colonne,nouvelleVal)
                elif colonne>0 and matrice.getVal(calque,ligne,colonne-1)==ancienneVal:
                    matrice.setVal(calque,ligne,colonne,nouvelleVal)
                elif colonne<matrice.getNbColonnes(calque)-1 and matrice.getVal(calque,ligne,colonne+1)==ancienneVal:
                    matrice.setVal(calque,ligne,colonne,nouvelleVal)

def casesAccessibles(plateau,listeDepart,distance):
    """
    retourne la liste des cases accessibles sous la forme de liste de couples 
    de coordonnées (lig,col)
    paramètres: plateau le plateau considéré
                listeDepart: une liste de couples (lig,col) indiquant les points de départ de la recherche
                distance: un entier positif indiquant de combien de cases on a le droit de se déplacer
    résultat: la liste des case atteignable à partir d'un des départs en utilisant moins de distance déplacements
    """
    accessibles = set()
    Lignes = getNbLignesP(plateau)
    Colonnes = getNbColonnesP(plateau)
    for depart in listeDepart:
        calque = matrice.Matrice(Lignes,Colonnes,0)
        for dist in range(distance):
            modif=marquageDirect(plateau, calque, dist, dist+1)
        for ligne in range(Lignes):
            for colonne in range(Colonnes):
                dist = getVal(calque,ligne,colonne)
                if dist%2==distance%2:
                    accessibles.add((ligne, colonne))
    return accessibles
        

def distancePieces(plateau,lig,col):
    """
    retourne un dictionnaire dont les clés sont les identifiant des pièces et les valeurs la distance
    a parcourir pour atteindre la pièce à partir de la case de coordonnées (lig,col)
    paramètres: plateau le plateau considéré
                lig: le numéro de la ligne de la case considérée
                col: le numéro de la colonne de la case considérée
    résultat: le dictionnaire décrit plus haut
    """
    dico = {}
    test=getPieces(plateau)
    for pieces in test.values():
        print(piece)
        for entrees in piece.getListeEntrees(pieces):
            valIntermediaire = (abs(lig-entree.getLigne(entrees)),abs(col-entree.getColonne(entrees)))
            dico["piece"] = dico.get("piece",valIntermediaire)
            if dico["piece"][0] > valIntermediaire[0] and dico["piece"][1] > valIntermediaire[1]:
                dico["piece"] = valIntermediaire
    return dico

def accessiblesJoueur(plateau,numJoueur,distance):
    """
    retourne une liste de couple (lig,col) indiquant les cases accessibles pour le joueur numJoueur
    à la distance
    paramètres: plateau le plateau considéré
                numJoueur un entier strictement positif
                distance  un entier strictement positif indiquant la distance maximale
    résultat: la liste des positions accessible par le joueur
    """
    ligne = 0
    colonne = 0
    nbLignes = getNbLignesP(plateau)
    nbColonnes = getNbColonnesP(plateau)
    contenu = None
    while contenu != numJoueur and ligne < nbLignes:
        ligne += 1
        while contenu != numJoueur and colonne < nbColonnes:
            contenu = getContenuP(plateau, ligne, colonne)
            colonne += 1
    position_joueur = (ligne, colonne)
    accessibles_joueur = casesAccessibles(plateau, [position_joueur], distance)
    return accessibles_joueur

# ----------------------------------------------------
# chargement d'un plateau à partir d'un fichier texte
# et affichage en mode texte d'un plateau
# ----------------------------------------------------

def traiterCase(laCase,lig,col,plateau,pieces):
    if laCase=='':
        setCase(plateau,lig,col,None)
    else:
        contenu=laCase.split(";")
        sorte=int(contenu[0])
        setCase(plateau,lig,col,sorte)
        if sorte>0 and sorte not in pieces:
            pieces[sorte]=piece.Piece(sorte)
        if len(contenu)>1:
            if contenu[1]=='P':
                piece.setPassage(pieces[sorte],int(contenu[2]),lig,col)
            elif contenu[1]=='N':
                piece.addEntree(pieces[sorte],entree.Entree(entree.NORD,lig,col))
            elif contenu[1]=='E':
                piece.addEntree(pieces[sorte],entree.Entree(entree.EST,lig,col))
            elif contenu[1]=='S':
                piece.addEntree(pieces[sorte],entree.Entree(entree.SUD,lig,col))
            elif contenu[1]=='O':
                piece.addEntree(pieces[sorte],entree.Entree(entree.OUEST,lig,col))
            elif contenu[1]=='J':
                if sorte>1:
                    piece.addJoueur(pieces[sorte],int(contenu[2]))
                else:
                    mettrePion(plateau,lig,col,int(contenu[2]))
                
def lirePlateau(nomFichier):
    texte=""
    try:
        fic=open(nomFichier)
        texte=fic.read()
        fic.close()
    except:
        print("probleme de lecture du fichier")
        return None
    lignes=texte.split("\n")
    nbLignes=len(lignes)
    if nbLignes==0:
        return None
    
    nbColonnes=len(lignes[0].split(","))
    plateau=Plateau(nbLignes-1,nbColonnes)
    lig=0
    lesPieces={}
    for ligne in lignes[:-1]:
        cases=ligne.split(",")
        col=0
        for c in cases:
            traiterCase(c,lig,col,plateau,lesPieces)
            col+=1
        lig+=1
    setPieces(plateau,lesPieces)
    return plateau



def afficherPlateau(plateau,information=[],decalage=8,debutInfo=3):
    joueurPiece={}
    pieceIdentifiees={}
    sortePrec=0
    for lig in range(getNbLignesP(plateau)):
        print(' '*decalage,sep='',end='')
        for col in range(getNbColonnesP(plateau)):
            c=getCase(plateau,lig,col)
            sorte=case.getCategorie(c)
            if sorte==None:
                print(' ',sep='',end='')
            elif sorte<=0:
                couleurF=ansiColor.GRIS+60
                pion=case.getContenu(c)
                if pion==None:
                    if sorte<0:
                        car='X'
                        couleurT=-sorte
                    else:
                        car=' '
                        couleurT=ansiColor.NORMAL
                else:
                    car='@'
                    couleurT=pion+ansiColor.CLAIR
                ansiColor.pcouleur(car,couleurT,couleurF,ansiColor.GRAS)
            else:
                if sorte not in pieceIdentifiees:
                    pieceIdentifiees[sorte]=[1,1]
                elif sorte==sortePrec:
                    pieceIdentifiees[sorte][1]+=1
                else:
                    pieceIdentifiees[sorte][0]+=1
                    pieceIdentifiees[sorte][1]=1               
                couleurF=sorte%7+sorte//7
                couleurT=ansiColor.NORMAL
                if piece.estEntree(getPieces(plateau)[sorte],lig,col):
                    car='/'
                else:
                    dest=piece.estPassage(getPieces(plateau)[sorte],lig,col)
                    if dest!=0:
                        car='P'
                        couleurT=dest%7+dest//7
                    else:
                        if sorte not in joueurPiece:
                            joueurPiece[sorte]=0
                        listeJoueur=piece.getContenu(getPieces(plateau)[sorte])
                        if joueurPiece[sorte]<len(listeJoueur):
                            couleurT=listeJoueur[joueurPiece[sorte]]+ansiColor.CLAIR
                            car='@'
                            joueurPiece[sorte]+=1
                        else:
                            if pieceIdentifiees[sorte]==[3,3]:
                                car=str(sorte%10)
                            else:
                                car=' '                            
                            couleurT=ansiColor.NORMAL
                ansiColor.pcouleur(car,couleurT,couleurF)
            sortePrec=sorte
        if lig>=debutInfo and lig<debutInfo+len(information):
            print('  ',information[lig-debutInfo])
        else:
            print()
