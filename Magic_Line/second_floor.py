from pico2d import *

class SecondFloor:
    def __init__(self):
        self.image = load_image('second_floor.png')

    def draw(self):
        self.image.draw(400, 300)