# Simple pygame program


# import

import pygame

pygame.init()


# make screen

screen = pygame.display.set_mode([500, 500])


# run

running = True

while running:


    # quit

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # background

    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)


    # Flip the display

    pygame.display.flip()


# Done! Time to quit.

pygame.quit()