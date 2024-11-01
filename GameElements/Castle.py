#by Kyle
import pygame
from pygame.examples.cursors import image


import GameElement

# Castle class
# Contains the fields health, shield, and gold
# Once health reaches 0 (or below), the player looses
# Gold is the amount of funds the player can spend on towers
class Castle:
    CONST_MAXHEALTH = 100
    health = 0
    shield = 0
    gold = 0

    def __init__(self, bg_img2, x, y, scale):
        # body of the constructor
        self.health = 100
        self.maxHealth = self.health
        self.sprite = bg_img2
        #getting width/height of the og castle img
        width = bg_img2.get_width()
        height = bg_img2.get_height()

        self.bg_img2 = pygame.transform.scale(bg_img2, (int (width*scale), int (height*scale)))

        #need a rectangle of this castle image for hit box, collision, and positioning
        self.rect = self.bg_img2.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.shield = 50
        self.gold = 50

#draw castle
    def draw(self, win):
        self.image = self.bg_img2
        win.blit(self.image, self.rect)


