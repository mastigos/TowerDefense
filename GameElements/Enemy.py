import pygame
import spritesheet
from pygame.examples.cursors import image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, damage, resistances, special, speed, corpseValue, animation_list, start_x=0, start_y=300):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.damage = damage
        self.resistances = resistances
        self.special = special
        self.animation_list = animation_list
        self.speed = speed
        self.corpseValue = corpseValue
        self.x = start_x
        self.y = start_y
        self.current_waypoint = 0  # waypoint index
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # starting img
        self.sprite = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0, 0, 70, 105)
        self.rect.center = (self.x, self.y)

    def update(self, surface, target):

            # move enemy
            self.rect.x -= self.speed
            self.update_animation()
            image_surface = pygame.image.load('KnightWalking/Knight-and-Horse_Front-Walking-Front_1.png').convert_alpha()
            # draw img
            pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)
            surface.blit(image_surface, self.rect)

    def update_animation(self):
        #animation cooldown
        ANIMATION_COOLDOWN = 50
        #update img based on current action
        self.sprite = self.animation_list[self.action][self.frame_index]

        #check time between frames
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #loop through image index
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def move(self, waypoints):

        if self.current_waypoint < len(waypoints):
            target_x, target_y = waypoints[self.current_waypoint]


            if self.x < target_x:  # Move right
                self.x += min(self.speed, target_x - self.x)
            elif self.x > target_x:  # Move left
                self.x -= min(self.speed, self.x - target_x)
            elif self.y < target_y:  # Move down
                self.y += min(self.speed, target_y - self.y)
            elif self.y > target_y:  # Move up
                self.y -= min(self.speed, self.y - target_y)


            if (self.x, self.y) == (target_x, target_y):
                self.current_waypoint += 1

    def draw(self, screen):

        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), 10)  # Blue circle for Knight

    def doSpecial(self):
        pass

# Enemies
class Knight(Enemy):
    def __init__(self):
        super().__init__(health=10, damage=5, resistances=[], special="none", animation_list = ["KnightWalking/Knight-and-Horse_Front-Walking-Front_1.png"],   speed=3, corpseValue=5)

class BatteringRam(Enemy):
    def __init__(self):
        super().__init__(health=25, damage=40, resistances=[], special="none", speed=1.5, corpseValue=20)

class Cavalry(Enemy):
    def __init__(self):
        super().__init__(health=20, damage=15, resistances=[], special="none", speed=2, corpseValue=15)

class Archer(Enemy):
    def __init__(self):
        super().__init__(health=5, damage=10, resistances=[], special="none", speed=1, corpseValue=3)

class BannerCarrier(Enemy):
    def __init__(self):
        super().__init__(health=10, damage=0, resistances=[], special="banner", speed=1.5, corpseValue=7)

class Dragon(Enemy):
    def __init__(self):
        super().__init__(health=500, damage=50, resistances=[], special="firebreath", speed=1, corpseValue=150)

class Giant(Enemy):
    def __init__(self):
        super().__init__(health=1000, damage=75, resistances=[], special="stomp", speed=0.5, corpseValue=150)
