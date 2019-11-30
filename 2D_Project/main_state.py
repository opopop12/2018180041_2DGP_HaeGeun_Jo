import random
import json
import os

from pico2d import *

import game_world
import game_framework
from PuyoBackground import Background
from PuyoBackground import Stage
from puyo import *
from charactor_board import Charactor_Board

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

name = "MainState"

puyo = []
#puyo2 = None
PuyoBackground = None
PuyoStage = None
font = None
charactor_board = None
bgm = None

def enter():
    global PuyoBackground, PuyoStage, puyo, puyo2, charactor_board , bgm
    puyo = [Puyo() for i in range(90)]
    #puyo2 = Puyo()
    PuyoBackground = Background()
    PuyoStage = Stage()
    charactor_board = Charactor_Board()
    puyo[main_state.index+1].y += 35*1.8
    game_world.add_object(PuyoBackground,0)
    game_world.add_object(charactor_board,1)
    game_world.add_object(puyo[main_state.index],2)
    game_world.add_object(puyo[main_state.index+1],2)
    game_world.add_object(PuyoStage,3)
    bgm = load_music('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\\Sound\\PC Computer - Puyo Puyo Tetris - Sound Effects\\Other Sound Effects\\18 Play throughly the Puyopuyo.mp3')
    bgm.set_volume(10)
    bgm.repeat_play()

def exit():
    global bgm
    game_world.clear()
    del(bgm)

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

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            puyo[main_state.index +1].x = puyo[main_state.index].x -70
            puyo[main_state.index +1].y = puyo[main_state.index].y
        else:
            puyo[main_state.index].handle_event(event)
            puyo[main_state.index+1].handle_event(event)



def update():
    global index
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(PuyoStage, puyo[main_state.index]):
        #for pu in puyo:
            # collide(puyo[main_state.index],pu(not puyo[main_state.index])) or collide(puyo[main_state.index+1],pu(not puyo[main_state.index+1])):
                #puyo[main_state.index].gravity = 0
                #puyo[main_state.index+1].gravity = 0
        index +=2
        game_world.add_object(puyo[main_state.index],2)
        puyo[main_state.index + 1].y += 35 * 1.8
        game_world.add_object(puyo[main_state.index+1],2)

    for puyo in puyos:
        if main_state.index >= 1 and collide(puyo, puyos[main_state.index]):
            if main_state.index < 47:
                main_state.index += 1
            else:
                game_framework.quit()
            print(main_state.index)
          return game_framework.push_state(main_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





