from pico2d import *

class BossFloor:
    def __init__(self):
        self.image = load_image('boss_floor.png')

    def draw(self):
        self.image.draw(400, 300)