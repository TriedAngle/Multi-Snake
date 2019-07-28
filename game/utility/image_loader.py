from PIL import Image


def load_map(map_name):
    return Image.open("assets/maps/" + map_name + "/map.png")


def load_map_settings(map_name):
    return Image.open("assets/maps/" + map_name + "/map-settings.png")


def loadTileId(id):
        img = Image.open("assets/texturepacks/default/tiles.png")
        px = img.load()
        xStart = ((id + 1) * 16 - 16) % 256
        yStart = (id // 16) * 16
        res = []
        for i in range(16):
            xRow = []
            for j in range(16):
                xRow.append(px[xStart + i, yStart + j])
            res.append(xRow)
        return res