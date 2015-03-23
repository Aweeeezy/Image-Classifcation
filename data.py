import pickle

"""
    This module has two classes: IMAGE, and DATA.

    IMAGE is a data abstraction that represents each images w/ attributes:
    identifier, level, pixel grid, etc.

    The DATA class is an object for storing and representing the summation
    of our IMAGE instances in useful variations.
"""

class image():
    """ Data abstraction that contains all information for each image. """

    identifier = ''
    level = ''
    pixels = ''

    def __init__(self, identifier, level, pixels):
        self.identifier = identifier
        self.level = level
        self.pixels = pixels

class data():
    """ Collection of dictionaries, each containing a different subset of all
    the instances of IMAGE. """

    all_images = {}
    healthy = {}
    unhealthy = {}
    level_1 = {}
    level_2 = {}
    level_3 = {}
    level_4 = {}
    left = {}
    right = {}

    def __init__(self, image_data):
        with open('image_data', 'r+b') as f:
            self.all_images = pickle.load(f)

        self.healthy = {k: v for k, v in self.all_images.items() if v.level == '0'}
        self.unhealthy = {k: v for k, v in self.all_images.items() if v.level != '0'}

        self.level_1 = {k: v for k, v in self.unhealthy.items() if v.level == '1'}
        self.level_2 = {k: v for k, v in self.unhealthy.items() if v.level == '2'}
        self.level_3 = {k: v for k, v in self.unhealthy.items() if v.level == '3'}
        self.level_4 = {k: v for k, v in self.unhealthy.items() if v.level == '4'}

        self.left = {k: v for k, v in self.all_images.items() if 'left' in k}
        self.right = {k: v for k, v in self.all_images.items() if 'right' in k}
