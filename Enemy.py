class Enemy:
    def __init__(self, health, damage, resistances, special, speed):
        self.health = health
        self.damage = damage
        self.resistances = resistances
        self.special = special
        self.speed = speed


    def move(self):
        #do stuff


    def doSpecial(self):
        #do stuff


#Enemies

class Knight(Enemy):
    def __init__(self):
        super().__init__(health=10,damage=5,resistances=[],special="none",speed=1)

class BatteringRam(Enemy):
    def __init__(self):
        super().__init__(health=25,damage=40,resistances=[],special="none",speed=1.5)

class Cavalry(Enemy):
    def __init__(self):
        super().__init__(health=20,damage=15,resistances=[],special="none",speed=2)

class Archer(Enemy):
    def __init__(self):
        super().__init__(health=5,damage=10,resistances=[],special="none",speed=1)

class BannerCarrier(Enemy):
    def __init__(self):
        super().__init__(health=10,damage=0,resistances=[],special="banner",speed=1.5)

class Dragon(Enemy):
    def __init__(self):
        super().__init__(health=500,damage=50,resistances=[],special="firebreath",speed=1)

class Giant(Enemy):
    def __init__(self):
        super().__init__(health=1000,damage=75,resistances=[],special="stomp",speed=0.5)