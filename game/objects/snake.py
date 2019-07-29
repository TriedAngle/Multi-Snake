import pygame
from game.utility.assets import asset
from PIL import Image

class Snake:
    def __init__(self, pos, dir, window, res, id):
        self.snake = [[pos[0], pos[1]]]
        self.dir = dir
        self.window = window
        self.res = res
        self.id = id
        tiles = Image.open("assets/texturepacks/default/tiles.png")
        headStartX = ((id + 1) * 16 - 16) % 256
        headStartY = (id // 16) * 16
        img_snakehead = tiles.crop((headStartX, headStartY, headStartX + 16, headStartY + 16))
        self.img_snakehead = pygame.image.fromstring(img_snakehead.tobytes(), img_snakehead.size, img_snakehead.mode)
        bodyStartX = ((id + 2) * 16 - 16) % 256
        bodyStartY = ((id + 1) // 16) * 16
        img_snakebody = tiles.crop((bodyStartX, bodyStartY, bodyStartX + 16, bodyStartY + 16))
        self.img_snakebody = pygame.image.fromstring(img_snakebody.tobytes(), img_snakebody.size, img_snakebody.mode)

    def shift(self, eaten):
        last = self.snake[-1]
        head = self.snake[0]
        head[0] += self.dir[0]
        head[1] += self.dir[1]
        self.snake = self.snake[::-1][0:-1].append(head)
        self.snake = self.snake[::-1]
        if eaten:
            self.snake.append(last)

    def render(self):
        self.window.blit(self.img_snakehead, self.snake[0])
        for part in self.snake[::-1][0:-1][::-1]:
            self.window.blit(self.img_snakebody, part)

    def update(self, food):
        head = self.snake[0]
        # 1. Movement #
        # 1.1 Check if the snake will eat in the next turn
        eaten = True if [head[0] + self.dir[0], head[1] + self.dir[1]] == food else False
        # 1.2 Shift the snake, as we now know if it will eat or not
        self.shift(eaten)

        # 2. Collision checking #
        # We will return a boolean to indicate if the snake has collided with itself or the walls
        # 2.1 Check them walls
        if head[0] < 0 or head[0] >= self.res[0] or head[1] < 0 or head[1] >= self.res[1]:
            return True, eaten
        # 2.2 Check that body
        elif head in self.snake[::-1][0:-1][::-1]:
            return True, eaten
        return False, eaten
