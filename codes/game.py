from map import *
from player import Player

class Game:  #Création de la classe Game

    def __init__(self):  #

        self.screen = pygame.display.set_mode((1440, 864))   # Affichage de la fenêtre
        pygame.display.set_caption("Projet RPG")

        self.player = Player("character1", 0, 0)            # Générer le joueur
        self.map_manager = MapManager(self.screen, self.player)

    def handle_input(self):                     #fonction des touches
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:                    #si fleche du haut presser
            self.player.move_up()                   #fonction move_up (voir player.py)
            self.player.change_animation("up")      #fonction change_animation (voir animation.py)
        elif pressed[pygame.K_DOWN]:                #etc
            self.player.move_down()
            self.player.change_animation("down")
        elif pressed[pygame.K_RIGHT]:               #etc
            self.player.move_right()
            self.player.change_animation("right")
        elif pressed[pygame.K_LEFT]:                #etc
            self.player.move_left()
            self.player.change_animation("left")   

    def update(self):                   #fonction rafraichisssant pour changer ce qui se passe à l'écran
        self.map_manager.update()

    def run(self):                      #fonction lançant la boucle du jeu
        clock = pygame.time.Clock()     #crée un timer

        running = True                  #variable pour mettre fin à la boucle

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            clock.tick(60)
