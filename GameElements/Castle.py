#by Kyle

import GameElement

# Castle class
# Contains the fields health, shield, and gold
# Once health reaches 0 (or below), the player looses
# Gold is the amount of funds the player can spend on towers
class Castle(GameElement):
    CONST_MAXHEALTH = 100
    health = 0
    shield = 0
    gold = 0

    def __init__(self):
        # body of the constructor
        GameElement.setSpite("./sprites/Castle.png")
        self.health = 100
        self.shield = 50
        self.gold = 50

    def getHealth(self):
        return self.health
    
    def setHealth(self,health):
        if (health > self.CONST_MAXHEALTH):
            self.health = self.CONST_MAXHEALTH
        else:
            self.health = health
        return self.health
    
    def removeHealth(self,remove):
        self.health -= remove
        return self.health
    
    def addHealth(self,add):
        newHealth = add + self.health
        if (newHealth > self.CONST_MAXHEALTH):
            self.health = self.CONST_MAXHEALTH
        else:
            self.health = newHealth
        return self.health

    def getShield(self):
        return self.health
    
    def setShield(self,shield):
        self.shield = shield
    
    def removeShield(self,remove):
        self.shield -= remove
        return self.shield
    
    def getGold(self):
        return self.gold
    
    def setGold(self,gold):
        self.gold = gold
    
    def removeGold(self,remove):
        if (self.gold >= remove):
            self.gold -= remove
            return self.gold
        return -1
    
    def addGold(self,add):
        self.gold += add
        return self.gold