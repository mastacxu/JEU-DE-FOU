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

level = Level("assets/maps/map1v2.png", "assets/maps/map1v2.tmx", "map1")
player = Player()


def affichage():
    level.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

def limites(max_droite,max_gauche,max_bas,max_haut):
    if level.rect.x + level.rect.width <= SCREEN_WIDTH :
        level.rect.x = SCREEN_WIDTH - level.rect.width
        max_droite = True
    if level.rect.x >= 0 :
        level.rect.x = 0
        max_gauche = True
    if player.rect.x <0:
        player.rect.x = 0
    if level.rect.bottom <= SCREEN_HEIGHT :
        level.rect.bottom = SCREEN_HEIGHT
        max_bas = True
    return max_droite,max_gauche,max_bas,max_haut

def boutons(running, max_droite, max_gauche,max_bas,max_haut):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.sauter()

    touches = pygame.key.get_pressed() 
    #version pas cote
    if touches[pygame.K_d] and not touches[pygame.K_q] :
        if max_gauche and player.rect.x < player.initx:
            player.rect.x += PLAYER_SPEED
        elif max_droite:
            player.rect.x += PLAYER_SPEED
        else:
            level.rect.x -= PLAYER_SPEED
        if player.rect.x >= player.initx:
            max_gauche = False

    if touches[pygame.K_q] and not touches[pygame.K_d]:
        if player.initx == player.rect.x and not max_gauche:  # si le joueur est à sa position initiale, on bouge la map
            max_droite = False  # on peut à nouveau bouger à droite 
        if player.initx == player.rect.x and not max_gauche:
            level.rect.x += PLAYER_SPEED
        if max_droite or max_gauche:
            player.rect.x -= PLAYER_SPEED

    if touches[pygame.K_z] and not touches[pygame.K_s]:
        if max_bas and player.rect.y >= player.inity:
            # ramener le joueur à sa position initiale d'abord
            player.rect.y -= PLAYER_SPEED
        elif max_haut:
            player.rect.y += PLAYER_SPEED
        else:
            level.rect.y += PLAYER_SPEED
    
    if touches[pygame.K_s] and not touches[pygame.K_z]:
        if max_haut and player.rect.y >= player.inity:
            # ramener le joueur à sa position initiale d'abord
            player.rect.y += PLAYER_SPEED
        elif max_bas:
            player.rect.y += PLAYER_SPEED
        else:
            level.rect.y -= PLAYER_SPEED

    if player.rect.y == player.inity :
        max_haut = False
        max_bas = False
    """
    #version de cote :
    touches = pygame.key.get_pressed()
    if touches[pygame.K_d] and not touches[pygame.K_q] :
        if max_gauche and player.rect.x < player.initx:
            player.rect.x += PLAYER_SPEED
        elif max_droite:
            player.rect.x += PLAYER_SPEED
        else:
            level.rect.x -= PLAYER_SPEED
        if player.rect.x >= player.initx:
            max_gauche = False
        droite = True
        gauche = False
    
    if touches[pygame.K_q] and not touches[pygame.K_d]:
        if player.initx == player.rect.x and not max_gauche:  # si le joueur est à sa position initiale, on bouge la map
            max_droite = False  # on peut à nouveau bouger à droite 
        if player.initx == player.rect.x and not max_gauche:
            level.rect.x += PLAYER_SPEED
        if max_droite or max_gauche:
            player.rect.x -= PLAYER_SPEED
    """
    return running, max_droite, max_gauche,max_bas,max_haut

def jeu():
    max_droite = False
    max_gauche = False
    max_bas = False
    max_haut = False
    running = True
    
    while running:
        max_droite, max_gauche, max_bas ,max_haut = limites(max_droite,max_gauche,max_bas,max_haut)
        running, max_droite, max_gauche,max_bas,max_haut = boutons(running, max_droite, max_gauche,max_bas,max_haut)

        player.update(level.collisions_sol,level.rect.x)
        affichage()
        clock.tick(FPS)
        

def play_music(fichier, voluume, boucle=-1): # -1 pour tourner en bouble (on met qu'un parametre)
    pygame.mixer.music.stop() # stop la musique précédente
    pygame.mixer.music.load(fichier) # lance la musique choisi
    pygame.mixer.music.play(boucle)
    pygame.mixer.music.set_volume(voluume)

jeu()