from os import listdir
import csv
from data import Image

"""
    This module contains the IMAGE_PROCESSOR class, which initializes with a
    given image directory and label CSV. Using these args, IMAGE_PROCESSOR
    populates the list, IMAGES_LEVELS, with a sequence of pairs. Each pair has
    the absolute path to the an image and that image's respective level.

    The method, `process_images()`, instantiates an IMAGE (see data.py) for
    each pair in IMAGES_LEVELS. Next, it generates the pixel grid to associate
    with each IMAGE.

    The method, `save_objects()`, writes all these IMAGE objects as binary to a
    file so the post-processed data can be accessed by other modules for
    structuring into arbitrary groups, fed into classifiers, etc.
"""

class image_processor():
    """ Takes an image directory and label CSV as arguments upon initialization
    and then populates IMAGES_LEVELS with tuples containg the absolute file
    paths of each image paired with its level.

    >>> image_dir = '/Users/aweeeezy/bin/python/Image-Classifcation/files/images'
    >>> trainingLabels = '/Users/aweeeezy/bin/python/Image-Classifcation/files/trainLabels.csv'
    >>> processor = image_processor(image_dir, trainingLabels)
    >>> processor.images_levels[0]
    ('/Users/aweeeezy/bin/python/Image-Classifcation/files/images/10_left', '0')
    """

    images_levels = []

    def __init__(self, image_dir, trainingLabels):
        """ Writes image/label information into IMAGES_LEVELS, a list of tuples """

        with open(trainingLabels) as csvfile:
            for row in csv.DictReader(csvfile):
                self.images_levels.append((image_dir + '/' + row['image'], row['level']))

    def process_images(self):
        """ Creates an IMAGE instance (see data.py) for each element in
        IMAGES_LEVELS and populates its attributes with an image ID, level,
        pixel grid, and other attributes TBD. """

        for tup in self.images_levels:
            identifier, level = tup[0].split('/')[-1], tup[1]

            # code for generating pixel grids goes here

            image = image(identifier, level, "variable for pixel grid")



