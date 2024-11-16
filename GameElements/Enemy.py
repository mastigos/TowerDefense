import pygame

class Enemy:
    def __init__(self, health, maxHealth, damage, resistances, special, speed, corpseValue, start_x=0, start_y=300):
        self.health = health
        self.maxHealth = maxHealth
        self.damage = damage
        self.resistances = resistances
        self.special = special
        self.speed = speed
        self.corpseValue = corpseValue
        self.x = start_x
        self.y = start_y
        self.current_waypoint = 0
        self.animation_index = 0
        self.animation_frames = []
        self.animation_speed = .25

    def load_animation_frames(self, frame_paths, ):
        self.animation_frames = []
        for path in frame_paths:
            frame = pygame.image.load(path).convert_alpha()
            frame = pygame.transform.scale(frame, (50, 50))
            self.animation_frames.append(frame)

    def update_animation(self):
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.animation_frames):
            self.animation_index = 0

    def draw(self, screen):
        if self.animation_frames:
            frame = self.animation_frames[int(self.animation_index)]
            screen.blit(frame, (self.x - frame.get_width() // 2, self.y - frame.get_height() // 2))
        else:
            pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), 10)

    def draw_health_bar(self, screen):
        bar_width = 40
        bar_height = 5
        pygame.draw.rect(screen, (0, 0, 0), (self.x - bar_width // 2, self.y - 15, bar_width, bar_height))
        health_ratio = max(self.health / self.maxHealth, 0)
        health_width = health_ratio * bar_width
        pygame.draw.rect(screen, (255, 0, 0), (self.x - bar_width // 2, self.y - 15, health_width, bar_height))

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print(f"Enemy at ({self.x}, {self.y}) has died.")
        return True

    def move(self, waypoints):
        if self.current_waypoint < len(waypoints):
            target_x, target_y = waypoints[self.current_waypoint]
            if self.x < target_x: self.x += min(self.speed, target_x - self.x)
            elif self.x > target_x: self.x -= min(self.speed, self.x - target_x)
            elif self.y < target_y: self.y += min(self.speed, target_y - self.y)
            elif self.y > target_y: self.y -= min(self.speed, self.y - target_y)

            if (self.x, self.y) == (target_x, target_y):
                self.current_waypoint += 1

class Knight(Enemy):
    def __init__(self):
        super().__init__(health=10, maxHealth=10, damage=5, resistances=[], special="none", speed=1, corpseValue=5)
        frame_paths = [
            "GameSprites/Knight_SPRITESHEETS/Knight-and-Horse_Back-Walking-Back.png",
            "GameSprites/Knight_SPRITESHEETS/Knight-and-Horse_Back-Walking-Back2.png",
            "GameSprites/Knight_SPRITESHEETS/Knight-and-Horse_Back-Walking-Back3.png",
            "GameSprites/Knight_SPRITESHEETS/Knight-and-Horse_Back-Walking-Back4.png",
            "GameSprites/Knight_SPRITESHEETS/Knight-and-Horse_Back-Walking-Back5.png",
            "GameSprites/Knight_SPRITESHEETS/Knight-and-Horse_Back-Walking-Back6.png",
            "GameSprites/Knight_SPRITESHEETS/Knight-and-Horse_Back-Walking-Back7.png",
            "GameSprites/Knight_SPRITESHEETS/Knight-and-Horse_Back-Walking-Back8.png"
        ]

        self.load_animation_frames(frame_paths)


class BatteringRam(Enemy):
    def __init__(self):
        super().__init__(health=25, damage=40, resistances=[], special="none", speed=1.5, corpseValue=20)
        frame_paths = [

        ]

        self.load_animation_frames(frame_paths)

class Soldier(Enemy):
    def __init__(self):
        super().__init__(health=5, damage=10, resistances=[], special="none", speed=1, corpseValue=3)
        frame_paths = [
            "Dwarf_Front-Walking-Left_0.png",
            "Dwarf_Front-Walking-Left_1.png",
            "Dwarf_Front-Walking-Left_2.png",
            "Dwarf_Front-Walking-Left_3.png",
            "Dwarf_Front-Walking-Left_4.png",
            "Dwarf_Front-Walking-Left_5.png",
            "Dwarf_Front-Walking-Left_6.png",
            "Dwarf_Front-Walking-Left_7.png",
        ]

        self.load_animation_frames(frame_paths)

#bosses--> last thing
class Dragon(Enemy):
    def __init__(self):
        super().__init__(health=300, damage=50, resistances=[], special="none", speed=1, corpseValue=150)
        frame_paths = [
            "Red Dragon_Front-Flying-Left_0.png",
            "Red Dragon_Front-Flying-Left_1.png",
            "Red Dragon_Front-Flying-Left_2.png",
            "Red Dragon_Front-Flying-Left_3.png",
            "Red Dragon_Front-Flying-Left_4.png",
            "Red Dragon_Front-Flying-Left_5.png",
            "Red Dragon_Front-Flying-Left_6.png",
            "Red Dragon_Front-Flying-Left_7.png"
        ]

        self.load_animation_frames(frame_paths)


class Giant(Enemy):
    def __init__(self):
        super().__init__(health=1000, damage=75, resistances=[], special="stomp", speed=0.5, corpseValue=150)
