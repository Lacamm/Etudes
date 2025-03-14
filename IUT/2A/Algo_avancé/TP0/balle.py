import pygame

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

class balle(object):

    def __init__(self,position,vitesse,taille,couleur):
        self.position = position #liste
        self.vitesse = vitesse #int
        self.taille = taille #int
        self.couleur = couleur #tuple

    def avance(self, t):
        self.position[0] = int( self.position[0] + self.vitesse*t/2000) % WINDOWWIDTH
        self.position[1] = int( self.position[1] + self.vitesse*t/2000) % WINDOWHEIGHT
    
    def dessine(self,s):
        pygame.draw.circle(s, self.couleur, (self.position[0],self.position[1]), self.taille)
    
    def contient(self, position):
        return (position[0] >= self.position[0]-self.taille and position[0] <= self.position[0]+self.taille) and (position[1] >= self.position[1]-self.taille and position[1] <= self.position[1]+self.taille)

