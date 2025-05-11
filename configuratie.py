import pygame

# Initialisatie
pygame.init()

# Kleuren
WIT = (255, 255, 255)
BLAUW = (0, 0, 128)
ZWART = (0, 0, 0)
ROOD = (255, 0, 0)
GROEN = (0, 255, 0)
GEEL = (255, 255, 0)
BRUIN = (138, 102, 66)
GRIJS = (128, 128, 128)

# Scherminstellingen
breedte = 870
hoogte = 620  # 570 + 50 zoals in Main_loop
screen = pygame.display.set_mode([breedte, hoogte])
font = pygame.font.SysFont(None, 36)