#! /usr/bin/env python3

import pygame
import sys

global FPSCLOCK
FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
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

def refresh(s):
    s.fill(ARRIERE_PLAN)

def drawApp(s, t):
    """
    Redessine l'écran. 't' est le temps écoulé depuis l'image précédente.
    """
    x = int(0.09*t) % WINDOWWIDTH
    y = int(0.15*t) % WINDOWHEIGHT
    refresh(s)
    pygame.draw.circle(s, (123,234,222), (x,y), 50)

def main():
    temps = 0
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Carre blanc sur fond blanc')
    ecran = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    refresh(ecran)

    while True:  #boucle principale
        try:
            handleEvents()
            drawApp(ecran, temps)
            pygame.display.update()
            
            temps_ecoule = FPSCLOCK.tick(FPS)
            temps += temps_ecoule
        except Quitte:
            break

            
    pygame.quit()
    sys.exit(0)

main()
