from PIL import Image


def load_map(map_name):
    map_image = Image.open("assets/maps/" + map_name + "/map.png")
    return map_image.load()


def load_map_settings(map_name):
    map_settings_image = Image.open("assets/maps/" + map_name + "/map_settings.png")
    return map_settings_image.load()
