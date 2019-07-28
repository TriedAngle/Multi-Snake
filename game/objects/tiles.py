from game.objects.tile import Tile
from PIL import Image

sprite_sheet = Image.open("assets/texturepacks/default/sprite_sheet.png")
grass_area = (0, 16, 16, 32)
grass_texture = sprite_sheet.crop(grass_area)
water_area = (64, 16, 80, 32)
water_texture = sprite_sheet.crop(water_area)
lava_area = (128, 16, 144, 32)
lava_texture = sprite_sheet.crop(lava_area)


class GrassTile(Tile):
    def __init__(self, x, y):
        self.texture = grass_texture
        super().__init__(self.texture, x, y)


class WaterTile(Tile):
    def __init__(self, x, y):
        self.texture = water_texture
        super().__init__(self.texture, x, y)

    def is_solid(self):
        return False


class LavaTile(Tile):
    def __init__(self, x, y):
        self.texture = lava_texture
        super().__init__(self.texture, x, y)

    def is_solid(self):
        return True
