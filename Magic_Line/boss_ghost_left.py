import random
import json
import os

from pico2d import *


class Ghostleft:

    image = None

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 2  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x, self.y = random.randint(0, 50), random.randint(0,600)
        self.time = 0
        self.speed = 0
        self.type = 1
        if Ghostleft.image == None:
            Ghostleft.image = load_image('ghost_right.png')

    def symbol_pos(self):
        return self.x, self.y + 85

    def update(self, frame_time):
        distance = Ghostleft.RUN_SPEED_PPS * frame_time
        if self.x < 200:
            self.x += distance + self.speed
        if self.y - 300 < 0:
            self.y += distance + self.speed
        else:
            self.y -= distance + self.speed

    def stop(self):
        Ghostleft.RUN_SPEED_PPS = 0

    def die(self):
        self.image_die = load_image('ghost_die.png')

    def get_bb(self):
        return self.x - 75, self. y - 75, self.x + 75, self.y + 75

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.image.draw(self.x, self.y)