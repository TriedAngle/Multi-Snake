from game.objects.tile import Tile
from game.utility.assets import asset


class GrassTile(Tile):
    def __init__(self, x, y):
        self.texture = asset.get_sprite(16)
        super().__init__(self.texture, x, y)


class WaterTile(Tile):
    def __init__(self, x, y):
        self.raw_textures = asset.get_animated((19, 20, 21))
        super().__init__(None, x, y, self.raw_textures)

    def is_solid(self):
        return False

    def is_animated(self):
        return True


class LavaTile(Tile):
    def __init__(self, x, y):
        self.raw_textures = asset.get_animated((22, 23, 24))
        super().__init__(None, x, y, self.raw_textures)

    def is_solid(self):
        return True

    def is_animated(self):
        return True
