#-*-coding:utf8-*-

import pygame
import traceback
from pygame.locals import *
from math import *
from random import randrange


def pos():
    """Fonction qui va calculer toutes les position du canon"""
    g=41         #nbr de positions
    liste_des_coo=[0]*g  #liste qui va contenir toutes les positions de la partie supérieure du canon
    for i in range (g):
        x=200+i*5   #position en abscisse
        z=abs(300-x)   #calcul pour la différence entre les abscisse des extrémités du cannon
        v=int(((((160**2)-(z**2))**(1/2))*2)//2) #calcul pour avoir l'ordonnée à  partir du bas
        y=600-v #avoir l'ordonnée à  partir du cadre supérieur
        liste_des_coo[i]=[x,y]  #stocker les positions
    return liste_des_coo


def drawline_balle(p,n):
    """fonction qui va permetre de dessiner le canon et le projectile à la position voulu"""
    coo=pos()    #récupère la liste des positions
    pygame.draw.line(fenetre, (0,0,0), [300,600], coo[p], 1)    #dessine le canon
    x=200+p*5    #l'abscisse de l'extrémité supérieure
    z=abs(300-x)   #calcul pour la différence entre les abscisses des extrémités du canon
    v=int(((((160**2)-(z**2))**(1/2))*2)//2) #calcul pour avoir l'ordonnée à  partir du bas
    y=600-v #avoir l'ordonnée à  partir du cadre suppérieur
    rectangle_bulle=pygame.Rect(x-20,y-20,40,40)  #créé un carré pour le projectile dont le centre est
                                            #l'extrémité supérieure
    fenetre.blit(liste_balle[n],rectangle_bulle)      #colle le projectile sur le carré
    return rectangle_bulle




def Affich_bulle():
    """Fonction qui va permetre d'afficher les bulles"""

    for i in range(len(liste_rectangle)):


        fenetre.blit(liste_balle[liste_couleur_bulle[i]],liste_rectangle[i])


def sorti(rectangle_bulle):
    """Fonction qui va détecter si la bulle sort de la fenêtre"""
    q=0  #variable qui détecte la sortie
    if rectangle_bulle.left <= 0 or rectangle_bulle.left >= 560: #test pour la sortie
        q=1
    return q

def incli(p):
    """Fonction qui va "calculer" l'inclinaison du canon"""
    x_ext=200+p*5   #position en abscisse de l'extrémité supérieure
    z=abs(300-x_ext)   #calcul pour la différence entre les abscisse des extrémités du canon
    v=int(((((160**2)-(z**2))**(1/2))*2)//2) #calcul pour avoir l'ordonnée à  partir du bas
    y_ext=600-v #avoir l'ordonnée à  partir du cadre supérieur
    x_int=300 #coordonnées de l'extrémité inférieure
    y_int=600
    delta_x=x_int-x_ext #différence entre les coordonées inférieures et supérieures
    delta_y=y_int-y_ext
    ord=abs(delta_y/delta_x) #coefficient directeur du canon
    dy=-ord     #direction du projectile en ordonnée
    return dy


def dep_x(p):
    """Fonction qui va diriger le projectile en abscisse"""
    x_ext=200+p*5
    x_int=300
    delta_x=x_int-x_ext #différence entre l'abscisse de l'extrémité supérieure et inférieure
    if delta_x<0: #test pour voir si le canon est orienté a gauche
        x=1
    if delta_x>0: #test pour voir si le canon est orienté a droite
        x=-1
    return x


def deplacement_bulle(p,rectangle_bulle,n,coo,liste_rectangle,win):
    """Fonction qui va deplacer le projectile"""
    a=-1
    continuer=1
    loose=0
    if p==20: #test pour voir si le canon est à la verticale
        while a==-1 and rectangle_bulle.top>=0:
            rectangle_bulle=rectangle_bulle.move(0,-1) #déplace le carré du projectile
            a=rectangle_bulle.collidelist(liste_rectangle)
            pygame.display.flip() #raffraichi la fenêtre
            fenetre.fill((100,200,255)) #effacer le fond
            fenetre.blit(liste_balle[n],rectangle_bulle) #recolle le projectile dans le carré
            pygame.draw.line(fenetre, (0,0,0), [300,600], coo[p], 1) #refaire le trait
            Affich_bulle() #réafficher les bulles
            pygame.display.flip() #raffraichi la fenêtre
        if r_bulle.bottom>=360:     #teste si la bulle atteint le domaine où se trouve le canon
            loose=1
        if l_n[a]==n:       #teste si la couleur du projectile est identique à celle de la bulle
            liste_rectangle[a]=rectangle_impossible     #déplace le projectile et la bulle en question au coordonné du rectangle impossible
            win=win-1       #retire un point du compteur
            print("win=",win)   #affiche le compteur de bulles restantes
        else:
            if loose==1:        #test qui affiche l'écran de défaite
                chaine="LOOSE"
                font=pygame.font.SysFont("broadway",48,bold=False,italic=False)
                text=font.render(chaine,1,(255,0,0))
                fenetre.fill((0,0,0))
                fenetre.blit(text,(230,250))
                pygame.display.flip()
                pygame.time.delay(5000)
                continuer=0
            else:
                liste_rectangle.append(rectangle_bulle) #ajoute le projectile à la liste des bulles
                liste_couleur_bulle.append(n)       #ajoute la couleur du projectile à celle 
                win=win+1           #ajoute un point au compteur
                print("win=",win)
    else:
        y=incli(p)
        x=dep_x(p)
        t=abs(20-p)
        time=21-t
        while a==-1 and rectangle_bulle.top>=0:
            coo=pos()
            fenetre.fill((100,200,255))
            q=sorti(rectangle_bulle)
            if q==0: #test pour voir si la bulle est encore dans le cadre
                rectangle_bulle=rectangle_bulle.move(x,y)
            if q==1: #test pour avoir si le projectile est sorti
                rectangle_bulle=rectangle_bulle.move(-x,y)
                x=-x
            fenetre.blit(liste_balle[n],rectangle_bulle)
            pygame.draw.line(fenetre, (0,0,0), [300,600], coo[p], 1)
            Affich_bulle()
            a=rectangle_bulle.collidelist(liste_rectangle)
            pygame.display.flip()
            pygame.time.delay(time)
        if r_bulle.bottom>=360:
            loose=1
        if liste_couleur_bulle[a]==n:
            liste_rectangle[a]=rectangle_impossible
            win=win-1
            print("win=",win)
        else:
            if loose==1:
                chaine="LOOSE"
                font=pygame.font.SysFont("broadway",48,bold=False,italic=False)
                text=font.render(chaine,1,(255,0,0))
                fenetre.fill((0,0,0))
                fenetre.blit(text,(230,250))
                pygame.display.flip()
                pygame.time.delay(5000)
                continuer=0
            else:
                liste_rectangle.append(rectangle_bulle)
                liste_couleur_bulle.append(n)
                win=win+1
                print("win=",win)

    if win==0:      #teste qui affiche l'écran de victoire
        chaine="WIN"
        font=pygame.font.SysFont("broadway",48,bold=False,italic=False)
        text=font.render(chaine,1,(128,128,0))
        fenetre.fill((100,200,255))
        fenetre.blit(text,(250,250))
        pygame.display.flip()
        pygame.time.delay(5000)
        continuer=0
    return win,continuer

pygame.init()
try:
    l=[(255,0,0),(0,255,0),(0,0,255)]   #liste contenant 3 couleurs: rouge,bleu et vert
    fenetre=pygame.display.set_mode((600,600)) #crée la fenetre
    fenetre.fill((100,200,255)) #colore le fond de la fenetre
    fenetre.blit
    pygame.key.set_repeat(100,30)  #Permet la répetition de la touche
    continuer=1 #varible qui sert a voir si l'on quitte le jeu ou non
    coo=pos() #faire la liste des position du canon
    p=20 #initialise la position au mileu
    win=15       #initialise le compteur de bulle à 15
    liste_balle=[0]*3 #liste qui va contenir les 3 type de projectiles
    for i in range (3): #boucle qui crée les projectiles
        balle=pygame.Surface((40,40))
        balle.fill((100,200,255))
        pygame.draw.circle(balle, l[i], [20,20], 20)
        liste_balle[i]=balle
    liste_couleur_bulle=[]
    for i in range (15):
        n=randrange(3)
        liste_couleur_bulle.append(n)   #ajoute la couleur générée dans une liste
    liste_rectangle=[]
    for i in range (15):
        rectangle=pygame.Rect(0+40*i,0,40,40)
        liste_rectangle.append(rectangle)   #ajoute le rectangle créé dans la liste contenant les rectangles
    rectangle_impossible=pygame.Rect(-900,-200,40,40)    #crée un rectangle hors de la fenêtre
    Affich_bulle() #afficher les bulles
    n=randrange(3) #choisir aléatoirement un des projectiles
    rectangle_bulle=drawline_balle(p,n)  #afficher le canon et le projectile
    while continuer:
        for event in pygame.event.get():
            if event.type==QUIT: #test pour voir si l'on veut quitter la fenetre
                continuer=0
            if event.type==KEYDOWN: #test si l'on appuie sur une touche
                if event.key==K_RIGHT: #déplacement vers la droite du canon
                    if p<40:
                        p=p+1
                        fenetre.fill((100,200,255))
                        rectangle_bulle=drawline_balle(p,n)
                        Affich_bulle()      #affiche les bulles
                if event.key==K_LEFT: #déplacement vers la gauche du canon
                    if p>0:
                        p=p-1
                        fenetre.fill((100,200,255))
                        rectangle_bulle=drawline_balle(p,n)
                        Affich_bulle()      #affiche les bulles
                if event.key==K_SPACE: #envoi de la balle
                    win,continuer=deplacement_bulle(p,rectangle_bulle,n,coo,liste_rectangle,win)
                    if continuer==1:
                        n=randrange(3) #rechoisi aleatoirement un projectile
                        rectangle_bulle=drawline_balle(p,n) #réaffiche le canon avec le nouveau projectile
                        Affich_bulle()      #affiche les bulles
            pygame.display.flip()


except:
   traceback.print_exc()

finally:
    pygame.quit()
    exit()