from game.objects.tiles import *


class Map:
    water = []
    grass = []
    lava = []

    def __init__(self):
        for i in range(0, 500, 16):
            if i % 2 == 0:
                self.grass.append(GrassTile(i, i*2))
            if i % 3 == 0:
                self.grass.append(WaterTile(i, i*3))
            if i % 7 == 0:
                self.lava.append(LavaTile(i, i*2))

    def render(self, window):
        for tile in self.grass:
            tile.render(window)
        for tile in self.water:
            tile.render(window)
        for tile in self.lava:
            tile.render(window)

    def update(self):
        pass
