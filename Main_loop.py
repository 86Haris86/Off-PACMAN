# Import and initialize the pygame library
import pygame
import random

# imports van andere files
from Speler import Speler , radius_speler , snelheid_speler , tijd_snelheidboost , snelheid_snelheidboost
from Vijand import Spook , snelheid_monster , snelheid_monster_2
from Plan_en_object import Object1 , Object2 , Muur , Snelheidsobject
from Hulpfuncties import maze_van_bestand , toon_levens
from Afbeeldingen import blauwspook, geelspook, roodspook, roosspook, pacman_imgs_op_schaal, Ronaldo, Neymar, Messi, \
    Lukaku
from Afbeeldingen import way_30x30, greenbleu_30x30, etoue_30x30, yellow_green_gradient, resized_tile_0_4, speed_img, casseau_img
from Afbeeldingen import donkergroen, lichtgroen , wite_lijn_L, cornerbasdroit, cornerbasgauche, cornerhautdroit, cornerhautgauche, ligenhaut, lignebas, lignedroit, lignegauche, pase, pase2, pessa, pessa2, sepabas, sepahaut
from Afbeeldingen import crocoo1 , gier1 , hippo1 , leeuw1 , neushoorn1 , olifant1
from menu import toon_menu


#----------------------------------------------------------------------------------------------------------------------#

# Initialisatie
pygame.init()

#----------------------------------------------------------------------------------------------------------------------#

# scherm groter maken met 'a' om de score bij te schrijven
a = 50
font = pygame.font.SysFont(None, 36)
tekst_punten_x , tekst_punten_y = 10 , 580
tekst_tijd_x , tekst_tijd_y = 200 , 580
tekst_tijd_bonus_x , tekst_tijd_bonus_y = 400 , 580
spook_teller_x, spook_teller_y = 600 , 580

# Scherminstellingen
breedte = int(870)
hoogte = int(570 + a)
balgrootte = 4
screen = pygame.display.set_mode([breedte, hoogte])
#screen = pygame.display.set_mode([breedte, hoogte], pygame.FULLSCREEN)


#----------------------------------------------------------------------------------------------------------------------#

# Tijd
tijd = pygame.time.Clock()
fps = 30
tijd_van_bonus = 8
tijd_van_overgang = 3000

#----------------------------------------------------------------------------------------------------------------------#

# Kleuren
WIT = (255, 255, 255)
BLAUW = (0, 0, 128)
ROOD = (255, 0, 0)
GROEN = (0, 255, 0)
GEEL = (255, 255, 0)
ZWART = (0, 0, 0)
BRUIN = (138,102,66)
GRIJS = (128,128,128)

#----------------------------------------------------------------------------------------------------------------------#

# Grootte van muur en rand
muurgrootte = 30
balgrootte1 = 4
balgrootte2 = 8

#----------------------------------------------------------------------------------------------------------------------#

# Verschillende maze
maze1 = maze_van_bestand("maze1.txt")
maze2 = maze_van_bestand("maze2.txt")
maze3 = maze_van_bestand("maze3.txt")

# maze dat wordt gebruikt bij het runnen
gebruikte_maze = maze1

#----------------------------------------------------------------------------------------------------------------------#

def init_maze1():
    global walls , items , items2 , items3, list_of_monsters , speler , zone1 , overdracht1 , zone2 , overdracht2 , vijand2
    global toegelaten_posities_vijand,deur_van_spoken , eindzone_x1,eindzone_y1, eindzone_x2,eindzone_y2, eindzone_x3,eindzone_y3   , zone_end , snelheids_object , croco , hippo

    # Bewaar bestaande spelerdata als speler al bestaat
    huidige_score = speler.punten if 'speler' in globals() else 0
    huidige_levens = speler.levens if 'speler' in globals() else 3
    huidige_eetcombo = speler.eetcombo if 'speler' in globals() else 0
    huidige_spookteller = speler.gegeten_spoken_teller if 'speler' in globals() else 0

    # Walls en Items vullen
    walls = []
    items = []
    items2 = []
    items3 = []

    # Waar de speler mag bewegen in de maze
    toegelaten_posities_speler = [0, 3, 4, 5]

    # Waar de vijand mag bewegen in de maze
    toegelaten_posities_vijand = [0, 2, 3, 4, 5]
    deur_van_spoken = 2

    # speler
    start_positie_x_speler1, start_positie_y_speler1 = 14 * muurgrootte + muurgrootte // 2, 12 * muurgrootte + muurgrootte // 2

    # vijanden
    start_positie_x_soort1, start_positie_y_soort1 = 12 * muurgrootte + muurgrootte // 2 + 1 * muurgrootte // 5, 10 * muurgrootte + muurgrootte // 2
    start_positie_x_soort2, start_positie_y_soort2 = 13 * muurgrootte + muurgrootte // 2 + 2 * muurgrootte // 5, 10 * muurgrootte + muurgrootte // 2
    start_positie_x_soort3, start_positie_y_soort3 = 14 * muurgrootte + muurgrootte // 2 + 3 * muurgrootte // 5, 10 * muurgrootte + muurgrootte // 2
    start_positie_x_soort4, start_positie_y_soort4 = 15 * muurgrootte + muurgrootte // 2 + 4 * muurgrootte // 5, 10 * muurgrootte + muurgrootte // 2
    start_positie_x_soort5, start_positie_y_soort5 = None, None
    start_positie_x_soort6, start_positie_y_soort6 = None, None


    # Overdrachtszones
    zone1_x, zone1_y = 0 * muurgrootte, 9 * muurgrootte
    zone2_x, zone2_y = 28 * muurgrootte + muurgrootte // 2, 9 * muurgrootte
    zone_breedte_x = muurgrootte // 2
    zone_hoogte_y = muurgrootte

    zone1 = (zone1_x, zone1_y, zone_breedte_x, zone_hoogte_y)
    zone2 = (zone2_x, zone2_y, zone_breedte_x, zone_hoogte_y)

    # Overdrachtcoördinaten
    overdracht12_co_x , overdracht12_co_y = zone2_x , zone2_y + zone_breedte_x
    overdracht21_co_x , overdracht21_co_y = zone1_x + zone_breedte_x , zone1_y + zone_breedte_x

    overdracht1 = (overdracht12_co_x, overdracht12_co_y)
    overdracht2 = (overdracht21_co_x, overdracht21_co_y)

    # Eindzone
    #eindzone_x = start_positie_x_speler1 - muurgrootte // 2
    #eindzone_y = start_positie_y_speler1 - muurgrootte // 2
    #zone_end = (eindzone_x,eindzone_y,zone_breedte_x, zone_hoogte_y)
    eindzone_x1 = start_positie_x_speler1 - muurgrootte // 2
    eindzone_y1 = start_positie_y_speler1 + 90 - muurgrootte // 2
    zone_end = (eindzone_x1, eindzone_y1, zone_breedte_x, zone_hoogte_y)

    # afbeeldingen vijanden , activatie
    soort1 , soort1_active = blauwspook , True
    soort2 , soort2_active = geelspook , True
    soort3 , soort3_active = roodspook , True
    soort4 , soort4_active = roosspook , True
    soort5 , soort5_active = crocoo1 , False
    soort6 , soort6_active = hippo1 , False

    for row_index, row in enumerate(gebruikte_maze):
        for col_index, tile in enumerate(row):
            x = col_index * muurgrootte
            y = row_index * muurgrootte
            if tile == 0:
                items.append(Object1(x, y, screen, balgrootte1, WIT))
            elif tile == 1:
                walls.append(Muur(x, y, screen, muurgrootte, BLAUW))
            elif tile == 2:
                walls.append(Muur(x, y, screen, muurgrootte, ROOD))
            elif tile == 3:
                items2.append(Object2(x, y, screen, balgrootte2, WIT))
            elif tile == 4:
                walls.append(Muur(x, y, screen, muurgrootte, GROEN))

    # Zoek alle lege tegels (waarde 0) in het doolhof
    lege_plekken = [(j * muurgrootte, i * muurgrootte) for i, rij in enumerate(gebruikte_maze) for j, waarde in enumerate(rij) if waarde == 0]

    # Kies willekeurig een positie voor het snelheidsobject
    x_positie, y_positie = random.choice(lege_plekken)

    # Maak het snelheidsobject aan (je kan hier een afbeelding toevoegen later)
    snelheids_object = Snelheidsobject(x_positie, y_positie, screen, muurgrootte, afbeelding=speed_img)
    for item in items:
        if item.x == x_positie and item.y == y_positie:
            items.remove(item)
            break  # stop na het verwijderen
    items3.append(snelheids_object)

    speler = Speler(start_positie_x_speler1, start_positie_y_speler1, screen, WIT, radius_speler, snelheid_speler, toegelaten_posities_speler, gebruikte_maze, pacman_imgs_op_schaal)
    vijand1 = Spook(start_positie_x_soort1, start_positie_y_soort1, screen, soort1, snelheid_monster, "pinky", toegelaten_posities_vijand, gebruikte_maze, soort1_active)
    vijand2 = Spook(start_positie_x_soort2, start_positie_y_soort2, screen, soort2, snelheid_monster, "blinky", toegelaten_posities_vijand, gebruikte_maze, soort2_active)
    vijand3 = Spook(start_positie_x_soort3, start_positie_y_soort3, screen, soort3, snelheid_monster, "inky", toegelaten_posities_vijand, gebruikte_maze, soort3_active)
    vijand4 = Spook(start_positie_x_soort4, start_positie_y_soort4, screen, soort4, snelheid_monster, "clyde", toegelaten_posities_vijand, gebruikte_maze, soort4_active)
    croco = Spook(start_positie_x_soort5, start_positie_y_soort5, screen, soort5, snelheid_monster_2, "blinky", toegelaten_posities_vijand, gebruikte_maze, soort5_active)
    hippo = Spook(start_positie_x_soort6, start_positie_y_soort6, screen, soort6, snelheid_monster_2, "blinky", toegelaten_posities_vijand, gebruikte_maze, soort6_active)
    list_of_monsters = [vijand1, vijand2, vijand3, vijand4, croco, hippo]

    # Zet waarden terug
    speler.punten = huidige_score
    speler.levens = huidige_levens
    speler.eetcombo = huidige_eetcombo
    speler.gegeten_spoken_teller = huidige_spookteller

    # 1 : muur
    # 2 : muur spoken
    # 0 : object
    # 3 : object2
    # 4 : overgang
    # 5 : niets

# ----------------------------------------------------------------------------------------------------------------------#

def init_maze2():
    global walls, items, items2, items3, list_of_monsters, speler, zone1, overdracht1, zone2, overdracht2, vijand2
    global toegelaten_posities_vijand, deur_van_spoken, eindzone_x1,eindzone_y1, eindzone_x2,eindzone_y2, eindzone_x3,eindzone_y3, zone_end , snelheids_object , croco , hippo

    # Bewaar bestaande spelerdata als speler al bestaat
    huidige_score = speler.punten if 'speler' in globals() else 0
    huidige_levens = speler.levens if 'speler' in globals() else 3
    huidige_eetcombo = speler.eetcombo if 'speler' in globals() else 0
    huidige_spookteller = speler.gegeten_spoken_teller if 'speler' in globals() else 0

    # Walls en Items vullen
    walls = []
    items = []
    items2 = []
    items3 = []
    # Waar de speler mag bewegen in de maze
    toegelaten_posities_speler = [0, 2, 3, 4, 10, 12, 18, 19, 20, 21, 22, 23, 25, 26,29]
    # Waar de vijand mag bewegen in de maze
    toegelaten_posities_vijand = [0, 2, 3, 4, 10, 12, 18, 19, 20, 21, 22, 23, 25, 26,29]
    deur_van_spoken = []
    # speler
    start_positie_x_speler1, start_positie_y_speler1 = 14 * muurgrootte + muurgrootte // 2, 9 * muurgrootte + muurgrootte // 2
    # vijanden
    start_positie_x_soort1, start_positie_y_soort1 = 1 * muurgrootte + 15, 1 * muurgrootte + 15
    start_positie_x_soort2, start_positie_y_soort2 = 27 * muurgrootte + 15, 1 * muurgrootte + 15
    start_positie_x_soort3, start_positie_y_soort3 = 1 * muurgrootte + 15, 17 * muurgrootte + 15
    start_positie_x_soort4, start_positie_y_soort4 = 27 * muurgrootte + 15, 17 * muurgrootte + 15
    start_positie_x_soort5, start_positie_y_soort5 = None, None
    start_positie_x_soort6, start_positie_y_soort6 = None, None

    # Overdrachtszones
    zone1_x, zone1_y = None, None
    zone2_x, zone2_y = None, None
    zone_breedte_x = muurgrootte
    zone_hoogte_y = muurgrootte

    zone1 = (zone1_x, zone1_y, zone_breedte_x, zone_hoogte_y)
    zone2 = (zone2_x, zone2_y, zone_breedte_x, zone_hoogte_y)

    # Overdrachtcoördinaten
    overdracht12_co_x, overdracht12_co_y = (None, None)
    overdracht21_co_x, overdracht21_co_y = (None, None)

    overdracht1 = (overdracht12_co_x, overdracht12_co_y)
    overdracht2 = (overdracht21_co_x, overdracht21_co_y)

    # Eindzone
    #eindzone_x = start_positie_x_speler1 - muurgrootte // 2
    #eindzone_y = start_positie_y_speler1 - muurgrootte // 2
    #zone_end = (eindzone_x, eindzone_y,zone_breedte_x, zone_hoogte_y)
    eindzone_x2 = start_positie_x_speler1  - muurgrootte // 2
    eindzone_y2 = start_positie_y_speler1 - 210 - muurgrootte // 2
    zone_end = (eindzone_x2, eindzone_y2,zone_breedte_x, zone_hoogte_y)



    # afbeeldingen vijanden , activatie
    soort1, soort1_active = Ronaldo, True
    soort2, soort2_active = Neymar, True
    soort3, soort3_active = Messi, True
    soort4, soort4_active = Lukaku, True
    soort5, soort5_active = crocoo1, False
    soort6, soort6_active = hippo1, False

    for row_index, row in enumerate(gebruikte_maze):
        for col_index, tile in enumerate(row):
            x = col_index * muurgrootte
            y = row_index * muurgrootte
            if tile == 0:
                items.append(Object1(x, y, screen, balgrootte, WIT))
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=donkergroen))
            elif tile == 29:
                items2.append(Object2(x, y, screen, balgrootte2, WIT))
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=donkergroen))
            elif tile == 1:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=lichtgroen))
            elif tile == 2:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=cornerbasgauche))
            elif tile == 3:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=cornerbasdroit))
            elif tile == 4:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=cornerhautdroit))
            elif tile == 5:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=lignebas))
            elif tile == 6:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=ligenhaut))
            elif tile == 7:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=sepahaut))
            elif tile == 8:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=sepabas))
            elif tile == 9:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=lignegauche))
            elif tile == 10:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=cornerhautgauche))
            elif tile == 12:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=wite_lijn_L))
            elif tile == 13:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=lignedroit))
            elif tile == 20:
                walls.append(Muur(x, y, screen, muurgrootte, kleur=WIT))
            elif tile == 18:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=pase))
            elif tile == 19:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=pase2))
            elif tile == 21:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=pessa))
            elif tile == 22:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=pessa2))
            elif tile == 23:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=lignedroit))
            elif tile == 26:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=ligenhaut))
            elif tile == 25:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=lignebas))

        # Zoek alle lege tegels (waarde 0) in het doolhof
        lege_plekken = [(j * muurgrootte, i * muurgrootte) for i, rij in enumerate(gebruikte_maze) for j, waarde in
                        enumerate(rij) if waarde == 0]

        # Kies willekeurig een positie voor het snelheidsobject
        x_positie, y_positie = random.choice(lege_plekken)

        # Maak het snelheidsobject aan (je kan hier een afbeelding toevoegen later)
        snelheids_object = Snelheidsobject(x_positie, y_positie, screen, muurgrootte, afbeelding=speed_img)
        for item in items:
            if item.x == x_positie and item.y == y_positie:
                items.remove(item)
                break  # stop na het verwijderen
        items3.append(snelheids_object)

    speler = Speler(start_positie_x_speler1, start_positie_y_speler1, screen, WIT, radius_speler, snelheid_speler, toegelaten_posities_speler, gebruikte_maze, pacman_imgs_op_schaal)
    vijand1 = Spook(start_positie_x_soort1, start_positie_y_soort1, screen, soort1, snelheid_monster, "pinky", toegelaten_posities_vijand, gebruikte_maze, soort1_active)
    vijand2 = Spook(start_positie_x_soort2, start_positie_y_soort2, screen, soort2, snelheid_monster, "blinky", toegelaten_posities_vijand, gebruikte_maze, soort2_active)
    vijand3 = Spook(start_positie_x_soort3, start_positie_y_soort3, screen, soort3, snelheid_monster, "inky", toegelaten_posities_vijand, gebruikte_maze, soort3_active)
    vijand4 = Spook(start_positie_x_soort4, start_positie_y_soort4, screen, soort4, snelheid_monster, "clyde", toegelaten_posities_vijand, gebruikte_maze, soort4_active)
    croco = Spook(start_positie_x_soort5, start_positie_y_soort5, screen, soort5, snelheid_monster_2, "blinky", toegelaten_posities_vijand, gebruikte_maze, soort5_active)
    hippo = Spook(start_positie_x_soort6, start_positie_y_soort6, screen, soort6, snelheid_monster_2, "blinky", toegelaten_posities_vijand, gebruikte_maze, soort6_active)
    list_of_monsters = [vijand1, vijand2, vijand3, vijand4, croco, hippo]
    #print('dit is van maze2',len(items))

    # Zet waarden terug
    speler.punten = huidige_score
    speler.levens = huidige_levens
    speler.eetcombo = huidige_eetcombo
    speler.gegeten_spoken_teller = huidige_spookteller

# ----------------------------------------------------------------------------------------------------------------------#
def init_maze3():
    global walls, items, items2, items3, list_of_monsters, speler, zone1, overdracht1, zone2, overdracht2, vijand2
    global toegelaten_posities_vijand, deur_van_spoken, eindzone_x1,eindzone_y1, eindzone_x2,eindzone_y2, eindzone_x3,eindzone_y3, zone_end , snelheids_object , croco , hippo

    # Bewaar bestaande spelerdata als speler al bestaat
    huidige_score = speler.punten if 'speler' in globals() else 0
    huidige_levens = speler.levens if 'speler' in globals() else 3
    huidige_eetcombo = speler.eetcombo if 'speler' in globals() else 0
    huidige_spookteller = speler.gegeten_spoken_teller if 'speler' in globals() else 0

    # Walls en Items vullen
    walls = []
    items = []
    items2 = []
    items3 = []
    # Waar de speler mag bewegen in de maze
    toegelaten_posities_speler = [0,6,9, 10,99,32]
    # Waar de vijand mag bewegen in de maze
    toegelaten_posities_vijand = [0,9,10,99,32]
    deur_van_spoken = []
    # speler
    start_positie_x_speler1, start_positie_y_speler1 = 14 * muurgrootte + muurgrootte // 2, 9 * muurgrootte + muurgrootte // 2
    # vijanden
    start_positie_x_soort1, start_positie_y_soort1 = 1 * muurgrootte + 15, 1 * muurgrootte + 15
    start_positie_x_soort2, start_positie_y_soort2 = 27 * muurgrootte + 15, 1 * muurgrootte + 15
    start_positie_x_soort3, start_positie_y_soort3 = 1 * muurgrootte + 15, 10 * muurgrootte + 15
    start_positie_x_soort4, start_positie_y_soort4 = 27 * muurgrootte + 15, 10 * muurgrootte + 15
    start_positie_x_soort5, start_positie_y_soort5 = 27 * muurgrootte + 15, 13 * muurgrootte + 15
    start_positie_x_soort6, start_positie_y_soort6 = 27 * muurgrootte + 15, 17 * muurgrootte + 15

    # Overdrachtszones
    zone1_x, zone1_y = (1 * muurgrootte, 7 * muurgrootte)
    zone2_x, zone2_y = (27 * muurgrootte + muurgrootte // 2, 15 * muurgrootte)
    zone_breedte_x = muurgrootte // 2
    zone_hoogte_y = muurgrootte

    zone1 = (zone1_x, zone1_y, zone_breedte_x, zone_hoogte_y)
    zone2 = (zone2_x, zone2_y, zone_breedte_x, zone_hoogte_y)

    # Overdrachtcoördinaten
    overdracht12_co_x, overdracht12_co_y = (zone2_x, zone2_y + zone_breedte_x)
    overdracht21_co_x, overdracht21_co_y = (zone1_x + zone_breedte_x, zone1_y + zone_breedte_x)

    overdracht1 = (overdracht12_co_x, overdracht12_co_y)
    overdracht2 = (overdracht21_co_x, overdracht21_co_y)

    #Eindzone
    #eindzone_x = 1 * muurgrootte
    #eindzone_y = 15 * muurgrootte
    #zone_end = (eindzone_x ,eindzone_y ,zone_breedte_x, zone_hoogte_y)
    eindzone_x3 = 1 * muurgrootte
    eindzone_y3 = 15 * muurgrootte
    zone_end = (eindzone_x3 ,eindzone_y3 ,zone_breedte_x, zone_hoogte_y)


    # afbeeldingen vijanden , activatie
    soort1 , soort1_active = leeuw1 , True
    soort2 , soort2_active = olifant1 , True
    soort3 , soort3_active = neushoorn1 , True
    soort4 , soort4_active = gier1 , True
    soort5 , soort5_active = crocoo1 , False
    soort6 , soort6_active = hippo1 , False

    for row_index, row in enumerate(gebruikte_maze):
        for col_index, tile in enumerate(row):
            x = col_index * muurgrootte
            y = row_index * muurgrootte
            if tile == 0:
                items.append(Object1(x, y, screen, balgrootte, WIT))
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=way_30x30))
            if tile == 32:
                items2.append(Object2(x, y, screen, balgrootte2, WIT))
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=way_30x30))
            elif tile == 1:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=resized_tile_0_4))
            elif tile == 2:
                walls.append(Muur(x, y, screen, muurgrootte, kleur=ROOD))
            elif tile == 3:
                walls.append(Muur(x, y, screen, muurgrootte, kleur=GEEL))
            elif tile == 4:
                walls.append(Muur(x, y, screen, muurgrootte, kleur=GROEN))
            elif tile == 5:
                items2.append(Object2(x, y, screen, balgrootte1, WIT))
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=way_30x30))
            elif tile == 6:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=resized_tile_0_4))
            elif tile == 7:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=yellow_green_gradient))
            elif tile == 8:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=etoue_30x30))
            elif tile == 9:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=greenbleu_30x30))
            elif tile == 10:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=etoue_30x30))
            elif tile == 11:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=etoue_30x30))
            elif tile == 31:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=etoue_30x30))
            elif tile == 99:
                walls.append(Muur(x, y, screen, muurgrootte, afbeelding=greenbleu_30x30))

        # Zoek alle lege tegels (waarde 0) in het doolhof
        lege_plekken = [(j * muurgrootte, i * muurgrootte) for i, rij in enumerate(gebruikte_maze) for j, waarde in
                        enumerate(rij) if waarde == 0]

        # Kies willekeurig een positie voor het snelheidsobject
        x_positie, y_positie = random.choice(lege_plekken)

        # Maak het snelheidsobject aan (je kan hier een afbeelding toevoegen later)
        snelheids_object = Snelheidsobject(x_positie, y_positie, screen, muurgrootte, afbeelding=speed_img)
        for item in items:
            if item.x == x_positie and item.y == y_positie:
                items.remove(item)
                break  # stop na het verwijderen
        items3.append(snelheids_object)

    speler = Speler(start_positie_x_speler1, start_positie_y_speler1, screen, WIT, radius_speler, snelheid_speler, toegelaten_posities_speler, gebruikte_maze, pacman_imgs_op_schaal)
    vijand1 = Spook(start_positie_x_soort1, start_positie_y_soort1, screen, soort1, snelheid_monster, "pinky", toegelaten_posities_vijand, gebruikte_maze, soort1_active)
    vijand2 = Spook(start_positie_x_soort2, start_positie_y_soort2, screen, soort2, snelheid_monster, "blinky", toegelaten_posities_vijand, gebruikte_maze, soort2_active)
    vijand3 = Spook(start_positie_x_soort3, start_positie_y_soort3, screen, soort3, snelheid_monster, "inky", toegelaten_posities_vijand, gebruikte_maze, soort3_active)
    vijand4 = Spook(start_positie_x_soort4, start_positie_y_soort4, screen, soort4, snelheid_monster, "clyde", toegelaten_posities_vijand, gebruikte_maze, soort4_active)
    croco = Spook(start_positie_x_soort5, start_positie_y_soort5, screen, soort5, snelheid_monster_2, "blinky", toegelaten_posities_vijand, gebruikte_maze, soort5_active)
    hippo = Spook(start_positie_x_soort6, start_positie_y_soort6, screen, soort6, snelheid_monster_2, "blinky", toegelaten_posities_vijand, gebruikte_maze, soort6_active)
    list_of_monsters = [vijand1, vijand2, vijand3, vijand4, croco, hippo]


    # Zet waarden terug
    speler.punten = huidige_score
    speler.levens = huidige_levens
    speler.eetcombo = huidige_eetcombo
    speler.gegeten_spoken_teller = huidige_spookteller

# Menu tonen
toon_menu()



# Spelers & Spoken aanmaken


if gebruikte_maze == maze1:
    init_maze1()
elif gebruikte_maze == maze2:
    init_maze2()
elif gebruikte_maze == maze3:
    init_maze3()


muur_kapotgemaakt = False


# Game-loop
# --------------------------- Hoofd Game-loop --------------------------- #
running = True
while running:
    print(len(items))  # Debug: toont hoeveel normale items er nog zijn
    tijd.tick(fps)  # Houdt het spel op vaste snelheid (frames per seconde)
    screen.fill(ZWART)  # Maak het scherm zwart voordat je alles opnieuw tekent

    # ----------------- Muren tekenen ----------------- #
    for wall in walls:
        wall.draw()

    # ----------------- Items tekenen ----------------- #
    for item in items:
        item.draw()
    for item in items2:
        item.draw()

    # ----------------- Spoken tekenen & bewegen ----------------- #
    for obj in list_of_monsters:
        obj.draw()
        obj.patrol(speler, gebruikte_maze, muurgrootte, zone1, overdracht1, zone2, overdracht2, vijand2)

        # Normale items oppakken
        for item in items[:]:
            if item.botsing(speler):
                items.remove(item)
                speler.punten += item.punten()

    # ----------------- Speciale items voor eetmodus ----------------- #
    for item in items2[:]:
        if item.botsing(speler):
            items2.remove(item)
            speler.start_eetmodus()

            # Spoken in "vlucht"-modus zetten
            for spook in list_of_monsters:
                spook.verander_type("vlucht")
                spook.removeposities(toegelaten_posities_vijand, deur_van_spoken)

    # ----------------- Botsing met spoken ----------------- #
    for spook in list_of_monsters:
        if speler.check_collision(spook):
            if speler.eetmodus_actief(tijd_van_bonus):
                speler.punten += speler.eetspook(spook, tijd_van_bonus)
                spook.verander_type(spook.oorspronkelijk_type)
            else:
                speler.levens -= 1
                speler.reset()
                for spooks in list_of_monsters:
                    spooks.reset()
                    spook.appendposities(toegelaten_posities_vijand, deur_van_spoken)
                pygame.time.delay(500)  # Korte pauze na dood

    # ----------------- Controleer of eetmodus voorbij is ----------------- #
    if not speler.eetmodus_actief(tijd_van_bonus):
        for spook in list_of_monsters:
            spook.verander_type(spook.oorspronkelijk_type)
            spook.appendposities(toegelaten_posities_vijand, deur_van_spoken)
        speler.eetcombo = 0

    # ----------------- Boost-object behandelen ----------------- #
    for item in items3[:]:
        if snelheids_object.botsing(speler):
            speler.activeer_snelheid(snelheid_snelheidboost, tijd_snelheidboost)
            items3.remove(item)
        else:
            snelheids_object.draw()

    # ----------------- Triggeracties in maze3 ----------------- #
    if gebruikte_maze == maze3 and speler.is_op_triggertegel([(24, 13), (24, 17)]):
        croco.zet_actief(True)
        hippo.zet_actief(True)

    # ----------------- Score en timers tonen ----------------- #
    score_text = font.render(f"Score: {speler.punten}", True, WIT)
    screen.blit(score_text, (tekst_punten_x, tekst_punten_y))
    speler.toon_timer(screen, font, tekst_tijd_x, tekst_tijd_y, tijd_van_bonus, WIT)

    # ----------------- Levens tonen ----------------- #
    toon_levens(screen, speler.levens)

    # ----------------- Game Over ----------------- #
    if speler.levens <= 0:
        font = pygame.font.SysFont(None, 75)
        tekst = font.render("Game Over", True, ROOD)
        screen.blit(tekst, (breedte // 2 - 150, hoogte // 2 - 40))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # ----------------- Extra tegel openen in maze3 ----------------- #
    if gebruikte_maze == maze3 and speler.punten >= 2200:
        for row_index, row in enumerate(gebruikte_maze):
            for col_index, tile in enumerate(row):
                if tile == 31:
                    gebruikte_maze[row_index][col_index] = 0
                    for muur in walls:
                        if muur.x == col_index * muurgrootte and muur.y == row_index * muurgrootte:
                            muur.afbeelding = casseau_img
                            break

    # ----------------- Eindzone zichtbaar maken per maze ----------------- #
    alle_items_opgeraakt = False
    if gebruikte_maze == maze1 and speler.punten >= 800:
        alle_items_opgeraakt = True
        pygame.draw.rect(screen, GROEN, (eindzone_x1, eindzone_y1, muurgrootte, muurgrootte))
    elif gebruikte_maze == maze2 and speler.punten >= 1500:
        alle_items_opgeraakt = True
        pygame.draw.rect(screen, GROEN, (eindzone_x2, eindzone_y2, muurgrootte, muurgrootte))
    elif gebruikte_maze == maze3 and speler.punten >= 2000:
        alle_items_opgeraakt = True
        pygame.draw.rect(screen, GROEN, (eindzone_x3, eindzone_y3, muurgrootte, muurgrootte))

    # ----------------- Levelovergang ----------------- #
    if alle_items_opgeraakt and speler.in_zone(zone_end):
        if gebruikte_maze == maze3:
            tegel_x = speler.x // muurgrootte
            tegel_y = speler.y // muurgrootte
            if gebruikte_maze[int(tegel_y)][int(tegel_x)] == 99:
                gewonnen_font = pygame.font.SysFont(None, 100)
                tekst = gewonnen_font.render("GEWONNEN!", True, (255, 255, 0))
                screen.blit(tekst, (breedte // 2 - 200, hoogte // 2 - 50))
                pygame.display.flip()
                pygame.time.delay(3000)
                running = False
        elif gebruikte_maze == maze2:
            gebruikte_maze = maze3
            init_maze3()
        elif gebruikte_maze == maze1:
            gebruikte_maze = maze2
            init_maze2()

    # ----------------- Input events ----------------- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # ----------------- Speler tekenen en bewegen ----------------- #
    speler.draw()
    speler.patrol(zone1, overdracht1, zone2, overdracht2)

    # ----------------- Extra weergave: score, timers, spoken ----------------- #
    score_text = font.render(f"Score: {speler.punten}", True, WIT)
    screen.blit(score_text, (tekst_punten_x, tekst_punten_y))
    speler.toon_timer(screen, font, tekst_tijd_x, tekst_tijd_y, tijd_van_bonus, WIT)
    speler.toon_snelheidstimer(screen, font, tekst_tijd_bonus_x, tekst_tijd_bonus_y, WIT)
    speler.toon_spook_teller(screen, font, spook_teller_x, spook_teller_y, WIT)

    # ----------------- Scherm bijwerken ----------------- #
    pygame.display.flip()

# --------------------------- Einde van spel --------------------------- #
pygame.quit()

#----------------------------------------------------------------------------------------------------------------------#
