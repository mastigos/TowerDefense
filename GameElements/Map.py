import pygame
from GameElements.Tower import Cannon, Catapult, Ballista, CaltropsDispenser, KnightsBarracks, HolyChapel
class Map:
    def __init__(self, width, height, block_size, waypoints, castle):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.tileMap = [[0 for _ in range(width // block_size)] for _ in range(height // block_size)]


        self.tower_ids = {
            Cannon: 1,
            Catapult: 2,
            Ballista: 3,
            CaltropsDispenser: 4,
            KnightsBarracks: 5,
            HolyChapel: 6
        }


        self.set_path_as_unbuildable(waypoints)


        self.set_castle_as_unbuildable(castle)

    def set_tile(self, row, col, value):

        self.tileMap[row][col] = value

    def build_tower(self, tower, row, col):

        tower_id = self.tower_ids.get(type(tower), 0)
        self.set_tile(row, col, tower_id)


    def build(self, tower, row, col):
        tower.x = col * self.block_size
        tower.y = row * self.block_size
        self.tileMap[row][col] = tower


        tower_id = self.tower_ids.get(type(tower), 0)
        self.set_tile(row, col, tower_id)

    def get_tile_at_mouse(self, mouse_x, mouse_y):

        col = mouse_x // self.block_size
        row = mouse_y // self.block_size
        return row, col

    def set_path_as_unbuildable(self, waypoints):

        for i in range(len(waypoints) - 1):
            start = waypoints[i]
            end = waypoints[i + 1]

            x, y = start
            target_x, target_y = end

            while (x, y) != (target_x, target_y):
                row, col = y // self.block_size, x // self.block_size


                if self.tileMap[row][col] != -1:
                    self.set_tile(row, col, -1)


                if x < target_x:
                    x += self.block_size
                    if x > target_x:
                        x = target_x
                elif x > target_x:
                    x -= self.block_size
                    if x < target_x:
                        x = target_x


                if y < target_y:
                    y += self.block_size
                    if y > target_y:
                        y = target_y
                elif y > target_y:
                    y -= self.block_size
                    if y < target_y:
                        y = target_y


                if not (0 <= row < len(self.tileMap) and 0 <= col < len(self.tileMap[0])):
                    break


            end_row, end_col = target_y // self.block_size, target_x // self.block_size
            if self.tileMap[end_row][end_col] != -1:
                self.set_tile(end_row, end_col, -1)

    def set_castle_as_unbuildable(self, castle):

        for i in range(castle.y, castle.y + castle.height, self.block_size):
            for j in range(castle.x, castle.x + castle.width, self.block_size):
                row, col = i // self.block_size, j // self.block_size
                self.set_tile(row, col, -1)

    def draw(self, screen):
        for row in range(len(self.tileMap)):
            for col in range(len(self.tileMap[row])):
                x, y = col * self.block_size, row * self.block_size
                tile_value = self.tileMap[row][col]

                if tile_value == -1:
                    pygame.draw.rect(screen, (139, 69, 19), (x, y, self.block_size, self.block_size))
                elif tile_value == 0:
                    pygame.draw.rect(screen, (34, 139, 34), (x, y, self.block_size, self.block_size))
                elif tile_value == 1:
                    pygame.draw.rect(screen, (255, 0, 0), (x, y, self.block_size, self.block_size))
                elif tile_value == 2:
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (x, y, self.block_size, self.block_size))  #
                elif tile_value == 3:
                    pygame.draw.rect(screen, (0, 0, 255), (x, y, self.block_size, self.block_size))
                elif tile_value == 4:
                    pygame.draw.rect(screen, (255, 255, 0),
                                     (x, y, self.block_size, self.block_size))
                elif tile_value == 5:
                    pygame.draw.rect(screen, (128, 0, 128),
                                     (x, y, self.block_size, self.block_size))
                elif tile_value == 6:
                    pygame.draw.rect(screen, (255, 215, 0), (x, y, self.block_size, self.block_size))