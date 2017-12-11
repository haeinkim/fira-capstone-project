import numpy as np
import json
from diced import DicedStore


class DicedArrayGenerator(object):
    def __init__(self, directory):
        self.directory = directory

    def load_roi(self):
        with open(self.directory, 'r') as f:
            roi = json.load(f)

        return roi

    def slice_extent_generator(self, roi=self.load_roi()):
        for loc in roi:
            z_extent = slice((loc[0]) * 32, (loc[0] * 32) + 32, None)
            y_extent = slice((loc[1]) * 32, (loc[1] * 32) + 32, None)
            x_extent = slice((loc[2]) * 32, (loc[3] * 32) + 32, None)

            yield z_extent, y_extent, x_extent
grayscale[next(slice_extent_generator())]