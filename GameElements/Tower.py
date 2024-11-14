import pygame
from GameElements.Projectile import Projectile

class Tower:
    def __init__(self, health, cost, attack, range, firerate, level=1, x=0, y=0):
        self.health = health
        self.cost = cost
        self.attack = attack
        self.range = range
        self.firerate = firerate
        self.level = level
        self.x = x
        self.y = y
        self.last_shot_time = 0
        self.projectiles = []

    def update(self, enemies, current_time):
        if current_time - self.last_shot_time >= 1000 / self.firerate:
            nearest_enemy = self.get_nearest_enemy(enemies)
            if nearest_enemy:
                distance = ((nearest_enemy.x - self.x) ** 2 + (nearest_enemy.y - self.y) ** 2) ** 0.5
                if distance <= self.range:
                    projectile = Projectile(self.x, self.y, nearest_enemy, self.attack)
                    self.projectiles.append(projectile)
                    self.last_shot_time = current_time
                    print(f"Firing a projectile at Enemy({nearest_enemy.x}, {nearest_enemy.y}).")
                else:
                    print("No enemies within range.")
            else:
                print("No nearest enemy found.")

        for projectile in self.projectiles[:]:
            projectile.move_towards_target()
            if projectile.check_collision():
                self.projectiles.remove(projectile)
                print("Projectile collided and was removed.")

    def get_nearest_enemy(self, enemies):
        nearest_enemy = None
        print(f"Tower range: {self.range}")
        min_distance = self.range
        print(f"Tower Position: ({self.x}, {self.y})")
        for enemy in enemies:
            print(f"Enemy Position: ({enemy.x}, {enemy.y})")


            distance = ((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2) ** 0.5


            print(f"Checking enemy at ({enemy.x}, {enemy.y}), distance: {distance}")


            if distance <= self.range and (nearest_enemy is None or distance < min_distance):
                nearest_enemy = enemy
                min_distance = distance

        if nearest_enemy:
            print(f"Nearest enemy found at ({nearest_enemy.x}, {nearest_enemy.y})")
        else:
            print("No enemy found within range.")

        return nearest_enemy

    def attack_target(self, target):
        target.health -= self.attack
        print(f"Attacking {target} for {self.attack} damage. Remaining health: {target.health}")

    def upgrade(self):
        self.level += 1

        pass


class Cannon(Tower):
    def __init__(self, level=1, x=0, y=0):
        if level == 1:
            super().__init__(health=100, cost=15, attack=3, range=100, firerate=1, level=level, x=x, y=y)
        elif level == 2:
            super().__init__(health=120, cost=25, attack=5, range=100, firerate=1, level=level, x=x, y=y)
        elif level == 3:
            super().__init__(health=150, cost=40, attack=10, range=100, firerate=1, level=level, x=x, y=y)

class Catapult(Tower):
    def __init__(self, level=1, x=0, y=0):
        if level == 1:
            super().__init__(health=150, cost=25, attack=5, range=150, firerate=2, level=level, x=x, y=y)
        elif level == 2:
            super().__init__(health=180, cost=40, attack=7, range=150, firerate=2, level=level, x=x, y=y)
        elif level == 3:
            super().__init__(health=220, cost=60, attack=10, range=150, firerate=2, level=level, x=x, y=y)

class Ballista(Tower):
    def __init__(self, level=1, x=0, y=0):
        if level == 1:
            super().__init__(health=200, cost=40, attack=15, range=200, firerate=0.5, level=level, x=x, y=y)
        elif level == 2:
            super().__init__(health=220, cost=60, attack=20, range=200, firerate=0.5, level=level, x=x, y=y)
        elif level == 3:
            super().__init__(health=250, cost=80, attack=25, range=200, firerate=0.5, level=level, x=x, y=y)

class CaltropsDispenser(Tower):
    def __init__(self, level=1, x=0, y=0):
        if level == 1:
            super().__init__(health=50, cost=20, attack=0, range=0, firerate=20, level=level, x=x, y=y)
        elif level == 2:
            super().__init__(health=60, cost=35, attack=0, range=0, firerate=15, level=level, x=x, y=y)
        elif level == 3:
            super().__init__(health=70, cost=40, attack=0, range=0, firerate=10, level=level, x=x, y=y)

class KnightsBarracks(Tower):
    def __init__(self, level=1, x=0, y=0):
        if level == 1:
            super().__init__(health=200, cost=50, attack=0, range=0, firerate=30, level=level, x=x, y=y)
        elif level == 2:
            super().__init__(health=250, cost=75, attack=0, range=0, firerate=30, level=level, x=x, y=y)
        elif level == 3:
            super().__init__(health=300, cost=100, attack=0, range=0, firerate=30, level=level, x=x, y=y)

class HolyChapel(Tower):
    def __init__(self, level=1, x=0, y=0):
        if level == 1:
            super().__init__(health=100, cost=30, attack=0, range=0, firerate=5, level=level, x=x, y=y)
        elif level == 2:
            super().__init__(health=120, cost=50, attack=0, range=0, firerate=5, level=level, x=x, y=y)
        elif level == 3:
            super().__init__(health=150, cost=80, attack=0, range=0, firerate=5, level=level, x=x, y=y)
