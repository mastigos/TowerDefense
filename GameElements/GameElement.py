
import pygame

class GameElement:
    sprite = 0
    locx = 0
    locy = 0
    
    def getSprite(self):
        return self.sprite

    def setSprite(self, path):
        self.sprite = path

    def getLocX(self):
        return self.locx
    
    def setLocX(self,loc):
        self.locx = loc

    def getLocY(self):
        return self.locy
    
    def setLocY(self,loc):
        self.locy = loc