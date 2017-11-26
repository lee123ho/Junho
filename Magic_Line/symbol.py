import random
import json
import os

from pico2d import *

class WidthSymbol:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('width.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class LengthSymbol:
    def __init__(self,x, y):
        self.x, self.y = x, y
        self.image = load_image('length.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)