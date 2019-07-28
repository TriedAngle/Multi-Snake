from game.objects.tiles import *
from PIL import Image


def load_map(tile_map_name):
    tile_map = Image.open("assets/maps/" + tile_map_name + "/map.png").convert('RGB')
    tile_map_settings = Image.open("assets/maps/" + tile_map_name + "/map-settings.png").convert('RGB')
    return tile_map, tile_map_settings


def set_tiles(tile_map):
    tiles = []
    for x in range(0, 16):
        for y in range(0, 16):
            if tile_map.getpixel((x, y)) == (255, 0, 0):
                tiles.append(LavaTile(x * 64, y * 64))
            elif tile_map.getpixel((x, y)) == (0, 0, 255):
                tiles.append(WaterTile(x * 64, y * 64))
            elif tile_map.getpixel((x, y)) == (0, 255, 0):
                tiles.append(GrassTile(x * 64, y * 64))
            else:
                tiles.append(GrassTile(x * 64, y * 64))
    return tiles


class Map:
    water = []
    grass = []
    lava = []
    tiles = []

    def __init__(self, tile_map_name="default"):
        self.tile_map, self.tile_settings = load_map(tile_map_name)
        self.tiles = set_tiles(self.tile_map)

    def render(self, window):
        for tile in self.tiles:
            tile.render(window)

    def update(self):
        for tile in self.tiles:
            tile.update()
