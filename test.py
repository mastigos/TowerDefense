import pygame
from GameElements.Enemy import Knight, Soldier, Dragon
from GameElements.Map import Map
from GameElements.Tower import Cannon, Catapult, Ballista, CaltropsDispenser, KnightsBarracks, HolyChapel

pygame.init()

# Screen settings
WIDTH, HEIGHT = 780, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

# Game clock
clock = pygame.time.Clock()
FPS = 30

background = pygame.image.load("GameSprites/background.png")
bg = pygame.transform.scale(background, (WIDTH, HEIGHT))

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

# Set the gold font
goldfont = pygame.font.SysFont('Corbel',35)

# Grid
def drawGrid():
    blockSize = 30  # Grid block size
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BROWN, rect, 1)


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

        self.original_image = pygame.image.load("GameSprites/Castle/Castle.png").convert_alpha()
        self.resized_image = pygame.transform.scale(self.original_image, (200, 200))
        self.image = pygame.transform.flip(self.resized_image, True, False)
        self.image_rect = self.image.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

    def draw(self):
        # Castle
        screen.blit(self.image, self.image_rect.topleft)
        # Health bar
        pygame.draw.rect(screen, RED, (self.x, self.y - 20, (self.health / 100) * self.width, 10))
        # Shield bar
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 35, (self.shield / 50) * self.width, 10))


def drawPath(screen, waypoints, path_image, block_size):
    for i in range(len(waypoints) - 1):
        start_x, start_y = waypoints[i]
        end_x, end_y = waypoints[i + 1]

        x, y = start_x, start_y
        path_image = pygame.image.load("GameSprites/pathTile80x80.png").convert_alpha()
        path_image = pygame.transform.scale(path_image, (30, 30))

        while (x, y) != (end_x, end_y):
            screen.blit(path_image, (x, y))

            if x < end_x:
                x += block_size
            elif x > end_x:
                x -= block_size

            if y < end_y:
                y += block_size
            elif y > end_y:
                y -= block_size

        # Place final tile
        screen.blit(path_image, (end_x, end_y))


def display_build_ui(player_gold):
        font = pygame.font.SysFont("Arial", 24)

        ui_width = 200
        ui_height = 150
        pygame.draw.rect(screen, (200, 200, 200), (WIDTH - ui_width, 0, ui_width, ui_height))

        tower_data = [
            ("Cannon", 15, Cannon),
            ("Catapult", 25, Catapult),
            ("Ballista", 40, Ballista),
            ("Caltrops", 20, CaltropsDispenser),
            ("Knights Barracks", 50, KnightsBarracks),
            ("Holy Chapel", 30, HolyChapel),
        ]

        y_offset = 20
        selected_tower = None
        for name, cost, tower_class in tower_data:
            color = GREEN if cost <= player_gold else RED
            text = font.render(f"{name}: {cost} Gold", True, color)
            screen.blit(text, (WIDTH - ui_width + 10, y_offset))
            y_offset += 30

            if color == GREEN and selected_tower is None:
                if pygame.mouse.get_pressed()[0]:
                    if y_offset - 30 < pygame.mouse.get_pos()[1] < y_offset:
                        selected_tower = tower_class(level=1)

                        # Build the selected tower
                        row, col = 5, 5  # Replace with actual row, col logic
                        player_gold = map.build_tower(selected_tower, row, col, player_gold)

        return player_gold


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

def wave_table(waves, enemy):
    castle = Castle
    waypoints = [
        (0, 300), (200, 300), (200, 100), (400, 100), (400, 500),
        (castle.x + castle.width // 2, 500),
        (castle.x + castle.width // 2, castle.y + castle.height)
    ]
    knight = Knight
    soldier = Soldier
    dragon = Dragon
    waves = {
        1: [knight, knight, soldier, soldier, knight, knight, knight, knight, soldier, soldier, soldier, dragon],
        2: [knight, knight, soldier, soldier, knight, knight, knight, knight, soldier, soldier, soldier, dragon, dragon, knight, knight, soldier, soldier, knight, knight, knight, knight, soldier, soldier, soldier, dragon, dragon],
        3: [knight, knight, soldier, soldier, knight, knight, knight, knight, soldier, soldier, soldier, dragon, dragon, dragon, knight, knight, soldier, soldier, knight, knight, knight, knight, soldier, soldier, soldier, dragon, dragon, dragon, knight, knight, soldier, soldier, knight, knight, knight, knight, soldier, soldier, soldier, dragon, dragon, dragon, dragon]
     }

    for enemy in waves.values():
        new_enemy = enemy
        enemy.append(new_enemy)
        enemy.move(waypoints)
        enemy.update_animation()
        enemy.draw(screen)

def start_wave(waves):
    waves_len = len(waves)
    enemies_len = len(waves.get(1))
    if waves_len != 4:
        for enemies in waves.values():
            current_wave = waves.index(enemies)
            wave_end = enemies_len - current_wave
            if wave_end != 1:
                next_wave = current_wave + 1
                next_wave = current_wave
                enemies_len = len(waves.get(current_wave))
                wave_end = enemies_len - current_wave
    else:
        print (f"you win!")

def start_screen():

    font = pygame.font.SysFont("Arial", 48)
    sub_font = pygame.font.SysFont("Arial", 24)


    screen.blit(bg, (0, 0))
    title_text = font.render("Tower Defense", True, BLUE)
    start_text = sub_font.render("Press SPACE to Start", True, BLACK)


    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

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

    global player_gold
    goldfont = pygame.font.SysFont('Courier', 30)





    running = True
    while running:


        map.draw(screen)

        gold = "Gold: " + str(player_gold)
        goldtext = goldfont.render(gold, True, (255,215,0))

        screen.blit(goldtext, (20, 20))

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
                        map.build(selected_tower, row, col, player_gold)
                        tower_costs = {
                            Cannon: 15,
                            Catapult: 25,
                            Ballista: 40,
                            CaltropsDispenser: 20,
                            KnightsBarracks: 50,
                            HolyChapel: 30
                        }
                        towers.append(selected_tower)
                        player_gold -= tower_costs.get(type(selected_tower))
                        selected_tower = None
                        selected_tile = None

        if show_ui:
            draw_ui(screen, ui_mouse_x, ui_mouse_y)



        castle.draw()



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
                player_gold += enemy.corpseValue

            enemy.draw_health_bar(screen)


        current_time = pygame.time.get_ticks()
        for tower in towers:
            tower.update(enemies, current_time)

            for projectile in tower.projectiles:
                pygame.draw.circle(screen, (200, 0, 0), (int(projectile.x), int(projectile.y)), 3)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
start_screen()
game_loop()
