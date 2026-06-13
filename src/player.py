import pygame
import pytmx
from settings import *

class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player/rudy.jpg")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 130
        self.rect.y = 560
        self.initx = self.rect.x 
        self.inity = self.rect.y
        self.vitesse_chute = 0

    def gravite(self, sol, offset_x):
        self.vitesse_chute += GRAVITY
        self.rect.y += self.vitesse_chute

        for plat in sol:
            # On décale la plateforme avec l'offset de la map
            sol_decalee = pygame.Rect(plat.x + offset_x, plat.y, plat.width, plat.height)
            if self.rect.colliderect(sol_decalee):
                if self.vitesse_chute > 0:  # seulement si on tombe
                    self.rect.bottom = sol_decalee.top
                    self.vitesse_chute = 0
                    self.saut = False


    def update(self, sol, offset_x):
        self.gravite(sol, offset_x)
        