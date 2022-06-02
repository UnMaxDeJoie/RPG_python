import pygame
from pygame import mixer #permet d'importer la possibilité de musique
pygame.mixer.init()#permet de faire tourner mixer
#ce fichier contient la provenance des sons utilisés pour les effets sonores
door_house_exit=mixer.Sound('sound/old_door_interior.wav')
door_house_enter=mixer.Sound('sound/old_door_exterior.wav')
ambiance=mixer.Sound('sound/inn_ambiance.wav')
door_inn_exit=mixer.Sound('sound/doorclose_inn.wav')
door_inn_enter=mixer.Sound('sound/doorOpen_inn.wav')
door_enter_castle=mixer.Sound('sound/doorClose_castle.wav')
door_exit_castle=mixer.Sound('sound/dooropen_castle.wav')