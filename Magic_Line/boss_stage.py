import random
import json
import os

from pico2d import *

import game_framework
from boss import Boss
from boss_pig_magician import PigMagician
from boss_floor import BossFloor
from boss_ghost_right import GhostRight
from boss_ghost_left import Ghostleft
from symbol import *
from boss_symbol import *
import game_over
import clear_staage

name = "BossStage"

boss = None
ghosts_left = None
ghosts_right = None
width_symbols = None
length_symbols = None
boss_symbols = None
symbol_width = None
symbol_length = None
boss_time = 0
fastghost_time = 0
ghost_right_time = 0
KillPoint = 0
GameOver = 0
boss_symbol_time = 0


def create_world():
    global pig_magician, boss_floor, ghost_left, ghost_right, boss_symbols,  symbol_width, symbol_length, ghosts_right, ghosts_left, width_symbols, length_symbols, boss, boss_symbol_width, boss_symbol_length

    ghosts_left = []
    ghosts_right = []
    width_symbols = []
    length_symbols = []
    boss_symbols = []

    boss = Boss()
    pig_magician = PigMagician()
    symbol_width = WidthSymbol
    symbol_length = LengthSymbol
    boss_symbol_width = BossWidthSymbol
    boss_symbol_length = BossLengthSymbol
    boss_floor = BossFloor()
    ghost_right = GhostRight
    ghost_left = Ghostleft


def create_ghost(frame_time):
    global ghost_right_time, fastghost_time, boss_time
    ghost_right_time += frame_time
    fastghost_time += frame_time
    boss_time += frame_time

    if boss_time >= 10:
        symbol_length = BossLengthSymbol(*boss.symbol_pos())
        length_symbols.append(symbol_length)
        boss_time = 0

    if fastghost_time >= 7:
        ghost_left = Ghostleft()
        ghosts_left.append(ghost_left)
        if ghost_left.type == 1:
            symbol_width = BossWidthSymbol(*ghost_left.symbol_pos())
            width_symbols.append(symbol_width)
        else:
            symbol_length = LengthSymbol(*ghost_left.symbol_pos())
            length_symbols.append(symbol_length)
        fastghost_time = 0

    if ghost_right_time >= 2:
        ghost_right = GhostRight()
        ghosts_right.append(ghost_right)
        if ghost_right.type == 1:
            symbol_width = WidthSymbol(*ghost_right.symbol_pos())
            width_symbols.append(symbol_width)
        else:
            symbol_length = LengthSymbol(*ghost_right.symbol_pos())
            length_symbols.append(symbol_length)
        ghost_right_time = 0.0


def kill_ghost(frame_time):
    global ghosts_right, ghosts_left, width_symbols, length_symbols, symbol_width, symbol_length, KillPoint, boss_symbol_time, boss_symbol_length, boss_symbols

    boss_symbol_time += frame_time

    if pig_magician.UpMousePosx != 0:
            for ghost_right in ghosts_right:
                if abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) > abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                    if ghost_right.type == 1:
                        ghosts_right.remove(ghost_right)
                        for symbol_width in width_symbols:
                            width_symbols.remove(symbol_width)
                        boss_symbol_time = 0
                elif abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) < abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                    for symbol_length in length_symbols:
                            length_symbols.remove(symbol_length)
                            KillPoint += 1
                    boss_symbol_time = 0

    if pig_magician.UpMousePosx != 0:
        for ghost_left in ghosts_left:
            if abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) > abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_left.type == 1:
                    ghosts_left.remove(ghost_left)
                    for symbol_width in width_symbols:
                        width_symbols.remove(symbol_width)
            elif abs(pig_magician.DownMousePosx - pig_magician.UpMousePosx) < abs(pig_magician.DownMousePosy - pig_magician.UpMousePosy):
                if ghost_left.type == 2:
                    ghosts_left.remove(ghost_left)
                    for symbol_length in length_symbols:
                        length_symbols.remove(symbol_length)

    print(KillPoint)

def enter():
    game_framework.reset_time()
    create_world()


def exit():
    global pig_magician, ghost_right, ghost_left, boss_floor, symbol, ghosts_left, ghosts_right, width_symbols, length_symbols, boss
    del(pig_magician)
    del(ghosts_right)
    del(ghost_left)
    del(boss_floor)
    del(width_symbols)
    del(length_symbols)
    del(boss)


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
        elif GameOver == 1:
            game_framework.change_state(game_over)
        elif KillPoint == 3:
            game_framework.change_state(clear_staage)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                pig_magician.handle_event(event)


def update(frame_time):
    global symbol_length, symbol_width, GameOver, pig_magician, ghost_left
    pig_magician.update(frame_time)
    boss.update(frame_time)
    create_ghost(frame_time)
    #create_symbol(frame_time)
    kill_ghost(frame_time)
    ghost_left.speed = 4
    BossWidthSymbol.speed = 4


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
            GameOver = 1

    for Ghostleft in ghosts_left:
        if collide(pig_magician, Ghostleft):
            pig_magician.die()
            Ghostleft.stop()
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
    global ghosts_right, ghosts_left, length_symbols, width_symbols, boss_symbols
    all_ghosts = ghosts_left + ghosts_right
    all_symbols = length_symbols + width_symbols + boss_symbols
    clear_canvas()
    boss_floor.draw()
    boss.draw()
    for Ghosts in all_ghosts:
        Ghosts.draw()
        #Ghosts.draw_bb()

    for Symbols in all_symbols:
        Symbols.draw()

    pig_magician.draw()
    #pig_magician.draw_bb()


    update_canvas()




