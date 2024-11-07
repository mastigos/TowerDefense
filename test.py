import pygame
from GameElements.Enemy import Knight

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

# Grid
def drawGrid():
    blockSize = 20  # Grid block size
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, GRAY, rect, 1)

# Castle
class Castle:
    def __init__(self):
        blockSize = 20
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

def game_loop():
    castle = Castle()
    knight = Knight()


    waypoints = [
        (50, 300), (200, 300), (200, 100), (400, 100), (400, 500),
        (castle.x + castle.width // 2, 500),  # Move to the same x as the castle, then move up
        (castle.x + castle.width //2 , castle.y + castle.height)
    ]

    running = True
    while running:
        screen.fill(DARK_GREEN)
        drawGrid()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        drawPath(waypoints)

        castle.draw()

        knight.move(waypoints)
        pygame.draw.circle(screen, BLUE, (int(knight.x), int(knight.y)), 10)





        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

game_loop()
