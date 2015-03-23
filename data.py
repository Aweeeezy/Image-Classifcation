import pickle

"""
    This module has two classes: IMAGE, and DATA. IMAGE is a data abstraction
    that represents each images w/ attributes: identifier, level, pixel grid,
    etc. The DATA class is an object for storing and representing the summation
    of our IMAGE instances in useful variations (to quickly access relevant
    information while optimizing our algorithms.
"""

class image():
    """ Data abstraction that contains all information for each image """

    identifier = ''
    level = ''
    pixels = ''

    def __init__(self, identifier, level, pixels=None):
        self.identifier = identifier
        self.level = level
        self.pixels = pixels

class data():
    """ Set of dictionaries, each containing a different subset of all the
    instances of IMAGE """

    healthy = {}
    unhealthy = {}
    all_images = {}

    def __init__(self, image_data):
        with open('image_data', 'r+b') as f:
            self.all_images = pickle.load(f)

        self.healthy = {k: v for k, v in self.all_images.items() if v.level == '0'}
        self.unhealthy = {k: v for k, v in self.all_images.items() if v.level != '0'}
