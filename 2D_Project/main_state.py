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
PuyoBackground = None
PuyoStage = None
font = None



def enter():
    global PuyoBackground, PuyoStage, puyo
    puyo = Puyo()
    PuyoBackground = Background()
    PuyoStage = Stage()
    game_world.add_object(PuyoBackground,0)
    game_world.add_object(PuyoStage,0)
    game_world.add_object(puyo,1)

def exit():
    #global PuyoBackground , PuyoStage ,puyo
    #del puyo
    #del PuyoBackground
    #del PuyoStage
    game_world.clear()



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
        else:
            puyo.handle_event(event)



def update():
    for game_object in game_world.all_objects():
        game_object.update()
    #puyo.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    #PuyoBackground.draw()
    #PuyoStage.draw()
    #puyo.draw()
    update_canvas()






