# Import
import pygame

#----------------------------------------------------------------------------------------------------------------------#

# Maze1 (niets)

    #pacman
pacman_imgs = [pygame.image.load("LEVEL 3/mond_dicht.png"), pygame.image.load("LEVEL 3/mond_open.png"), pygame.image.load("LEVEL 3/mond_half_open.png")]
pacman_imgs_op_schaal = [pygame.transform.scale(img, (30, 30)) for img in pacman_imgs]

    #vijanden
blauwspook = pygame.transform.scale(pygame.image.load("LEVEL 1/blauwspook.png"), (28, 28))
geelspook = pygame.transform.scale(pygame.image.load("LEVEL 1/geelspook.png"), (28, 28))
roodspook = pygame.transform.scale(pygame.image.load("LEVEL 1/roodspook.png"), (30, 30))
roosspook = pygame.transform.scale(pygame.image.load("LEVEL 1/roosspook.png"), (30, 30))

#----------------------------------------------------------------------------------------------------------------------#

# Maze2 (Naïl)

    # weg
donkergroen = pygame.transform.scale(pygame.image.load("LEVEL 2/donkergroen.png"), (30, 30))


    # veld
lichtgroen = pygame.transform.scale(pygame.image.load("LEVEL 2/lichtgroen.png"), (30, 30))
wite_lijn_L = pygame.transform.scale(pygame.image.load("LEVEL 2/wite lijn(L).png"), (30, 30))
cornerbasdroit = pygame.transform.scale(pygame.image.load("LEVEL 2/cornerbasdroit.png"), (30, 30))
cornerbasgauche = pygame.transform.scale(pygame.image.load("LEVEL 2/cornerbasgauche.png"), (30, 30))
cornerhautdroit = pygame.transform.scale(pygame.image.load("LEVEL 2/cornerhautdroit.png"), (30, 30))
cornerhautgauche = pygame.transform.scale(pygame.image.load("LEVEL 2/cornerhautgauche.png"), (30, 30))
ligenhaut = pygame.transform.scale(pygame.image.load("LEVEL 2/ligenhaut.png"), (30, 30))
lignebas = pygame.transform.scale(pygame.image.load("LEVEL 2/lignebas.png"), (30, 30))
lignedroit = pygame.transform.scale(pygame.image.load("LEVEL 2/lignedroit.png"), (30, 30))
lignegauche = pygame.transform.scale(pygame.image.load("LEVEL 2/lignegauche.png"), (30, 30))
pase = pygame.transform.scale(pygame.image.load("LEVEL 2/pase.png"), (30, 30))
pase2 = pygame.transform.scale(pygame.image.load("LEVEL 2/pase2.jpg"), (30, 30))
pessa = pygame.transform.scale(pygame.image.load("LEVEL 2/pessa.png"), (30, 30))
pessa2 = pygame.transform.scale(pygame.image.load("LEVEL 2/pessa2.png"), (30, 30))
sepabas = pygame.transform.scale(pygame.image.load("LEVEL 2/sepabas.png"), (30, 30))
sepahaut = pygame.transform.scale(pygame.image.load("LEVEL 2/sepahaut.png"), (30, 30))

    #vijanden
Ronaldo = pygame.transform.scale(pygame.image.load("LEVEL 2/Ronaldo_30x30.png"), (30, 30))
Neymar = pygame.transform.scale(pygame.image.load("LEVEL 2/Neymar_30x30.png"), (30, 30))
Messi = pygame.transform.scale(pygame.image.load("LEVEL 2/Messi_30x30.png"), (30, 30))
Lukaku = pygame.transform.scale(pygame.image.load("LEVEL 2/Lukaku_30x30.png"), (30, 30))


#----------------------------------------------------------------------------------------------------------------------#

# Maze3 (Haris)

#afbeeldingen
speed_img = pygame.transform.scale(pygame.image.load("LEVEL 3/boost_30x30 (1).png"), (30, 30))
crocoo1 = pygame.transform.scale(pygame.image.load("LEVEL 3/crocooo_processed.png"), (30, 30))
etoue_30x30 = pygame.transform.scale(pygame.image.load("LEVEL 3/etoue_30x30.jpg"), (30, 30))
gier1 = pygame.transform.scale(pygame.image.load("LEVEL 3/gier.png"), (30, 30))
greenbleu_30x30 = pygame.transform.scale(pygame.image.load("LEVEL 3/greenbleu_30x30.jpg"), (30, 30))
hart1 = pygame.transform.scale(pygame.image.load("LEVEL 3/hart1.png"), (30, 30))
hippo1 = pygame.transform.scale(pygame.image.load("LEVEL 3/hippo_processed.png"), (30, 30))
leeuw1 = pygame.transform.scale(pygame.image.load("LEVEL 3/leeuw1.png"), (30, 30))
neushoorn1 = pygame.transform.scale(pygame.image.load("LEVEL 3/neushoorn1.png"), (30, 30))
olifant1 = pygame.transform.scale(pygame.image.load("LEVEL 3/olifant1.png"), (30, 30))
resized_tile_0_4 = pygame.transform.scale(pygame.image.load("LEVEL 3/resized_tile_0_4 (1).png"), (30, 30))
way_30x30 = pygame.transform.scale(pygame.image.load("LEVEL 3/way_30x30.jpeg"), (30, 30))
yellow_green_gradient = pygame.transform.scale(pygame.image.load("LEVEL 3/yellow_green_gradient.png"), (30, 30))

# breek-frames
#break_wall_imgs = [
#     pygame.image.load("LEVEL 3/casseau_30x30.png")
#]

casseau_img = pygame.transform.scale(pygame.image.load("LEVEL 3/casseau_30x30.png"), (30, 30))

#----------------------------------------------------------------------------------------------------------------------#