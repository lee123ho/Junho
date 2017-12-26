import random
import json
import os

from pico2d import *

class BossWidthSymbol:

    image = None

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.speed = 0
        if BossWidthSymbol.image == None:
            BossWidthSymbol.image = load_image('width.png')

    def update(self, frame_time):
        distance = BossWidthSymbol.RUN_SPEED_PPS * frame_time
        if self.x > 400:
            self.x -= distance + self.speed
        elif self.x < 400:
            self.x += distance + self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class BossLengthSymbol:

    image = None

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 2  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self,x, y):
        self.x, self.y = x, y
        self.speed = 0
        if BossLengthSymbol.image == None:
            BossLengthSymbol.image = load_image('length.png')

    def update(self, frame_time):
        distance = BossLengthSymbol.RUN_SPEED_PPS * frame_time
        if self.x > 400:
            self.x -= distance + self.speed
        elif self.x < 400:
            self.x += distance + self.speed

    def draw(self):
        self.image.draw(self.x, self.y)