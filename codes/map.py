from dataclasses import dataclass
import pygame
import pytmx
import pyscroll
from pygame import mixer  #permet d'importer la possibilité de musique
from sound import * #permet d'importer la possibilité d'effets sonore
from monstretuto import *
pygame.mixer.init() #permet de faire tourner mixer
mixer.music.load('sound/background.wav') #cherche la musique à jouer
mixer.music.play(-1)#musique tourne en continue
pygame.mixer.music.set_volume(0.10) #volume



@dataclass  #permet de dire que cette classe ne contient que des donnée
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str

@dataclass      #permet de dire que cette classe ne contient que des donnée
class Map:
    name: str   #définit la catégorie de la variable name
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]

class MapManager:

    def __init__(self, screen, player):
        self.maps = dict()
        self.screen = screen
        self.player = player
        self.current_map = "Maison_hero_int"
        self.monster = "monstre"
        self.register_map("Maison_hero_int", portals=[
            Portal(from_world="Maison_hero_int", origin_point='exit_house', target_world='Maison_hero_ext', teleport_point='exit_house')
        ])  #permet de se téléporter d'une map à l'autre
        self.register_map("Maison_hero_ext", portals=[
            Portal(from_world="Maison_hero_ext", origin_point='enter_house', target_world='Maison_hero_int', teleport_point='enter_house'),
            Portal(from_world="Maison_hero_ext", origin_point='exit_map', target_world='map1', teleport_point='enter_map01')
        ])
        self.register_map("map1", portals=[
            Portal(from_world="map1", origin_point='exit_map01', target_world='Maison_hero_ext', teleport_point='enter_map'),
            Portal(from_world="map1", origin_point='exit_map02', target_world='map2', teleport_point='enter_map01')
        ])
        self.register_map("map2", portals=[
            Portal(from_world="map2", origin_point='exit_bonus', target_world='mapbonus', teleport_point='enter_map'),
            Portal(from_world="map2", origin_point='exit_map01', target_world='map1', teleport_point='enter_map02'),
            Portal(from_world="map2", origin_point='exit_map03', target_world='entréeville', teleport_point='enter_map01')
        ])
        self.register_map("mapbonus", portals=[
            Portal(from_world="mapbonus", origin_point='exit_field', target_world='map2', teleport_point='enter_map02')
        ])
        self.register_map("entréeville", portals=[
            Portal(from_world="entréeville", origin_point='exit_map01', target_world='map2', teleport_point='enter_map03'),
            Portal(from_world="entréeville", origin_point='exit_map03', target_world='map4', teleport_point='enter_map'),
            Portal(from_world="entréeville", origin_point='exit_village', target_world='map_ville1', teleport_point='enter_map01')
        ])
        self.register_map("map4", portals=[
            Portal(from_world="map4", origin_point='exit_map', target_world='entréeville', teleport_point='enter_map03')
        ])
        self.register_map("map_ville1", portals=[
            Portal(from_world="map_ville1", origin_point='exit_field', target_world='entréeville', teleport_point='enter_map02'),
            Portal(from_world="map_ville1", origin_point='exit_map02', target_world='entrée_chateau', teleport_point='enter_map01'),
            Portal(from_world="map_ville1", origin_point='exit_inn', target_world='interrieurtavern', teleport_point='enter_map')
        ])
        self.register_map("interrieurtavern", portals=[
            Portal(from_world="interrieurtavern", origin_point='enter_city', target_world='map_ville1', teleport_point='enter_map03'),
        ])
        self.register_map("entrée_chateau", portals=[
            Portal(from_world="entrée_chateau", origin_point='exit_map01', target_world='map_ville1', teleport_point='enter_map02'),
            Portal(from_world="entrée_chateau", origin_point='enter_castle', target_world='chateau_interrieur', teleport_point='enter_map')
        ])
        self.register_map("chateau_interrieur", portals=[
            Portal(from_world="chateau_interrieur", origin_point='exit_castle', target_world='entrée_chateau', teleport_point='enter_map02'),
        ])
        self.teleport_player("joueur")
        


        

    def register_map(self, name, portals):
        # Charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(f"../maps/{name}.tmx")  #charge la carte par son nom
        map_data = pyscroll.data.TiledMapData(tmx_data)                 #obtient les donnée de la map tmx
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())    #obtient les calque de la map tmx
        map_layer.zoom = 3      #permet de grossir la taille

        # Les collisions
        walls = []

        for obj in tmx_data.objects:
            if obj.name == "obstacle":      #si dans la catégorie le nom est "obstacle"
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))  #rajoute dans la liste walls les mur avec le coordonnée

        # Dessiner les différents calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)

        # Enregistre la nouvelle carte chargée
        self.maps[name] = Map(name, walls, group, tmx_data, portals)
            
    def check_collisions(self):         #Fonction vérifie collision et les portails

        #boucle des portails
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.bottom.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)
                    if portal.target_world == 'map1':
                        pygame.quit()
                        Pmonster(player,0)
                    #Condition lancement musiques et effets sonores
                    if portal.origin_point=="exit_village":#quand le joueur utilise ce portail la musique change pour une autre
                        mixer.music.load('sound/village.wav')
                        mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.10)
                    elif portal.origin_point=="exit_field":#idem
                        mixer.music.load('sound/background.wav')
                        mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.10)
                    elif portal.origin_point=="exit_bonus":#idem
                        mixer.music.load('sound/bonus.wav')
                        mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.10)
                    elif portal.origin_point=="exit_house":#quand le joueur utilise ce portail un bruit de porte est joué
                        door_house_exit.play()
                        door_house_exit.set_volume(0.03)
                    elif portal.origin_point=="enter_house":#idem
                        door_house_enter.play()
                        door_house_enter.set_volume(0.03)
                    elif portal.origin_point=="exit_inn":#quand le joueur utilise ce portail un bruit de foule est joué
                        ambiance.play()
                        ambiance.set_volume(0.1)
                        door_inn_exit.play()
                        door_inn_exit.set_volume(0.03)
                    elif portal.origin_point=="enter_city":#quand le joueur utilise ce portail un bruit de porte est joué
                        door_inn_enter.play()
                        door_inn_enter.set_volume(0.03)
                        ambiance.stop()
                    elif portal.origin_point=="enter_castle":#idem
                        door_enter_castle.play()
                        door_enter_castle.set_volume(0.03)
                    elif portal.origin_point=="exit_castle":#idem
                        door_exit_castle.play()
                        door_exit_castle.set_volume(0.03)
        #boucles des collisions
        for sprite in self.get_group().sprites():
            if sprite.bottom.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def get_map(self):
        return self.maps[self.current_map]

    def get_group(self):
        return self.get_map().group

    def get_walls(self):
        return self.get_map().walls

    def get_object(self, name):
        return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def teleport_player(self, name):    #fonction téléportation joueur
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def update(self):
        self.get_group().update()
        self.check_collisions()