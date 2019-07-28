from game.objects.tile import Tile
from game.utility.assets import Assets

assets = Assets()
assets.load_sprite_sheet()
assets.set_sprites()
grass_texture = assets.get_sprite(0)
# grass_texture = grass_texture.resize((64, 64), Image.ANTIALIAS)
# water_area = (64, 16, 80, 32)
# water_texture = sprite_sheet.crop(water_area)
# water_texture = water_texture.resize((64, 64), Image.ANTIALIAS)
# lava_area = (128, 16, 144, 32)
# lava_texture = sprite_sheet.crop(lava_area)
# lava_texture = lava_texture.resize((64, 64), Image.ANTIALIAS)


class GrassTile(Tile):
    def __init__(self, x, y):
        self.texture = grass_texture
        super().__init__(self.texture, x, y)


class WaterTile(Tile):
    def __init__(self, x, y):
        self.texture = grass_texture
        super().__init__(self.texture, x, y)

    def is_solid(self):
        return False


class LavaTile(Tile):
    def __init__(self, x, y):
        self.texture = grass_texture
        super().__init__(self.texture, x, y)

    def is_solid(self):
        return True
