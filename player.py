import random
import pygame

class Player:
    def __init__(self, x, y, is_bot=False):
        self.x = int(x)
        self.y = int(y)
        self.player_size = 10
        self.rect = pygame.Rect(self.x, self.y, self.player_size, self.player_size)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
        self.is_bot = is_bot

    def move_bot(self, tile, grid_cells):
        if self.is_bot:
            direction = random.choice(['left', 'right', 'up', 'down'])
            if direction == 'left':
                self.left_pressed = True
            elif direction == 'right':
                self.right_pressed = True
            elif direction == 'up':
                self.up_pressed = True
            elif direction == 'down':
                self.down_pressed = True
            self.check_move(tile, grid_cells, 5)  # Adjust thickness as needed

    def check_move(self, tile, grid_cells, thickness):
        current_cell_x, current_cell_y = self.x // tile, self.y // tile
        current_cell = self.get_current_cell(current_cell_x, current_cell_y, grid_cells)
        current_cell_abs_x, current_cell_abs_y = current_cell_x * tile, current_cell_y * tile
        if self.left_pressed:
            if current_cell.walls['left']:
                if self.x <= current_cell_abs_x + thickness:
                    self.left_pressed = False
        if self.right_pressed:
            if current_cell.walls['right']:
                if self.x >= current_cell_abs_x + tile - (self.player_size + thickness):
                    self.right_pressed = False
        if self.up_pressed:
            if current_cell.walls['top']:
                if self.y <= current_cell_abs_y + thickness:
                    self.up_pressed = False
        if self.down_pressed:
            if current_cell.walls['bottom']:
                if self.y >= current_cell_abs_y + tile - (self.player_size + thickness):
                    self.down_pressed = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, tile, grid_cells, thickness):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.check_move(tile, grid_cells, thickness)

        self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)
