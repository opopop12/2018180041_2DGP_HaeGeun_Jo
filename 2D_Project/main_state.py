import random
import json
import os

from pico2d import *

import game_world
import game_framework


#from boy import Boy
from PuyoBackground import Background
from PuyoBackground import Stage
from puyo import Puyo


name = "MainState"

puyo = None
puyo1 =None
PuyoBackground = None
PuyoStage = None
font = None

def enter():
    global PuyoBackground, PuyoStage, puyo, puyo1
    puyo = Puyo()
    puyo1 = Puyo()
    PuyoBackground = Background()
    PuyoStage = Stage()

def exit():
    global PuyoBackground , PuyoStage ,puyo, puyo1
    del puyo
    del PuyoBackground
    del PuyoStage
    del puyo1



def pause():
    pass


def resume():
    pass


def handle_events():
    global  index
    index=0
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            if index == 0:
                puyo.handle_event(event)
                index +=1
            elif index == 1:
                puyo1.handle_event(event)
                index -=1


def update():
    puyo.update()

def draw():
    clear_canvas()
    PuyoBackground.draw()
    PuyoStage.draw()
    puyo.draw()
    puyo1.draw()
    update_canvas()






