import pygame
from game.utility.assets import asset


class Snake:
    x = None
    y = None
    snake_parts = []
    width = 64
    height = 64

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.snake_parts.append((x, y))
        self.tick = 0
        self.mov_locked = False

    def render(self, window):
        for part in self.snake_parts:
            if part == self.snake_parts[0]:
                window.blit(asset.get_sprite(0), part)
            else:
                window.blit(asset.get_sprite(1), part)

    def update(self):
        self.tick += 1
        if self.tick >= 30:
            self.tick = 0
            self.mov_locked = False

        if not self.mov_locked:
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.y -= 64
                self.mov_locked = True
            if key[pygame.K_s]:
                self.y += 64
                self.mov_locked = True
            if key[pygame.K_a]:
                self.x -= 64
                self.mov_locked = True
            if key[pygame.K_d]:
                self.x += 64
                self.mov_locked = True

        self.snake_parts[0] = self.x, self.y
