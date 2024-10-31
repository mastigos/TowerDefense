import pygame
from Castle import Castle
pygame.init()

#setting window demensions
window_width = 800
window_height = 1000
win=pygame.display.set_mode((window_height, window_width))
pygame.display.set_caption('Medieval Tower Defense')

#Setting games FPS
clock = pygame.time.Clock()
FPS = 60

#loading imgs
bg_img1= pygame.image.load('background.png').convert()
#castle img
bg_img2= pygame.image.load('Castle.png').convert_alpha()
bg =pygame.transform.scale(bg_img1, (1000, 800))

#create castle
castle = Castle(bg_img2, window_width - 800, window_height - 800, 0.2)
#main game loop
run= True
while run:

    clock.tick(FPS)
    #create window
    win.blit(bg, (0, 0))

    #draw Castle
    castle.draw(win)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #update display window
        pygame.display.update()


