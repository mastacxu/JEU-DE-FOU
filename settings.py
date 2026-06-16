import pygame
pygame.init()
infos_ecran = pygame.display.Info()
SCREEN_WIDTH = infos_ecran.current_w -100
SCREEN_HEIGHT = infos_ecran.current_h -100
FPS = 60
TITLE = "JEU"
PLAYER_SPEED = 15
JUMP_FORCE = -15
GRAVITY = 0.8
vitesse_chute = 0