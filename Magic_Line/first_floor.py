from pico2d import *

class FirstFloor:

    back_music = None

    def __init__(self):
        self.image = load_image('first_floor.png')

    def draw(self):
        self.image.draw(400, 300)