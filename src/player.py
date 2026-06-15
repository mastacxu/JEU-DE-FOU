import pygame
import pytmx
from settings import *

class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player/rudy.jpg")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 500
        self.initx = self.rect.x 
        self.inity = self.rect.y
        self.sol = True
        self.vitesse_chute = 0
    def sauter(self):
        if not self.saut:
            self.vitesse_chute = JUMP_FORCE
            self.saut = True
            return True
        else :
            return False
    
    def gravite(self, plateformes, offset_x):
        self.vitesse_chute += GRAVITY
        self.rect.y += self.vitesse_chute

        for plat in plateformes:
            plat_decalee = pygame.Rect(plat.x + offset_x, plat.y, plat.width, plat.height)
            if self.rect.colliderect(plat_decalee):
                if self.vitesse_chute > 0:  # seulement si on tombe
                    self.rect.bottom = plat_decalee.top
                    self.vitesse_chute = 0
                    self.saut = False
                if self.vitesse_chute < 0:  # si on saute et qu'on touche une plateforme au-dessus
                    self.rect.top = plat_decalee.bottom
                    self.vitesse_chute = 0

    def update(self, plateformes, offset_x):
        
        self.gravite(plateformes, offset_x)
        