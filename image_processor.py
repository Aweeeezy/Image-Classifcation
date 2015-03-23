from os import listdir
import csv
import data
import pickle
from skimage import io
import skimage
import numpy

"""
    This module contains the IMAGE_PROCESSOR class, which initializes with a
    given image directory and label CSV. Using these args, IMAGE_PROCESSOR
    populates the list, IMAGES_LEVELS, with a sequence of pairs. Each pair has
    the absolute path to the an image and that image's respective level.

    The method, `process_images()`, instantiates an IMAGE (see data.py) for
    each pair in IMAGES_LEVELS. Next, it generates the pixel grid to associate
    with each IMAGE.

    *** NOTE: Skimage.io is not importing properly! ****

    The method, `save_images()`, writes all these IMAGE objects as binary to a
    file so the post-processed data can be accessed by other modules for
    structuring into arbitrary groups, fed into classifiers, etc.

    `load_images()` is a convienence method that returns IMAGE_DATA.
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
    >>> processor.image_data['10_left'].identifier
    '10_left
    >>> processor.image_data['10_left'].level
    '0'
    >>> processor.image_data['10_left'].pixels
    #!#!#! YET TO BE IMPLENTED...ERROR ON IMPORT SKIMAGE.IO #!#!#!
    """

    images_levels = [] # temporary container used to generate IMAGE_DATA
    image_data = {} # final dictionary that contains all the IMAGE objects

    def __init__(self, image_dir, trainingLabels):
        """ Appends image/label tuples to IMAGES_LEVELS, a list """

        with open(trainingLabels) as csvfile:
            for row in csv.DictReader(csvfile):
                self.images_levels.append((image_dir + '/' + row['image'], row['level']))

    def process_images(self):
        """ Creates an IMAGE instance (see data.py) for each element in
        IMAGES_LEVELS and populates its attributes with an image ID, level,
        pixel grid, and other attributes TBD. """

        for tup in self.images_levels:
            identifier, level = tup[0].split('/')[-1], tup[1]
            #image_pixels = io.imread(tup[0]) # can't import skimage.io!!!
            image_pixels = None # remove after fixing skimage.io problem
            i = data.image(identifier, level, image_pixels)
            self.image_data[i.identifier] = i

    def save_images(self):
        """ Writes IMAGE_DATA to file in binary for easy restoration of states """
        with open('image_data', 'r+b') as f:
            pickle.dump(self.image_data, f, -1)

    def load_images(self):
        """ Repopulates IMAGE_DATA with binary objects in `image_data` file """
        with open('image_data' , 'r+b') as f:
            return pickle.load(f)
