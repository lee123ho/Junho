from pico2d import *

class SecondFloor:
    def __init__(self):
        self.image = load_image('second_floor.png')
        self.bgm = load_music('BackgroundMusic.mp3')
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(400, 300)