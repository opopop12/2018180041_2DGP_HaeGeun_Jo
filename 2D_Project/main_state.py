import random
import json
import os

from pico2d import *

import game_world
import game_framework
from PuyoBackground import Background
from PuyoBackground import Stage
from puyo import *
index = 0
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    if not(a.get_bb() == b.get_bb()):
        return True

def collide_side(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    if collide(a, b):
        if left_a < right_b: return True
        if right_a > left_b: return True

        return False



name = "MainState"

puyos = []
PuyoBackground = None
PuyoStage = None
font = None

def enter():
    global PuyoBackground, PuyoStage, puyos
    puyos = [Puyo() for i in range(48)]
    PuyoBackground = Background()
    PuyoStage = Stage()
    game_world.add_object(PuyoBackground,0)
    game_world.add_object(PuyoStage,1)
    game_world.add_object(puyos[main_state.index],2)


def exit():
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
            puyos[main_state.index].handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(PuyoStage,puyos[main_state.index]):
        main_state.index+=1
        print(main_state.index)
        return game_framework.push_state(main_state)
    for puyo in puyos:
        if main_state.index >= 1 and collide(puyo, puyos[main_state.index]):
            main_state.index += 1
            print(main_state.index)
            return game_framework.push_state(main_state)


def draw():

    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





