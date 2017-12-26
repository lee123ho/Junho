import random
import json
import os

from pico2d import *

import game_framework
import main_state

class PigMagician:

    image = None
    width_bgm = None
    length_bgm = None
    back_music = None

    def __init__(self):
        self.x, self.y = 200, 300
        self.DownMousePosx = 0
        self.DownMousePosy = 0
        self.UpMousePosx = 0
        self.UpMousePosy = 0
        self.frame = 0
        self.act = 0
        PigMagician.image = load_image('pig_magician_200.png')
        if PigMagician.width_bgm == None:
            PigMagician.width_bgm = load_music('width.mp3')
        if PigMagician.length_bgm == None:
            PigMagician.length_bgm = load_music('length.mp3')

    def update(self, frame_time):
        #print(abs(self.DownMousePosx - self.UpMousePosx) - abs(self.UpMousePosy - self.DownMousePosy))
        if self.act == 1:
            if abs(self.DownMousePosx - self.UpMousePosx) > abs(self.UpMousePosy - self.DownMousePosy):
                self.frame += 1
                if self.frame == 5:
                    self.frame = 0
                    self.act = 0
                    self.DownMousePosx, self.DownMousePosy, self.UpMousePosx, self.UpMousePosy = 0, 0, 0, 0
                    PigMagician.width_bgm.play()
            elif abs(self.DownMousePosx - self.UpMousePosx) < abs(self.UpMousePosy - self.DownMousePosy):
                self.frame += 1
                if self.frame == 8:
                    self.frame = 0
                    self.act = 0
                    PigMagician.length_bgm.play()
                    self.DownMousePosx, self.DownMousePosy, self.UpMousePosx, self.UpMousePosy = 0, 0, 0, 0
        if self.die == True:
            self.frame = 0
            self.frame += 1
            if self.frame == 4:
                pass

    def die(self):
        PigMagician.image = load_image('pig_die.png')

    def get_bb(self):
        return self.x - 42, self. y - 74, self.x + 58, self.y + 70

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.image.clip_draw(self.frame * 300, 0, 250, 250, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            self.DownMousePosx, self.DownMousePosy = event.x, event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            self.UpMousePosx, self.UpMousePosy = event.x, event.y
            self.act = 1