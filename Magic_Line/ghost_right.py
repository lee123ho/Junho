import random
import json
import os

from pico2d import *

class GhostRight:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 2  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x, self.y = random.randint(0, 50), random.randint(0,600)
        self.regen_time = 0.0
        self.image_normal = load_image('ghost_right.png')
        self.image_die = load_image('ghost_die.png')
        self.type = random.randint(1, 2)

    def symbol_pos(self):
        return self.x, self.y + 85

    def update(self, frame_time):
        distance = GhostRight.RUN_SPEED_PPS * frame_time
        if self.x < 400:
            self.x += distance
        if self.y - 300 < 0:
            self.y += distance
        else:
            self.y -= distance

    def stop(self):
        GhostRight.RUN_SPEED_PPS = 0

    def get_bb(self):
        return self.x - 75, self. y - 75, self.x + 75, self.y + 75

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.image_normal.draw(self.x, self.y)