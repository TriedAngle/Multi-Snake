import pygame


class Tile:
    width, height = 16, 16
    tile_id = None
    texture = None

    def __init__(self, texture, x, y):
        self.mode = texture.mode
        self.size = texture.size
        self.data = texture.tobytes()
        self.texture = pygame.image.fromstring(self.data, self.size, self.mode)
        self.x = x
        self.y = y

    def update(self):
        pass

    def render(self, window):
        window.blit(self.texture, (self.x, self.y))

    def is_solid(self):
        return False

    def get_tile_id(self):
        return self.tile_id
