import pickle

class image():
    identifier = ''
    level = ''
    pixels = ''

    def __init__(self, identifier, level, pixels=None):
        self.identifier = identifier
        self.level = level
        self.pixels = pixels

class data():
    healthy = {}
    unhealthy = {}
    all_images = {}

    def __init__(self, image_data):
        with open('image_data', 'r+b') as f:
            self.all_images = pickle.load(f)

        """ As of now, the first dictionary comprehesion doesn't work at all
        (`len(data.healthy)` is 0) and the second comprension has a length equal
        to ALL_IMAGES """

        self.healthy = {k: v for k, v in self.all_images.items() if v.level is 0}
        self.unhealthy = {k: v for k, v in self.all_images.items() if v.level is not 0}
