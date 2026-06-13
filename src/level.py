import pygame
import pytmx
from settings import *

class Level :
    def __init__(self, map_file, tmx_file, nom):
        self.image = pygame.image.load(map_file)
        self.largeur_origine, self.hauteur_origine = self.image.get_size()
        self.nouvelle_largeur = self.largeur_origine * 2
        self.nouvelle_hauteur = self.hauteur_origine * 2
        self.image = pygame.transform.scale(self.image, (self.nouvelle_largeur, self.nouvelle_hauteur))
        self.rect = self.image.get_rect()
        self.nom = nom
        self.rect.x = SCREEN_WIDTH - self.image.get_width()
        self.rect.y = SCREEN_HEIGHT - self.image.get_height()
        self.collisions_sol = []
        tmx = pytmx.load_pygame(tmx_file)
        if tmx_file == "assets/maps/map1.tmx":
            for obj in tmx.get_layer_by_name("collisions_sol"):
                self.collisions_sol.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def draw(self, surface):
        surface.blit(self.image, self.rect)