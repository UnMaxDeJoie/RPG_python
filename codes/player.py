import pygame
from animation import AnimateSprite

class Player(AnimateSprite):        #Création de la classe Player

    def __init__(self, name, x, y):
        super().__init__(name)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey(0, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.bottom = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.previous_position = self.position.copy()

    def get(self):      #Donne la position de l'image de base lors de son spawn
        self.image = self.images["down"]
        self.image.set_colorkey(0, 0)
        return self.image

    def save_location(self):        #retien la position du joueur
        self.previous_position = self.position.copy()

    def move_up(self):          #fonction déplacement en haut
        self.position[1] -= self.player_speed

    def move_down(self):        #fonction déplacement en bas
        self.position[1] += self.player_speed

    def move_right(self):       #fonction déplacement à droite
        self.position[0] += self.player_speed

    def move_left(self):        #fonction déplacement à gauche
        self.position[0] -= self.player_speed

    def move_back(self):        #Fonction faisant revnir en avant le personnage si le personnage à une collision
        self.position = self.previous_position
        self.update()

    def update(self):
        self.rect.topleft = self.position
        self.bottom.midbottom = self.rect.midbottom