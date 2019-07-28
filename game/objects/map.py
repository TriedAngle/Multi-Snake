from game.objects.tiles import *
import pygame
from PIL import Image


class Map:
    water = []
    grass = []
    lava = []
    tiles = []

    def __init__(self):
        # self.tile_map = load_map("test_map")
        # self.tile_settings = load_map_settings("test_map")
        self.tile_map = Image.open("assets/maps/test_map/map.png").convert('RGB')
        self.tile_settings = Image.open("assets/maps/test_map/map-settings.png").convert('RGB')

        for x in range(0, 16):
            for y in range(0, 16):
                if self.tile_map.getpixel((x, y)) == (255, 0, 0):
                    self.tiles.append(LavaTile(x*64, y*64))
                elif self.tile_map.getpixel((x, y)) == (0, 0, 255):
                    self.tiles.append(WaterTile(x*64, y*64))
                elif self.tile_map.getpixel((x, y)) == (0, 255, 0):
                    self.tiles.append(GrassTile(x * 64, y * 64))
                else:
                    self.tiles.append(GrassTile(x * 64, y * 64))

    def render(self, window):
        for tile in self.tiles:
            tile.render(window)

    def update(self):
        for tile in self.tiles:
            tile.x += 5
