from PIL import Image


class Assets:
    def __init__(self):
        self.sprite_sheet = None
        self.sprites = []

    def load_sprite_sheet(self, texture_pack="default"):
        self.sprite_sheet = Image.open("assets/texturepacks/" + texture_pack + "/sprite_sheet.png").convert('RGB')

    def set_sprites(self):
        tmp = 0
        for x in range(0, 16):
            for y in range(0, 16):
                self.sprites.append(self.sprite_sheet.crop((x*16, y*16, x*16 + 16, y*16 + 16)).resize((64, 64), Image.ANTIALIAS))

    def get_sprite(self, index):
        return self.sprites[index]
