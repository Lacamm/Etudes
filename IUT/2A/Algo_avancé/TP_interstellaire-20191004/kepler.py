#! /usr/bin/env python3

import pygame
import sys
import json
from planete import Planete
from vaisseau import Vaisseau

global FPSCLOCK
FPS = 120
WINDOWWIDTH = 1800
WINDOWHEIGHT = 1600
ARRIERE_PLAN = (42,17,51)


class Quitte(Exception ):
    pass

def isQuitEvent(event):
    return (event.type == pygame.QUIT or 
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE))

def handleKey(event):
    print("appui sur la touche", event.key)

def handleClick(event):
    print("Clic à la position", event.pos)

def handleEvents():
    for event in pygame.event.get():
        # pour chaque évènement depuis le dernier appel de cette fonction
        if isQuitEvent(event):
            raise Quitte
        elif event.type == pygame.KEYDOWN:
            handleKey(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("clic")

def drawApp(s_temp, s_pers, ecran, univers):
    """
    Redessine l'écran.
    """
    s_temp.fill((0,0,0,0)) # on remplit avec du transparent
    for objet in univers:
        objet.dessine(s_pers, s_temp)
    ecran.fill(ARRIERE_PLAN)
    ecran.blit(s_pers, (0,0))
    ecran.blit(s_temp, (0,0))
    pygame.display.update()
    
def main():
    temps = 0
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Space Oddity')
    info = pygame.display.Info()
    WINDOWWIDTH, WINDOWHEIGHT = info.current_w,info.current_h
    ecran = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    s_pers = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT), pygame.SRCALPHA)
    s_temp = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT), pygame.SRCALPHA)

    # etoile = Planete(30, 0, (WINDOWWIDTH/2,WINDOWHEIGHT/2), 0, (255, 255, 255))
    # pVert = Planete(20, 100, (0,0), 30, (0,255,0))
    # pRouge = Planete(pVert.taille*2, 100,(WINDOWWIDTH/2,WINDOWHEIGHT/2), pVert.v_angulaire/2,(255,0,0))
    # pFushia = Planete(20, 100, (WINDOWWIDTH,0), 30, (255,0,255), False, 90)
    
    #univers = [etoile, pVert, pRouge, pFushia]

    etoile = Planete(30, 0, (WINDOWWIDTH/2,WINDOWHEIGHT/2), 0, (255, 255, 255))
    planete = etoile.add_satellite(30, 200, 3.01, (22,45,123))
    planete2 = etoile.add_satellite(30, 500, 1.51, (22, 245,123))
    lune1 = planete.add_satellite(20, 70, -12, (223,45,76))
    lune2 = planete.add_satellite(10, 100, 10, (223,45,76))
    lune3 = planete2.add_satellite(10, 100, 10.01, (223,145,76), True)
    sonde = lune2.add_satellite(3, 12, 50.01, (255, 255, 76), True)
    sonde2 = lune3.add_satellite(3, 12, 50.01, (255, 255, 76), True)

    v1 = Vaisseau((10,10), [planete,planete2, lune1], (255,255,255), False, "tardis.png")
    v2 = Vaisseau((20,20), etoile.parcours_prefixe(), (255,0,255))
    v3 = Vaisseau((30,30), etoile.parcours_postfixe(), (0,0,255))
    v3 = Vaisseau((40,40), etoile.parcours_largeur(), (0,255,255))

    univers = [etoile, v3]
    
    ecran.fill(ARRIERE_PLAN)

    while True:  #boucle principale
        try:
            handleEvents()
            drawApp(s_temp, s_pers, ecran, univers)

            temps_ecoule = FPSCLOCK.tick(FPS)
            for objet in univers:
                objet.avance(temps_ecoule)

        except Quitte:
            break
            
    pygame.quit()
    sys.exit(0)

main()
(WINDOWWIDTH/2,WINDOWHEIGHT/2)