
from ..GameElement import GameElement
from pygame.examples.cursors import image
import math

class Tower(GameElement):
    health = 0
    attack = 0
    cost = 0
    rangeElement = 0
    firerate = 0
    level = 0
    ATTACK_VALUE = [0,0,0]
    COST = [0,0,0]
    target = 0

    def attackTarget(self):
        #launch at target
        
        return self.attack
    
    def build(self):
        return self.cost

    def target(self,range, ememies):
        closest = range*40
        for ememy in ememies:
            dist = math.hypot(self.locx-ememy.locx, self.locy-ememy.locy)
            if dist < closest:
                dist = closest
                self.target = ememy
        
