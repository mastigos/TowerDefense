from .Tower import Tower

class Cannon(Tower):
    ATTACK_VALUE = [3,5,10]
    COST = [15,25,40]

    def __init__(self):
        self.health = 60
        self.cost = self.COST[1]
        self.attack = self.ATTACK_VALUE[0]
        self.range = 2
        self.firerate = 2
        self.level = 1
        Tower.COST = [15,25,40]
        Tower.ATTACK_VALUE = [3,5,10]
