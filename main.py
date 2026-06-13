import pygame
import json
from settings import *
from src.level import Level
from src.player import Player

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

level = Level("assets/maps/map1.png", "assets/maps/map1.tmx", "map1")
player = Player()


def affichage():
    level.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

def boutons(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running

def jeu():
    running = True
    
    while running:
        running = boutons(running)

        player.update(level.collisions_sol,level.rect.x)
        affichage()
        clock.tick(FPS)
        

def play_music(fichier, voluume, boucle=-1): # -1 pour tourner en bouble (on met qu'un parametre)
    pygame.mixer.music.stop() # stop la musique précédente
    pygame.mixer.music.load(fichier) # lance la musique choisi
    pygame.mixer.music.play(boucle)
    pygame.mixer.music.set_volume(voluume)

jeu()