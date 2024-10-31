
from .Tower import Tower

class Ballista(Tower):
    ATTACK_VALUE = [15,20,25]
    COST = [40,60,80]

    def __init__(self):
        self.health = 60
        self.cost = self.COST[1]
        self.attack = self.ATTACK_VALUE[0]
        self.range = 2
        self.firerate = 3
        self.level = 1
        Tower.COST = [15,25,40]
        Tower.ATTACK_VALUE = [3,5,10]

