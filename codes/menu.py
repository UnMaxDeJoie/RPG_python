import pygame, sys
from game import Game
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Projet RPG')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)
button_quitter = pygame.Rect(50, 100, 200, 50)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        draw_text('button game', font, (255, 255, 255), screen, 20, 80)
        draw_text('button options', font, (255, 255, 255), screen, 20, 180)
        draw_text('button new_game', font, (255, 255, 255), screen, 20, 280)
        draw_text('button load_game', font, (255, 255, 255), screen, 20, 380)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        button_4 = pygame.Rect(50, 400, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                jeu = Game()
                jeu.run()

        if button_2.collidepoint((mx, my)):
            if click:
                options()

        if button_3.collidepoint((mx, my)):
            if click:
                new_game()

        if button_4.collidepoint((mx, my)):
            if click:
                load_game()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 40, 43), button_2)
        pygame.draw.rect(screen, (150, 75, 0), button_3)
        pygame.draw.rect(screen, (150, 100, 75), button_4)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def new_game():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('new_game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
        mx, my = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (255, 0, 0), button_quitter)
        if button_quitter.collidepoint((mx, my)):
            if click:
                main_menu()



def load_game():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('load game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)