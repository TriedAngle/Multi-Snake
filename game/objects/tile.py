class Tile:
    tile_id = None
    tile_x = None
    tile_y = None
    tile_width = 16
    tile_height = 16

    def render(self):
        pass

    def update(self):
        pass


class teleporter:
    def __init__(self, x, y, oX, oY):
        self.x = x
        self.y = y
        self.oX = oX
        self.oY = oY

