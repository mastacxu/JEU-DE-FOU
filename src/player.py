import pygame
import pytmx
from settings import *

class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player/rudy.jpg")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - 500
        self.rect.y = SCREEN_HEIGHT - 400
        self.initx = self.rect.x 
        self.inity = self.rect.y
        self.sol = True
        self.vitesse_chute = 0

    def resistance_sol(self, sol, offset_x):
        for plat in sol:
            # On décale la plateforme avec l'offset de la map
            sol_decalee = pygame.Rect(plat.x + offset_x, plat.y, plat.width, plat.height)
            if self.rect.colliderect(sol_decalee):
                self.sol = True

    def update(self, sol, offset_x):
        
        self.resistance_sol(sol, offset_x)
        