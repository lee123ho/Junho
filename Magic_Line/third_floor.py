from pico2d import *

class ThirdFloor:
    def __init__(self):
        self.image = load_image('third_floor.png')

    def draw(self):
        self.image.draw(400, 300)