import random
import json
import os

from pico2d import *

import game_framework


#from boy import Boy
from PuyoBackground import Background



name = "MainState"

#boy = None
PuyoBackground = None
font = None



def enter():
    global PuyoBackground#,boy
    #boy = Boy()
    PuyoBackground = Background()


def exit():
    global PuyoBackground #,boy
    #del boy
    del PuyoBackground



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        #else:
           # boy.handle_event(event)



def update():
    pass
    #boy.update()

def draw():
    clear_canvas()
    PuyoBackground.draw()
    #boy.draw()
    update_canvas()






