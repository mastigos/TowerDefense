from GameElement import GameElement
from pygame.draw import circle
import pygame

class rangeElement(GameElement):
    radius = 0

    def draw(self,window):
        pygame.draw.circle(window,tuple(100,100,100,0.7),[self.locx,self.locy],self.radius)