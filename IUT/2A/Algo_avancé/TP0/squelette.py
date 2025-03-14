#! /usr/bin/env python3

import pygame
import sys
import balle

global FPSCLOCK
FPS = 60
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
ARRIERE_PLAN = (42,17,51)
score = 0


b1 = balle.balle([400,300],1,45,(0,255,0))
b2 = balle.balle([100,500],2,20,(0,0,255))


class Quitte(Exception ):
    pass

def isQuitEvent(event):
    return (event.type == pygame.QUIT or 
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE))

def handleKey(event):
    print("appui sur la touche", event.key)

def handleClick(event):
    global score
    print("Clic à la position", event.pos)
    if b2.contient(event.pos) or b1.contient(event.pos):
        score+=1
        print(score)

def handleEvents():
    for event in pygame.event.get():
        # pour chaque évènement depuis le dernier appel de cette fonction
        if isQuitEvent(event):
            raise Quitte
        elif event.type == pygame.KEYDOWN:
            handleKey(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handleClick(event)

def refresh(s):
    s.fill(ARRIERE_PLAN)

def drawApp(s, t):
    """
    Redessine l'écran. 't' est le temps écoulé depuis l'image précédente.
    """
    #x = int(0.09*t) % WINDOWWIDTH
    #y = int(0.15*t) % WINDOWHEIGHT
    refresh(s)
    b1.dessine(s)
    b2.dessine(s)
    
    b1.avance(t)
    b2.avance(t)
    #pygame.draw.circle(s, (255,0,0), (x,y), 300)

    font = pygame.font.SysFont("comicsansms", 72)
    msg_score = font.render("Score : "+str(score),True,(255,255,255))
    s.blit(msg_score,(0,0))

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
