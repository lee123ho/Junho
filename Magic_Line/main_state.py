import random
import json
import os

from pico2d import *

import game_framework
from pig_magician import PigMagician
from first_floor import FirstFloor
from ghost_left import GhostLeft
from ghost_right import GhostRight
from symbol import *
from mouse_move_line import MouseLine
import second_stage
import game_over

name = "MainStage"

ghosts_left = None
ghosts_right = None
width_symbols = None
length_symbols = None
symbol_width = None
symbol_length = None
mouses = None
ghost_left_time = 0
ghost_right_time = 0
KillPoint = 0
GameOver = 0
right_die = 0
left_die = 0

class BGM:
    def __init__(self):
        self.bgm = load_music('BackgroundMusic.mp3')
        self.bgm.repeat_play()


def create_world():
    global pig_magician, first_floor, ghost_left, ghost_right, symbol_width, symbol_length, ghosts_right, ghosts_left, width_symbols, length_symbols, mouses

    ghosts_left = []
    ghosts_right = []
    width_symbols = []
    length_symbols = []
    mouses = []

    pig_magician = PigMagician()
    first_floor = FirstFloor()
    symbol_width = WidthSymbol
    symbol_length = LengthSymbol


def create_ghost(frame_time):
    global ghost_right_time, ghost_left_time
    ghost_left_time += frame_time
    ghost_right_time += frame_time

    if ghost_left_time >= 2:
        ghost_left = GhostLeft()
        ghosts_left.append(ghost_left)
        if ghost_left.type == 1:
            symbol_width = WidthSymbol(*ghost_left.symbol_pos())
            width_symbols.append(symbol_width)
        else:
            symbol_length = LengthSymbol(*ghost_left.symbol_pos())
            length_symbols.append(symbol_length)
        ghost_left_time = 0.0

    if ghost_right_time >= 3:
        ghost_right = GhostRight()
        ghosts_right.append(ghost_right)
        if ghost_right.type == 1:
            symbol_width = WidthSymbol(*ghost_right.symbol_pos())
            width_symbols.append(symbol_width)
        else:
            symbol_length = LengthSymbol(*ghost_right.symbol_pos())
            length_symbols.append(symbol_length)
        ghost_right_time = 0.0




def delete_symbol(frame_time):
    global symbol_width, symbol_length

    if pig_magician.UpMousePosx != 0:
        if abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) > abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
            for symbol_width in width_symbols:
                    width_symbols.remove(symbol_width)
        elif abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) < abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
            for symbol_length in length_symbols:
                length_symbols.remove(symbol_length)

    if pig_magician.UpMousePosx != 0:
        if abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) > abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
            for symbol_width in width_symbols:
                width_symbols.remove(symbol_width)
        elif abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) < abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
            for symbol_length in length_symbols:
                length_symbols.remove(symbol_length)


def kill_ghost(frame_time):
    global ghosts_right, ghosts_left, width_symbols, length_symbols, symbol_width, symbol_length, KillPoint, right_die, left_die

    if pig_magician.UpMousePosx != 0:
        for ghost_right in ghosts_right:
            if abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) > abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_right.type == 1:
                    right_die = 1
                    ghosts_right.remove(ghost_right)
                    for symbol_width in width_symbols:
                        width_symbols.remove(symbol_width)
                    KillPoint += 1
            elif abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) < abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_right.type == 2:
                    right_die = 1
                    ghosts_right.remove(ghost_right)
                    for symbol_length in length_symbols:
                        length_symbols.remove(symbol_length)
                    KillPoint += 1

    if pig_magician.UpMousePosx != 0:
        for ghost_left in ghosts_left:
            if abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) > abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_left.type == 1:
                    left_die = 1
                    ghosts_left.remove(ghost_left)
                    for symbol_width in width_symbols:
                        width_symbols.remove(symbol_width)
                    KillPoint += 1
            elif abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) < abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_left.type == 2:
                    left_die = 1
                    ghosts_left.remove(ghost_left)
                    for symbol_length in length_symbols:
                        length_symbols.remove(symbol_length)
                    KillPoint += 1

def mouse_inout(frame_time):
    mouse = MouseLine()
    mouses.append(mouse)


def enter():
    game_framework.reset_time()
    create_world()


def exit():
    global pig_magician, ghost_left, ghost_right, first_floor, symbol, ghosts_left, ghosts_right, width_symbols, length_symbols, mouses
    del(pig_magician)
    del(ghosts_left)
    del(ghosts_right)
    del(first_floor)
    del(width_symbols)
    del(length_symbols)
    del(mouses)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global KillPoint, GameOver
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif KillPoint == 20:
            game_framework.change_state(second_stage)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_l):
            game_framework.change_state(second_stage)
        elif GameOver == 1:
            game_framework.change_state(game_over)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                pig_magician.handle_event(event)


def update(frame_time):
    global symbol_length, symbol_width, GhostsLeft, GameOver, right_die, left_die
    pig_magician.update(frame_time)
    create_ghost(frame_time)
    #create_symbol(frame_time)
    kill_ghost(frame_time)
    delete_symbol(frame_time)

    for ghost_left in ghosts_left:
        ghost_left.update(frame_time)

    for ghost_right in ghosts_right:
        ghost_right.update(frame_time)

    for symbol_width in width_symbols:
        symbol_width.update(frame_time)

    for symbol_length in length_symbols:
        symbol_length.update(frame_time)

    for GhostsRight in ghosts_right:
        if collide(pig_magician, GhostsRight):
            pig_magician.die()
            GhostsRight.stop()
            GhostsLeft.stop()
            GameOver = 1

    for GhostsLeft in ghosts_left:
        if collide(pig_magician, GhostsLeft):
            pig_magician.die()
            GhostsLeft.stop()
            GhostsRight.stop()
            GameOver = 1


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:return False
    if right_a < left_b:return False
    if top_a < bottom_b:return False
    if bottom_a > top_b:return False

    return True


def draw(frame_time):
    global ghosts_right, ghosts_left, length_symbols, width_symbols, mouses
    all_ghosts = ghosts_left + ghosts_right
    all_symbols = length_symbols + width_symbols
    clear_canvas()
    first_floor.draw()
    for Ghosts in all_ghosts:
        Ghosts.draw()
        #Ghosts.draw_bb()

    for Mouse in mouses:
        Mouse.draw()

    pig_magician.draw()
    for Symbols in all_symbols:
        Symbols.draw()

    #pig_magician.draw_bb()

    update_canvas()





