import pygame
import json
from settings import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

def affichage():
    print('à remplir')

def jeu():
    print('à remplir')

def play_music(fichier, voluume, boucle=-1): # -1 pour tourner en bouble (on met qu'un parametre)
    pygame.mixer.music.stop() # stop la musique précédente
    pygame.mixer.music.load(fichier) # lance la musique choisi
    pygame.mixer.music.play(boucle)
    pygame.mixer.music.set_volume(voluume)