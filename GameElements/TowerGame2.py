import pygame
from Enemy import Knight

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

#loading images
backgroundImage = pygame.image.load('background.png').convert_alpha()
#create castle
castleImage = pygame.image.load('Castle.png').convert_alpha()

bg = pygame.transform.scale(backgroundImage, (800, 600))

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
        self.sprite = castleImage

        self.castleImage = pygame.transform.scale(castleImage, (self.width, self.height))

        #make a rectangle
        #need a rectangle of this castle image for hit box, collision, and positioning
        self.rect = self.castleImage.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        # Castle
        self.sprite = self.castleImage
        screen.blit(self.sprite, self.rect)
        pygame.draw.rect(self.sprite, GRAY, (self.x, self.y, self.width, self.height))
        # Health bar
        pygame.draw.rect(screen, RED, (self.x, self.y - 20, (self.health / 100) * self.width, 10))
        # Shield bar
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 35, (self.shield / 50) * self.width, 10))

def drawPath(waypoints):
    for i in range(len(waypoints) - 1):
        pygame.draw.line(screen, BROWN, waypoints[i], waypoints[i + 1], 5)

def game_loop():
    castle = Castle()



    waypoints = [
        (50, 300), (200, 300), (200, 100), (400, 100), (400, 500),
        (castle.x + castle.width // 2, 500),  # Move to the same x as the castle, then move up
        (castle.x + castle.width //2 , castle.y + castle.height)
    ]

    # load enemies
    enemy_animations = []
    enemy_types = ['Knight', 'Battering Ram', 'Cavalry']
    enemy_health = [100]
    enemy_animation_types = ['walk', 'death']
    enemy_group = pygame.sprite.Group()
    castle = Castle()

    for knight in enemy_types:
        # reset temp img list
        animation_list = []
        for animation in enemy_animation_types:
            temp_list = []
            # number of frames
            frames = 30
            for i in range(frames):
                img = pygame.image.load(f'KnightWalking/Knight-and-Horse_Front-Walking-Front_{i}.png').convert_alpha()
                i_w = img.get_width()
                i_h = img.get_height()
                img = pygame.transform.scale(img, (int(i_w * 0.4), (int(i_h * 0.4))))
                temp_list.append(img)
            animation_list.append(temp_list)
        enemy_animations.append(animation_list)


    knight = Knight()
    enemy_group.add(knight)

    running = True
    while running:
        screen.fill(DARK_GREEN)
        drawGrid()
        screen.blit(bg, (0, 0))
        # draw enemies
        enemy_group.update(screen, castle.castleImage)
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
