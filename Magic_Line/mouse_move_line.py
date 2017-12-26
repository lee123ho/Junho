from pico2d import *

class MouseLine:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.mouse_inout = 0
        self.mouse_posx = 0
        self.mouse_posy = 0
        self.image = load_image('mouse_postion.png')

    def get_mouse_pos(self):
        if self.mouse_inout == 1:
            return self.mouse_posx, self.mouse_posy

    def handle_event(self, event):
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            self.mouse_inout = 1
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            self.mouse_inout = 0
        if (event.type, event.button) == (SDL_MOUSEMOTION):
            self.mouse_posx, self.mouse_posy = event.x, event. y

    def draw(self):
        self.image.draw(self.x, self.y)