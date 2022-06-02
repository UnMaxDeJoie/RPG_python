import pygame

class AnimateSprite(pygame.sprite.Sprite):      #creation classe AnimateSprite

    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'../sprites/{name}.png') #permet d'obtenir le png de l'image choisit
        self.animation_index = 0
        self.timer = 0
        self.images_sprites = {                 #création du dictionnaire images
            "down": self.get_images(0),
            "right": self.get_images(22),
            "up": self.get_images(44),
            "left": self.get_images(66)
        }
        self.player_speed = 2

    def get_image(self, x, y):
        image = pygame.Surface([16, 22])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 22))
        return image

    def get_images(self, y):    #permet de donner l'image à la bonne position
        images = []

        for i in range(0, 3):
            x = i*16
            image = self.get_image(x, y)
            images.append(image)
        return images

    def change_animation(self, name):       #fonction changement animation
        self.image = self.images_sprites[name][self.animation_index]
        self.image.set_colorkey(0, 0)
        self.timer += self.player_speed * 8
        if self.timer >= 100:   #permet que la vitesse de changement de sprite ne soit pas trop rapide

            self.animation_index += 1
            if self.animation_index >= len(self.images_sprites[name]):
                self.animation_index = 0
            self.timer = 0