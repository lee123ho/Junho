import random
import json
import os

from pico2d import *

import game_framework
from pig_magician import PigMagician
from second_floor import SecondFloor
from ghost_left import GhostLeft
from ghost_right import GhostRight
from symbol import *

name = "MainState"

ghosts_left = None
ghosts_right = None
width_symbols = None
length_symbols = None
ghost_left_time = 0
ghost_right_time = 0
KillPoint = 0


def create_world():
    global pig_magician, second_floor, ghost_left, ghost_right, symbol_width, symbol_length, ghosts_right, ghosts_left, width_symbols, length_symbols

    ghosts_left = []
    ghosts_right = []
    width_symbols = []
    length_symbols = []

    pig_magician = PigMagician()
    second_floor = SecondFloor()


def create_ghost(frame_time):
    global ghost_right_time, ghost_left_time
    ghost_left_time += frame_time
    ghost_right_time += frame_time

    if ghost_left_time >= 4:
        ghost_left = GhostLeft()
        ghosts_left.append(ghost_left)
        ghost_left_time = 0.0

    if ghost_right_time >= 5:
        ghost_right = GhostRight()
        ghosts_right.append(ghost_right)
        ghost_right_time = 0.0

def create_symbol(frame_time):
    global symbol_width, symbol_length
    for GhostsLeft in ghosts_left:
        if GhostsLeft.type == 1:
            symbol_width = WidthSymbol(*GhostsLeft.symbol_pos())
            width_symbols.append(symbol_width)
        else:
            symbol_length = LengthSymbol(*GhostsLeft.symbol_pos())
            length_symbols.append(symbol_length)

    for GhostsRight in ghosts_right:
        if GhostsRight.type == 1:
            symbol_width = WidthSymbol(*GhostsRight.symbol_pos())
            width_symbols.append(symbol_width)
        else:
            symbol_length = LengthSymbol(*GhostsRight.symbol_pos())
            length_symbols.append(symbol_length)


def kill_ghost(frame_time):
    global ghosts_right, ghosts_left, width_symbols, length_symbols, symbol_width, symbol_length, KillPoint

    for ghost_right in ghosts_right:
        if pig_magician.UpMousePosx != 0:
            if abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) > abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_right.type == 1:
                    ghosts_right.remove(ghost_right)
                    KillPoint += 1
            elif abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) < abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_right.type == 2:
                    ghosts_right.remove(ghost_right)
                    KillPoint += 1

    for ghost_left in ghosts_left:
        if pig_magician.UpMousePosx != 0:
            if abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) > abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_left.type == 1:
                    ghosts_left.remove(ghost_left)
                    KillPoint += 1
            elif abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) < abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_left.type == 2:
                    ghosts_left.remove(ghost_left)
                    KillPoint += 1


def enter():
    game_framework.reset_time()
    create_world()


def exit():
    global pig_magician, ghost_left, ghost_right, second_floor, symbol, ghosts_left, ghosts_right, width_symbols, length_symbols
    del (pig_magician)
    del (ghosts_left)
    del (ghosts_right)
    del (second_floor)
    del (width_symbols)
    del (length_symbols)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global KillPoint
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                pig_magician.handle_event(event)


def update(frame_time):
    global symbol_length, symbol_width, GhostsLeft
    pig_magician.update(frame_time)
    create_ghost(frame_time)
    create_symbol(frame_time)
    kill_ghost(frame_time)

    for ghost_left in ghosts_left:
        ghost_left.update(frame_time)

    for ghost_right in ghosts_right:
        ghost_right.update(frame_time)

    for GhostsRight in ghosts_right:
        if collide(pig_magician, GhostsRight):
            pig_magician.die()
            GhostsRight.stop()
            GhostsLeft.stop()

    for GhostsLeft in ghosts_left:
        if collide(pig_magician, GhostsLeft):
            pig_magician.die()
            GhostsLeft.stop()
            GhostsRight.stop()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:return False
    if right_a < left_b:return False
    if top_a < bottom_b:return False
    if bottom_a > top_b:return False

    return True


def draw(frame_time):
    global ghosts_right, ghosts_left, length_symbols, width_symbols
    all_ghosts = ghosts_left + ghosts_right
    all_symbols = length_symbols + width_symbols
    clear_canvas()
    second_floor.draw()
    for Ghosts in all_ghosts:
        Ghosts.draw()
        Ghosts.draw_bb()


    pig_magician.draw()
    for Symbols in all_symbols:
        Symbols.draw()

    pig_magician.draw_bb()

    update_canvas()





