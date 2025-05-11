# Import
import pygame
import heapq

interval = 5

#----------------------------------------------------------------------------------------------------------------------#

# Checkt  of de vijand/Speler op de 'tegel' mag gaan
class MazeChecker:
    def __init__(self, maze, afmeting):
        self.maze = maze
        self.afmeting = afmeting

    def is_valid(self, x, y , toegelaten_posities):
        kol = int(x // self.afmeting)
        rij = int(y // self.afmeting)
        if self.maze[rij][kol] in toegelaten_posities:
            return True
        return False

#----------------------------------------------------------------------------------------------------------------------#

# Maze inlezen (29x19)
def maze_van_bestand(bestand):
    document = []
    file = open(bestand, 'r')
    for lijn in file:
        lijn = lijn.strip().split()
        lijn = [int(cijfer) for cijfer in lijn]
        document.append(lijn)
    file.close()
    return document

#----------------------------------------------------------------------------------------------------------------------#

# nakijken of er een botsing is tussen een speler en spook
def check_collision2(speler, spook):
    # Maak een rechthoek voor de speler op basis van zijn positie en straal
    speler_rect = pygame.Rect(speler.x - speler.radius, speler.y - speler.radius, speler.radius * 2, speler.radius * 2)

    # Controleer of de speler's rechthoek botst met de rechthoek van het spook
    if speler_rect.colliderect(spook.rect):
        return True  # Als er een botsing is, retourneer True
    else:
        return False  # Als er geen botsing is, retourneer False

#----------------------------------------------------------------------------------------------------------------------#

# Checkt of speler en spook: leeuwen etc voila botsen met elkaar
def check_collision(speler, spook):
    speler_rect = pygame.Rect(speler.x - speler.radius, speler.y - speler.radius , speler.radius-interval, speler.radius+interval)
    return speler_rect.colliderect(spook.rect)

#----------------------------------------------------------------------------------------------------------------------#

# Teken hartjes linksboven misschien later voor elk niveau iets anders
def toon_levens(screen, levens):
    hart_afbeelding = pygame.image.load("LEVEL 3/hart1.png")
    hart_afbeelding = pygame.transform.scale(hart_afbeelding, (25, 25))
    for i in range(levens):
        screen.blit(hart_afbeelding, (10 + i * 35, 10))
    # de functie algemener maken

#----------------------------------------------------------------------------------------------------------------------#

def herstart_spel(speler, spoken , levens):
    speler.levens -= 3
    speler.reset()
    for spook in spoken:
        spook.reset()
        spook.pad = []         #  Leeg het oude pad
        spook.doel_index = 0   #  Zet index terug op 0 zodat hij direct herberekent
    pygame.time.delay(1000)
    # verloren leven , time.delay

#----------------------------------------------------------------------------------------------------------------------#
# jai rajouter le functie ici au lieux detre dans settings
def a_star(maze, start, goal, tile_size, toegelaten_posities_vijand):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    rows, cols = len(maze), len(maze[0])
    start_tile = (start[1] // tile_size, start[0] // tile_size)
    goal_tile = (goal[1] // tile_size, goal[0] // tile_size)

    frontier = [(0, start_tile)]
    came_from = {start_tile: None}
    cost_so_far = {start_tile: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal_tile:
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current[0] + dy, current[1] + dx
            if 0 <= nx < rows and 0 <= ny < cols and maze[int(nx)][int(ny)] in toegelaten_posities_vijand: # welke vakjes de spook mag bewegen
                next_tile = (int(nx), int(ny))
                new_cost = cost_so_far[current] + 1
                if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                    cost_so_far[next_tile] = new_cost
                    priority = new_cost + heuristic(goal_tile, next_tile)
                    heapq.heappush(frontier, (priority, next_tile))
                    came_from[next_tile] = current

    path = []
    current = goal_tile
    while current != start_tile:
        if current in came_from:
            path.append((current[1] * tile_size + tile_size//2, current[0] * tile_size + tile_size//2))
            current = came_from[current]
        else:
            return []
    path.reverse()
    return path