import random
import json
import os

from pico2d import *


class Boss:

    image = None

    def __init__(self):
        self.x, self.y = 600, 200
        self.frame = 0
        self.image = load_image('boss_sheet_2500.png')

    def update(self, frame_time):
        self.frame += 1
        if self.frame == 5:
            self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 500, 0, 500, 500, self.x, self.y)