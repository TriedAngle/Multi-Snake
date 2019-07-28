import pygame


class Tile:
    width, height = 16, 16
    tile_id = None
    texture = None
    textures = []

    def __init__(self, texture, x, y, raw_textures=None):
        self.raw_textures = raw_textures
        self.raw_texture = texture
        if not self.is_animated():
            self.texture = pygame.image.fromstring(self.raw_texture.tobytes(),
                                                   self.raw_texture.size,
                                                   self.raw_texture.mode)
        else:
            self.texture = pygame.image.fromstring(self.raw_textures[0].tobytes(),
                                                   self.raw_textures[0].size,
                                                   self.raw_textures[0].mode)

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
            if self.texture_index >= len(self.raw_textures):
                self.texture_index = 0
            self.texture = pygame.image.fromstring(self.raw_textures[self.texture_index].tobytes(),
                                                   self.raw_textures[self.texture_index].size,
                                                   self.raw_textures[self.texture_index].mode)

    def render(self, window):
        window.blit(self.texture, (self.x, self.y))

    def is_animated(self):
        return False

    def is_solid(self):
        return False

    def get_tile_id(self):
        return self.tile_id
