import pygame


class Tile:
    width, height = 16, 16
    tile_id = None
    texture = None
    textures = []

    def __init__(self, texture, x, y, textures=None):
        self.textures = textures

        if not self.is_animated():
            self.texture = texture
        else:
            self.texture = textures[0]

        self.texture_index = 0
        self.x = x
        self.y = y
        self.ticks = 0

    def update(self):
        self.ticks += 1
        if self.ticks >= 60:
            self.ticks = 0

        if self.is_animated() and self.ticks % 20 == 0:
            self.texture_index += 1
            if self.texture_index >= len(self.textures):
                self.texture_index = 0
            self.texture = self.textures[self.texture_index]

    def render(self, window):
        window.blit(self.texture, (self.x, self.y))

    def is_animated(self):
        return False

    def is_solid(self):
        return False

    def get_tile_id(self):
        return self.tile_id
