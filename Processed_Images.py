"""
    Module for storing processed data in an organized fashion. Structured data
    allows easy application of controlled data sets to machine learning models
    for both training and testing.
"""

class Processed_Images():
    """ This class is the summation of all the built structures. Each structure
    is constructed by call `Images().<structure_name>` via the `@property`
    decorator. """

    healthy_unhealthy = {} # simple binary classification <INDICATOR> = '@'
    unhealthy_degree = {} # ranked 1-4                   <INDICATOR> = '$'
    all_samples = {} =     # unstructured                 <INDICATOR> = '%'

    def __init__(self):
        """ Reads data (objects written as binary, see 'data.py') from file """
        groups = {'@':healthy_unhealthy, '$':unhealthy_degree, '%':all_samples}
        with open('structured_data', 'r') as f:
            [create_structure(line, f) for line in f if line is in groups]

    def create_structure(self, indicator, f):
        """ arg `indicator` determines which structure dictionary is populated """



