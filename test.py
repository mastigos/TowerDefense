import pygame
from GameElements.Enemy import Knight
from GameElements.Map import Map
from GameElements.Tower import Cannon, Catapult, Ballista, CaltropsDispenser, KnightsBarracks, HolyChapel

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

# Game clock
clock = pygame.time.Clock()
FPS = 30

# Colors
DARK_GREEN = (34, 139, 34)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)

# Player resources
player_gold = 100  # Initialize player's gold for building towers

# Grid
def drawGrid():
    blockSize = 30  # Grid block size
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, GRAY, rect, 1)

# Castle
class Castle:
    def __init__(self):
        blockSize = 30
        self.health = 100
        self.shield = 50
        self.width = 5 * blockSize  # Align to grid
        self.height = 5 * blockSize  # Ditto

        self.x = WIDTH - self.width - (WIDTH % blockSize) - (5 * blockSize)
        self.y = ((HEIGHT // 2) // blockSize) * blockSize  # Snap to grid

    def draw(self):
        # Castle
        pygame.draw.rect(screen, GRAY, (self.x, self.y, self.width, self.height))
        # Health bar
        pygame.draw.rect(screen, RED, (self.x, self.y - 20, (self.health / 100) * self.width, 10))
        # Shield bar
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 35, (self.shield / 50) * self.width, 10))

def drawPath(waypoints):
    for i in range(len(waypoints) - 1):
        pygame.draw.line(screen, BROWN, waypoints[i], waypoints[i + 1], 5)

def display_build_ui(player_gold):

    font = pygame.font.SysFont("Arial", 24)


    ui_width = 200
    ui_height = 150
    pygame.draw.rect(screen, (200, 200, 200), (WIDTH - ui_width, 0, ui_width, ui_height))

    tower_data = [
        ("Cannon", 15),
        ("Catapult", 25),
        ("Ballista", 40),
        ("Caltrops", 20),
        ("Knights Barracks", 50),
        ("Holy Chapel", 30),
    ]

    y_offset = 20
    selected_tower = None
    for name, cost in tower_data:
        color = GREEN if cost <= player_gold else RED
        text = font.render(f"{name}: {cost} Gold", True, color)
        screen.blit(text, (WIDTH - ui_width + 10, y_offset))
        y_offset += 30

        if color == GREEN and selected_tower is None:
            if pygame.mouse.get_pressed()[0]:
                if y_offset - 30 < pygame.mouse.get_pos()[1] < y_offset:
                    if name == "Cannon":
                        selected_tower = Cannon(level=1)
                    elif name == "Catapult":
                        selected_tower = Catapult(level=1)
                    elif name == "Ballista":
                        selected_tower = Ballista(level=1)
                    elif name == "Caltrops":
                        selected_tower = CaltropsDispenser(level=1)
                    elif name == "Knights Barracks":
                        selected_tower = KnightsBarracks(level=1)
                    elif name == "Holy Chapel":
                        selected_tower = HolyChapel(level=1)

    return selected_tower

def draw_ui(screen, mouse_x, mouse_y):

    tower_ui_width = 200
    tower_ui_height = 120
    tower_ui_x = mouse_x
    tower_ui_y = mouse_y

    pygame.draw.rect(screen, (255, 255, 255), (tower_ui_x, tower_ui_y, tower_ui_width, tower_ui_height))

    pygame.draw.rect(screen, (255, 0, 0), (tower_ui_x + 10, tower_ui_y + 10, 180, 30))
    pygame.draw.rect(screen, (0, 255, 0), (tower_ui_x + 10, tower_ui_y + 40, 180, 30))
    pygame.draw.rect(screen, (0, 0, 255), (tower_ui_x + 10, tower_ui_y + 70, 180, 30))

    font = pygame.font.SysFont(None, 24)
    font_render = font.render("Cannon", True, (0, 0, 0))
    screen.blit(font_render, (tower_ui_x + 75, tower_ui_y + 15))
    font_render = font.render("Catapult", True, (0, 0, 0))
    screen.blit(font_render, (tower_ui_x + 65, tower_ui_y + 45))
    font_render = font.render("Ballista", True, (0, 0, 0))
    screen.blit(font_render, (tower_ui_x + 70, tower_ui_y + 75))

def game_loop():
    castle = Castle()
    knight = Knight()
    waypoints = [
        (0, 300), (200, 300), (200, 100), (400, 100), (400, 500),
        (castle.x + castle.width // 2, 500),
        (castle.x + castle.width // 2, castle.y + castle.height)
    ]

    map = Map(WIDTH, HEIGHT, 30, waypoints, castle)

    selected_tower = None
    show_ui = False
    ui_mouse_x = 0
    ui_mouse_y = 0
    selected_tile = None

    towers = []
    enemies = []




    running = True
    while running:
        screen.fill(DARK_GREEN)
        map.draw(screen)
        drawGrid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // map.block_size
                col = mouse_x // map.block_size

                if map.tileMap[row][col] == 0 and not show_ui:
                    show_ui = True
                    ui_mouse_x = mouse_x
                    ui_mouse_y = mouse_y
                    selected_tile = (row, col)

                if show_ui:
                    if ui_mouse_x + 10 <= mouse_x <= ui_mouse_x + 190:
                        if ui_mouse_y + 10 <= mouse_y <= ui_mouse_y + 40:
                            selected_tower = Cannon()
                            show_ui = False
                        elif ui_mouse_y + 40 <= mouse_y <= ui_mouse_y + 70:
                            selected_tower = Catapult()
                            show_ui = False
                        elif ui_mouse_y + 70 <= mouse_y <= ui_mouse_y + 100:
                            selected_tower = Ballista()
                            show_ui = False

                if selected_tower and selected_tile:
                    row, col = selected_tile
                    if map.tileMap[row][col] == 0:
                        map.build(selected_tower, row, col)
                        towers.append(selected_tower)
                        selected_tower = None
                        selected_tile = None

        if show_ui:
            draw_ui(screen, ui_mouse_x, ui_mouse_y)

        castle.draw()
        drawPath(waypoints)


        if pygame.time.get_ticks() % 5000 < 50:
            new_enemy = Knight()
            enemies.append(new_enemy)

        for enemy in enemies:
            enemy.move(waypoints)
            enemy.update_animation()
            enemy.draw(screen)


            if castle.x <= enemy.x <= castle.x + castle.width and castle.y <= enemy.y <= castle.y + castle.height:
                if castle.shield > 0:
                    castle.shield -= enemy.damage
                else:
                    castle.health -= enemy.damage
                enemies.remove(enemy)


            if enemy.health < 1:
                enemies.remove(enemy)

            enemy.draw_health_bar(screen)


        current_time = pygame.time.get_ticks()
        for tower in towers:
            tower.update(enemies, current_time)

            for projectile in tower.projectiles:
                pygame.draw.circle(screen, (200, 0, 0), (int(projectile.x), int(projectile.y)), 3)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
game_loop()