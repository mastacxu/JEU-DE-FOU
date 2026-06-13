import pygame
import pytmx
from settings import *

class PNJ:
    def __init__(self, x, y, image_path, dialogue):
        self.font = pygame.font.Font("CinzelDecorative-Bold.ttf", 20)
        self.font_petite = pygame.font.Font("CinzelDecorative-Bold.ttf", 10)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (45, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dialogue = dialogue