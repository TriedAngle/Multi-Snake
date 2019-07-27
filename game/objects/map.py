from game.utility.image_loader import load_map, load_map_settings, loadTileId,Image
import random

class Map:
    def __init__(self, mapName):
        self.tileMap = load_map(mapName)
        self.tileSettings = load_map_settings(mapName)
        self.tiles = Image.open("assets/texturepacks/default/tiles.png")
        res = self.tileMap.size
        img = Image.new("RGB", (res[0] * 16, res[1] * 16))
        px = img.load()

        pxTileMap = self.tileMap.load()

        teleporters = {}
        grass = {}
        water = {}
        lava = {}

        self.coordinates = {"teleporters": [], "grass": [], "water": [], "lava": []}

        pxSet = self.tileSettings.load()
        resSet = self.tileSettings.size
        for x in range(resSet[0]):
            if pxSet[x, 1] == (0, 255, 255):
                teleporters[pxSet[x, 0]] = pxSet[x, 2]
            elif pxSet[x, 1] == (0, 255, 0):
                grass[pxSet[x, 0]] = pxSet[x, 2]
            elif pxSet[x, 1] == (255, 0, 0):
                lava[pxSet[x, 0]] = pxSet[x, 2]
            elif pxSet[x, 1] == (0, 0, 255):
                water[pxSet[x, 0]] = pxSet[x, 2]

        for x in range(res[0]):
            for y in range(res[1]):
                id = None
                for g in grass:
                    if pxTileMap[x, y] == g:
                        id = grass[g][1] if grass[g][0] == 0 else random.randint(grass[g][1], grass[g][2])
                        self.coordinates["grass"].append((x, y))
                if id == None:
                    for w in water:
                        if pxTileMap[x, y] == w:
                            id = water[w][1] if water[w][0] == 0 else random.randint(water[w][1], water[w][2])
                            self.coordinates["water"].append((x, y))
                if id == None:
                    for l in lava:
                        if pxTileMap[x, y] == l:
                            id = lava[l][1] if lava[l][0] == 0 else random.randint(lava[l][1], lava[l][2])
                            self.coordinates["lava"].append((x, y))
                if id == None:
                    for t in teleporters.keys():
                        if pxTileMap[x, y] == t:
                            id = teleporters[t][0]
                            self.coordinates["teleporters"].append((x, y))
                tile = loadTileId(id)
                for i in range(16):
                    for j in range(16):
                        px[x * 16 + i, y * 16 + j] = tile[i][j]
        img.show()



    def render(self):
        pass

    def update(self):
        pass
