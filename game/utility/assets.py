from PIL import Image
import pygame


class Assets:
    def __init__(self):
        self.sprite_sheet = None
        self.sprites = []

    def load_sprite_sheet(self, texture_pack="default"):
        self.sprite_sheet = Image.open("assets/texturepacks/" + texture_pack + "/sprite_sheet.png").convert('RGB')

    def set_sprites(self):
        for y in range(0, 2):
            for x in range(0, 16):
                tmp_image = self.sprite_sheet.crop((x*16, y*16, x*16 + 16, y*16 + 16)).resize((64, 64))
                tmp_img_data = tmp_image.tobytes()
                tmp_image_size = tmp_image.size
                tmp_image_mode = tmp_image.mode
                self.sprites.append(pygame.image.fromstring(tmp_img_data, tmp_image_size, tmp_image_mode))

    def get_sprite(self, index):
        return self.sprites[index]

    def get_animated(self, indexes):
        sprites = []
        for index in indexes:
            sprites.append(self.get_sprite(index))

        return sprites


asset = Assets()
asset.load_sprite_sheet()
asset.set_sprites()
