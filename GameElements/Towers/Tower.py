
from ..GameElement import GameElement

class Tower(GameElement):
    health = 0
    attack = 0
    cost = 0
    range = 0
    firerate = 0
    level = 0
    ATTACK_VALUE = [0,0,0]
    COST = [0,0,0]
    special = 0

    def attackTarget(self):
        return self.attack
    
    def build(self):
        return self.cost
    
