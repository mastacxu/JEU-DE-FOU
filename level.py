import pygame
import pytmx

class Level :
    def __init__(self, map_file, tmx_file, nom):
        self.image = pygame.image.load(map_file)
        self.rect = self.image.get_rect()
        self.nom = nom

        self.collisions_sol = []
        tmx = pytmx.load_pygame(tmx_file)
        if tmx_file == "assets/maps/map1.tmx":
            for obj in tmx.get_layer_by_name("collisions_sol"):
                self.collisions_sol.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def draw(self, surface):
        surface.blit(self.image, self.rect)