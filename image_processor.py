from os import listdir
import csv
import data
import pickle
from skimage import io

"""
    This modules contains the IMAGE_PROCESSOR class which is used to take raw,
    un-processed data, create IMAGE class instances for each data, and generate
    a dictionary, IMAGE_DATA, whose values are these IMAGE instances and keys
    are their unique identifiers. Finally, this class writes IMAGE_DATA to a
    binary file so the processed data can be accessed by other modules for
    structuring into arbitrary groups, feeding into classifiers, etc.
"""

class image_processor():
    """ Takes an image directory and label CSV as arguments upon initialization
    and then populates IMAGES_LEVELS with tuples containg the absolute file
    paths of each image (w/o file extention) paired with its level.

    >>> image_dir = '/Users/aweeeezy/bin/python/Image-Classifcation/files/images'
    >>> trainingLabels = '/Users/aweeeezy/bin/python/Image-Classifcation/files/trainLabels.csv'
    >>> processor = image_processor(image_dir, trainingLabels)
    >>> processor.images_levels[0]
    ('/Users/aweeeezy/bin/python/Image-Classifcation/files/images/10_left', '0')
    >>> processor.process_images()
    >>> processor.image_data['10_left'].identifier
    '10_left
    >>> processor.image_data['10_left'].level
    '0'
    >>> processor.image_data['10_left'].pixels[0]
    [[0 0 0]
     [0 0 0]
     [0 0 0]
     ...,
     [0 0 0]
     [0 0 0]
     [0 0 0]]
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
        pixel grid, and other attributes TBD.

        #!#!#! ASSUMES THAT THE EXT FOR EACH IMAGE FILE IS .JPEG #!#!#!
        """

        for tup in self.images_levels:
            identifier, level = tup[0].split('/')[-1], tup[1]
            image_pixels = io.imread(tup[0] + '.jpeg')
            i = data.image(identifier, level, image_pixels)
            self.image_data[identifier] = i

    def save_images(self):
        """ Writes IMAGE_DATA to file in binary for easy restoration of data """
        with open('image_data', 'r+b') as f:
            pickle.dump(self.image_data, f, -1)

    def load_images(self):
        """ returns dictionary of IMAGE instances using `image_data` file """
        with open('image_data' , 'r+b') as f:
            return pickle.load(f)
