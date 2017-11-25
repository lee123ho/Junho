import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

boy = None
grass = None
font = None
die = 0
kill = 0
act = 0
up = 0
dmx = 0
dmy = 0
umx = 0
umy = 0

class Grass:
    def __init__(self):
        self.image = load_image('room.png')

    def draw(self):
        self.image.draw(400, 300)

class Boy:
    global dmx, dmy, umx, umy, up, act, kill

    def __init__(self):
        self.x, self.y = 400, 300
        if up == 0:
            self.frame = 0
        else:
            self.frame = 5
        self.image = load_image('pig_magician3.png')

    def update(self):
        global dmx, dmy, umx, umy, up, act, kill
        print(abs(dmy))
        if act == 1:
            if abs(dmx - umx) > abs(umy - dmy):
                self.frame += 1
                delay(0.05)
                if self.frame == 5:
                    self.frame = 0
                    act = 0
                    kill = 1
            elif abs(umy - dmy) > abs(dmx - umx):
                up = 1
                self.frame += 1
                delay(0.05)
                if self.frame == 8:
                    self.frame = 0
                    act = 0
                    kill = 2

    def draw(self):
        self.image.clip_draw(self.frame * 300, 0, 250, 300, self.x, self.y)

class Ghost1:
    def __init__(self):
        self.x, self.y = random.randint(650, 700), random.randint(200,400)
        self.image = load_image('ghost1.png')

    def update(self):
        if self.x > 400:
            self.x -= 0.5
        if self.y - 300 < 0:
            self.y += 0.5
        else:
            self.y -= 0.5

    def draw(self):
        global kill
        if kill < 1:
            self.image.draw(self.x, self.y)

class Ghost2:
    def __init__(self):
        self.x, self.y = random.randint(0, 50), random.randint(200,400)
        self.image = load_image('ghost2.png')

    def update(self):
        if self.x < 400:
            self.x += 0.5
        if self.y - 300 < 0:
            self.y += 0.5

    def draw(self):
        global kill
        if kill < 2:
            self.image.draw(self.x, self.y)


def enter():
    global boy, ghost1, ghost2, grass
    boy = Boy()
    ghost1 = Ghost1()
    ghost2 = Ghost2()
    grass = Grass()


def exit():
    global boy, ghost1, ghost2, grass
    del(boy)
    del(ghost1)
    del(ghost2)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global dmx, dmy, umx, umy, act
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            dmx, dmy = event.x, event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            umx, umy = event.x, event.y
            act = 1
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()




def update(frame_time):
    boy.update()
    ghost1.update()
    ghost2.update()


def draw(frame_time):
    clear_canvas()
    grass.draw()
    ghost1.draw()
    ghost2.draw()
    boy.draw()
    update_canvas()





