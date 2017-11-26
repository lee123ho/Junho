from pico2d import *

class FirstStage:
    def __init__(self):
        self.image = load_image('first_stage.png')

    def draw(self):
        self.image.draw(400, 300)