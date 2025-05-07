import random

class Rect:
    def __init__(self):
        self.giant_ecart = 710
        self.x = 1300
        self.y1 = 650
        self.y2 = -60
        self.largeur = 250
        self.hauteur1 = 530
        self.hauteur_bonus = 328
        self.hauteur2 = 640
        self.speed = 3
        self.red = 255
        self.blue = 255
        self.green = 255
    def MoveRect(self):
        self.y1 = random.randint(280, 640)
        self.x = 1300
        self.red = 0
        self.green = 0
        self.blue = 0
        self.giant_ecart -= 1
    def initial(self):
        self.x = 1300
        self.y1 = 650
        self.y2 = -60
        self.red = 255
        self.blue = 255
        self.green = 255
        self.speed = 3
        self.giant_ecart = 710

