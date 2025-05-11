# Import
import pygame
import time
#import update

from Hulpfuncties import MazeChecker
#from Main_loop import gebruikte_maze
global walls


#----------------------------------------------------------------------------------------------------------------------#
refactor = 1
muurgrootte = 30
# speler
snelheid_speler = 5
radius_speler = 14
levens = 3
tijd_snelheidboost = 7000
snelheid_snelheidboost = 1.5

#----------------------------------------------------------------------------------------------------------------------#

# Klasse die de speler representeert en beweging/leven/overdracht regelt
class Speler:
    def __init__(self, x, y, scherm, kleur , straal, snelheid , toegelaten_posities , gebruikte_maze , afbeelding = None):
        self.x, self.y = (round(x/5)*5) , (round(y/5)*5)
        self.scherm = scherm
        self.kleur = kleur
        self.straal = straal
        self.snelheid = snelheid
        self.toegelaten_posities = toegelaten_posities
        self.gebruikte_maze = gebruikte_maze
        self.afbeelding = afbeelding

        self.snelheid_standaard = snelheid  # Bewaar de normale snelheid
        self.startpositie = ((round(x/5)*5) , (round(y/5)*5))
        self.levens = 3
        self.punten = 0
        self.eetcombo = 0
        self.gegeten_spoken_teller = 0

        self.timer = None
        self.timer_duur = None
        self.snelheid_timer = None  # Start op None, wordt gevuld bij boost
        self.snelheid_duur = 5000
        self.snelheid_duur = 5000
        #self.break_walls = False  # power-up: muren kapot

        self.richting = None  # Toegevoegd: huidige richting ("UP", "DOWN", etc.)
        self.richting2 = "rechts"  # standaard richting voor pacman
        self.animatie_index = 0
        self.animatie_teller = 0

#------------------------------------------------Speler_tekenen--------------------------------------------------------#
    def draw(self):
        if self.afbeelding:
            img = self.afbeelding[self.animatie_index]

            # Afbeelding roteren op basis van richting
            if self.richting2 == "rechts":
                rotated = img
            elif self.richting2 == "links":
                rotated = pygame.transform.flip(img, True, False)
            elif self.richting2 == "omhoog":
                rotated = pygame.transform.rotate(img, 90)
            elif self.richting2 == "omlaag":
                rotated = pygame.transform.rotate(img, -90)
            else:
                rotated = img  # fallback bij geen richting

            rect = rotated.get_rect(center=(self.x, self.y))
            self.scherm.blit(rotated, rect)
        else:
            # Fallback: gewone cirkel als geen afbeelding beschikbaar is
            pygame.draw.circle(self.scherm, self.kleur, (int(self.x), int(self.y)), self.straal)

    def update_animatie(self):
        self.animatie_teller += 1
        if self.animatie_teller % 5 == 0:
            self.animatie_index = (self.animatie_index + 1) % len(self.afbeelding)

#----------------------------------------------Speler_bewegen----------------------------------------------------------#

    def Controleren(self, posities):
        maze_checker = MazeChecker(self.gebruikte_maze, muurgrootte)
        for coordinaat_x, coordinaat_y in posities:
            if not maze_checker.is_valid(coordinaat_x, coordinaat_y, self.toegelaten_posities):
                return False
        return True

    def move(self, snelheid_x, snelheid_y):
        # Richting bepalen (voor animatie)
        if snelheid_x > 0:
            self.richting2 = "rechts"
        elif snelheid_x < 0:
            self.richting2 = "links"
        elif snelheid_y < 0:
            self.richting2 = "omhoog"
        elif snelheid_y > 0:
            self.richting2 = "omlaag"

        import math

        stappen = math.ceil(max(abs(snelheid_x), abs(snelheid_y)))
        stap_x = snelheid_x / stappen if stappen != 0 else 0
        stap_y = snelheid_y / stappen if stappen != 0 else 0

        for _ in range(stappen):
            tussen_x = self.x + stap_x
            tussen_y = self.y + stap_y


            te_controleren_posities = [
                (tussen_x + self.straal, tussen_y + self.straal),
                (tussen_x + self.straal, tussen_y - self.straal),
                (tussen_x - self.straal, tussen_y + self.straal),
                (tussen_x - self.straal, tussen_y - self.straal)
            ]

            if self.Controleren(te_controleren_posities):
                self.x = tussen_x
                self.y = tussen_y
            else:
                break  # Stoppen bij botsing

        self.update_animatie()


    def patrol(self, zone1, overdracht1, zone2, overdracht2):
        self.update_snelheid()
        self.overdracht(zone1, overdracht1, zone2, overdracht2)
        keys = pygame.key.get_pressed()
        nieuw_x, nieuw_y = self.x + self.snelheid, self.y + self.snelheid
        te_controleren_posities = [
            (nieuw_x + self.straal, nieuw_y + self.straal),
            (nieuw_x + self.straal, nieuw_y - self.straal),
            (nieuw_x - self.straal, nieuw_y + self.straal),
            (nieuw_x - self.straal, nieuw_y - self.straal)
        ]

        # Update richting bij nieuwe toetsaanslagen
        if keys[pygame.K_DOWN]:
            nieuw_x, nieuw_y = self.x, self.y + self.snelheid
            te_controleren_posities = [(nieuw_x + self.straal, nieuw_y + self.straal), (nieuw_x - self.straal, nieuw_y + self.straal)]
            if self.Controleren(te_controleren_posities):
                self.richting = "DOWN"

        elif keys[pygame.K_UP]:
            nieuw_x, nieuw_y = self.x, self.y - self.snelheid
            te_controleren_posities = [(nieuw_x + self.straal, nieuw_y - self.straal), (nieuw_x - self.straal, nieuw_y - self.straal)]
            if self.Controleren(te_controleren_posities):
                self.richting = "UP"

        elif keys[pygame.K_LEFT]:
            nieuw_x, nieuw_y = self.x - self.snelheid, self.y
            te_controleren_posities = [(nieuw_x - self.straal, nieuw_y + self.straal), (nieuw_x - self.straal, nieuw_y - self.straal)]
            if self.Controleren(te_controleren_posities):
                self.richting = "LEFT"

        elif keys[pygame.K_RIGHT]:
            nieuw_x, nieuw_y = self.x + self.snelheid, self.y
            te_controleren_posities = [(nieuw_x + self.straal, nieuw_y + self.straal), (nieuw_x + self.straal, nieuw_y - self.straal)]
            if self.Controleren(te_controleren_posities):
                self.richting = "RIGHT"

        # Blijf bewegen in huidige richting
        if self.richting == "DOWN":
            self.move(0, self.snelheid)
        elif self.richting == "UP":
            self.move(0, -self.snelheid)
        elif self.richting == "LEFT":
            self.move(-self.snelheid, 0)
        elif self.richting == "RIGHT":
            self.move(self.snelheid, 0)

    def reset(self):
        self.x, self.y = self.startpositie

    def in_zone(self, zone):
        zone_x, zone_y, zone_breedte, zone_hoogte = zone
        if None in zone:
            return False
        return zone_x <= self.x <= zone_x + zone_breedte and zone_y <= self.y <= zone_y + zone_hoogte

    def overdracht(self, zone1, overdracht1, zone2, overdracht2):
        if self.in_zone(zone1):
            self.x, self.y = overdracht1


#-----------------------------------------------Speler_eten/botsing----------------------------------------------------#

    def check_collision(self, spook):
        speler_rect = pygame.Rect(self.x - self.straal + 3, self.y - self.straal + 3, (self.straal - 4) * 2,
                                  (self.straal - 4) * 2)
        return speler_rect.colliderect(spook.rect)

    def eetspook(self, spook , tijd_van_bonus):
        if self.eetmodus_actief(tijd_van_bonus) and self.check_collision(spook):
            self.eetcombo += 1
            punten = 50 * self.eetcombo
            self.gegeten_spoken_teller += 1

            # Check op extra leven
            if self.gegeten_spoken_teller >= 10:
                self.levens += 1
                self.gegeten_spoken_teller = 0  # Reset teller

            spook.reset()
            return punten
        return 0

#-----------------------------------------------Speler_start-----------------------------------------------------------#

    def start_eetmodus(self):
        self.timer = time.time()  # actieve eetmodus met echte tijd
        self.eetcombo = 0  # reset combo wanneer nieuwe modus start

    def start_timer(self, duur_in_seconden):
        self.timer = pygame.time.get_ticks()
        self.timer_duur = duur_in_seconden * 1000  # omzetten naar milliseconden

    def activeer_snelheid(self, boost, duur):
        self.snelheid = self.snelheid_standaard + boost
        self.snelheid_timer = pygame.time.get_ticks()
        self.snelheid_duur = duur

#-----------------------------------------------Speler_tools-----------------------------------------------------------#

    def is_op_triggertegel(self, tegels):
        tegel_x = self.x // muurgrootte
        tegel_y = self.y // muurgrootte
        return (tegel_x, tegel_y) in tegels

    def eetmodus_actief(self, tijd_van_bonus):
        if self.timer is None:
            return False
        if time.time() - self.timer <= tijd_van_bonus:  # 30 seconden duren
            return True
        else:
            self.timer = None  # Zet terug naar None als tijd voorbij is
            return False

    def update_snelheid(self):
        if self.snelheid_timer and pygame.time.get_ticks() - self.snelheid_timer > self.snelheid_duur:
            self.snelheid = self.snelheid_standaard
            self.snelheid_timer = None



#---------------------------------------Toonfuncties-------------------------------------------------------------------#

    def toon_timer(self, scherm, font , x_positie, y_positie , tijd_van_bonus , kleur):
        if self.eetmodus_actief(tijd_van_bonus):
            resterende_tijd = max(0, int(tijd_van_bonus - (time.time() - self.timer)))
            tekst = font.render(f"Eetmodus: {resterende_tijd}s", True, kleur)  # Gele tekst
            scherm.blit(tekst, (x_positie, y_positie))  # Positie linksboven

    def toon_snelheidstimer(self, scherm, font, x_positie, y_positie, kleur):
        if self.snelheid_timer:
            verstreken = pygame.time.get_ticks() - self.snelheid_timer
            resterende_ms = max(0, self.snelheid_duur - verstreken)
            resterende_seconden = int(resterende_ms / 1000)
            if resterende_seconden > 0:
                tekst = font.render(f"Boost: {resterende_seconden}s", True, kleur)
                scherm.blit(tekst, (x_positie, y_positie))

    def toon_spook_teller(self, scherm, font, x, y, kleur):
        tekst = font.render(f"Spoken: {self.gegeten_spoken_teller}/10", True, kleur)
        scherm.blit(tekst, (x, y))

