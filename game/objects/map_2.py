from game.utility.image_loader import load_map, load_map_settings, loadTileId,Image
import random
import pygame

class Map:
    def __init__(self, mapName, window):
        self.ticks = 0
        self.rawticks = 0
        self.window = window
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
        self.animated = []

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
                        id = grass[g][1] if grass[g][0] == 0 else random.randint(grass[g][1], grass[g][2]) if grass[g][0] == 1 else (grass[g][1], grass[g][2])
                        if id == (grass[g][1], grass[g][2]):
                            self.animated.append((x, y, grass[g][1], grass[g][2]))
                            id = id[0]
                        self.coordinates["grass"].append((x, y))

                if id == None:
                    for w in water:
                        if pxTileMap[x, y] == w:
                            id = water[w][1] if water[w][0] == 0 else random.randint(water[w][1], water[w][2]) if water[w][0] == 1 else (water[w][1], water[w][2])
                            if id == (water[w][1], water[w][2]):
                                self.animated.append((x, y, water[w][1], water[w][2]))
                                id = id[0]
                            self.coordinates["water"].append((x, y))
                if id == None:
                    for l in lava:
                        if pxTileMap[x, y] == l:
                            id = lava[l][1] if lava[l][0] == 0 else random.randint(lava[l][1], lava[l][2]) if lava[l][0] == 1 else (lava[l][1], lava[l][2])
                            if id == (lava[l][1], lava[l][2]):
                                self.animated.append((x, y, lava[l][1], lava[l][2]))
                                id = id[0]
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
        self.renderedMap = pygame.image.fromstring(img.tobytes(), img.size, img.mode)



    def render(self):
        self.window.blit(self.renderedMap, (0, 0))

        # Now we iterate through all the animated tiles
        for tile in self.animated:
            diff = tile[3] - tile[2]
            useId = tile[2] + self.ticks % diff
            sX = ((useId + 1) * 16 - 16) % 256
            sY = (useId // 16) * 16
            img = self.tiles.crop((sX, sY, sX + 16, sY + 16))
            self.window.blit(pygame.image.fromstring(img.tobytes(), img.size, img.mode), (tile[0] * 16, tile[1] * 16))

    def update(self):
        self.rawticks += 1
        self.ticks = self.rawticks // 5