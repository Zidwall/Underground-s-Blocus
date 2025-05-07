import pygame

import variable

screen = pygame.display.set_mode((1000, 800))
class Perso:
    def __init__(self):
        self.x = 30
        self.y = 594
        self.vitesse = 4
        self.largeur = 25
        self.hauteur = 38
        self.lancement = None
    def haut(self, varia:variable):
            if not varia.inversed_gravity:
                self.y -= self.vitesse
    def haut_world2(self):
        self.y -= 132
    def bas(self):
        self.y += self.vitesse
    def bas_world2(self):
            self.y += 132

    def droite(self):
        self.x += self.vitesse


    def gauche(self):
        self.x -= self.vitesse
        if self.x < -5:
            self.x += self.vitesse
    def initial(self):
        self.x = 30
        self.y = 594
        self.vitesse = 4
        self.largeur = 25
        self.hauteur = 38


    def nouvelles_dimensions_joueur(self):
        for loop in range(30):
            self.largeur -= 0.1
        for loop in range(30):
            self.hauteur -= 0.2
