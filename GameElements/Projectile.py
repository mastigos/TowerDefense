import math

class Projectile:
    def __init__(self, start_x, start_y, target, damage):
        self.x = start_x
        self.y = start_y
        self.target = target
        self.damage = damage
        self.speed = 5

    def move_towards_target(self):
        if self.target.x > self.x:
            self.x += self.speed
        elif self.target.x < self.x:
            self.x -= self.speed
        if self.target.y > self.y:
            self.y += self.speed
        elif self.target.y < self.y:
            self.y -= self.speed

        print(f"Projectile moving to: ({self.x}, {self.y})")


    def check_collision(self):
        distance_to_target = ((self.x - self.target.x) ** 2 + (self.y - self.target.y) ** 2) ** 0.5
        if distance_to_target < 30:
            self.target.take_damage(self.damage)
            return True
        return False

