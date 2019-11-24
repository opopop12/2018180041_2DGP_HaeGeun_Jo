from pico2d import *
import random
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

import game_framework
import main_state

PIXEL_PER_METER = (10.0 / 10.0)
RUN_SPEED_KMPH = 3.6
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, Z_DOWN, X_DOWN,\
RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, Z_UP, X_UP, PUYO_TIMER = range(13)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_z): Z_DOWN,
    (SDL_KEYDOWN, SDLK_x): X_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYUP, SDLK_z): Z_UP,
    (SDL_KEYUP, SDLK_x): X_UP
}


class IdleState:
    @staticmethod
    def enter(puyo, event):
        if event == RIGHT_DOWN:
            puyo.line +=1
            pass
        elif event == LEFT_DOWN:
            puyo.line -=1
            pass
        elif event == DOWN_DOWN:
            puyo.gravity +=0.5 #RUN_SPEED_PPS
            pass
        elif event == DOWN_UP:
            puyo.gravity = 0.5 #RUN_SPEED_PPS

    @staticmethod
    def exit(puyo,event):
        pass

    @staticmethod
    def do(puyo):
        if puyo.y > puyo.lastline:
            puyo.y -= puyo.gravity
        pass
    @staticmethod
    def draw(puyo):
        puyo.image.clip_draw(0,488-puyo.frame*35,35,35,puyo.x,puyo.y+35*1.8,35*2,35*2)
        puyo.image.clip_draw(0,488-puyo.frame2*35,35,35,puyo.x,puyo.y,35*2,35*2)

class DropState:
    @staticmethod
    def enter(puyo, event):
        if event == RIGHT_DOWN:
            puyo.line +=1
        elif event == LEFT_DOWN:
            puyo.line -=1
        elif event == DOWN_DOWN:
            puyo.gravity +=0.5
        elif event == DOWN_UP:
            puyo.gravity = 0.5

    @staticmethod
    def exit(puyo,event):
        pass

    @staticmethod
    def do(puyo):
        if puyo.line > 3:
            puyo.line = 3
        elif puyo.line < -2:
            puyo.line = -2
        if puyo.y > puyo.lastline:
            puyo.y -= puyo.gravity
        if puyo.y > puyo.lastline:
            puyo.x = 445 + 35*2*puyo.line

    @staticmethod
    def draw(puyo):
        puyo.image.clip_draw(0,488-puyo.frame*35,35,35,puyo.x,puyo.y+35*1.8,35*2,35*2)
        puyo.image.clip_draw(0,488-puyo.frame2*35,35,35,puyo.x,puyo.y,35*2,35*2)
    pass


class RotateState:
    @staticmethod
    def enter (puyo,event):
       # if event == Z_DOWN:
        pass
    pass


next_state_table = {
    IdleState: {RIGHT_DOWN:DropState, LEFT_DOWN:DropState,
                DOWN_DOWN:DropState, RIGHT_UP:DropState,
                LEFT_UP:DropState, DOWN_UP:DropState,
                UP_DOWN:RotateState, Z_DOWN:RotateState,
                X_DOWN:RotateState, UP_UP:RotateState,
                X_UP:RotateState, Z_UP:RotateState,PUYO_TIMER:IdleState},
    DropState: {RIGHT_DOWN:IdleState, LEFT_DOWN:IdleState,
                DOWN_DOWN:IdleState, RIGHT_UP:IdleState,
                LEFT_UP:IdleState, DOWN_UP:IdleState,
                UP_DOWN:RotateState, Z_DOWN:RotateState,
                X_DOWN:RotateState, UP_UP:RotateState,
                X_UP:RotateState, Z_UP:RotateState,PUYO_TIMER:IdleState},
    RotateState: {RIGHT_DOWN:IdleState, LEFT_DOWN:IdleState,
                DOWN_DOWN:IdleState, RIGHT_UP:IdleState,
                LEFT_UP:IdleState, DOWN_UP:IdleState,
                UP_DOWN:RotateState, Z_DOWN:RotateState,
                X_DOWN:RotateState, UP_UP:RotateState,
                X_UP:RotateState, Z_UP:RotateState,PUYO_TIMER:IdleState}
}

class Puyo:

    def __init__(self):
        self.x, self.y = 445, 830
        self.image = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\\Puyo\\PC Computer - Puyo Puyo Tetris - Puyo Puyo Elements12.png')
        self.lastline = 200
        self.line = 0
        self.dir = 1
        self.gravity = 0.5
        self.frame = random.randint(1, 5)
        self.frame2 = random.randint(1, 5)
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.index = 0
        pass

    def change_state(self,  state):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        # fill here
        pass

    def get_bb(self):
        return self.x - 35, self.y - 30, self.x + 35, self.y + 35

    def add_event(self, event):
        self.event_que.insert(0, event)
        # fill here
        pass

    def build_behavior_tree(self):
        #drop_node = LeafNode("Gravity Drop", self.drop)
        find_near_puyo_node = LeafNode("Find Near Puyo", self.find_near_puyo)
        delete_puyo_node = LeafNode("Delete Puyo", self.delete_puyo)
        puyo_block_node = SequenceNode("Puyo Block")
        puyo_block_node.add_children(find_near_puyo_node, delete_puyo_node)
        puyo_drop_node = SelectorNode("Puyo Drop")
        puyo_drop_node.add_children(puyo_block_node)#,drop_node)
        self.bt = BehaviorTree(puyo_drop_node)

    def update(self):
        # fill here
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        #self.bt.run()
        pass


    def draw(self):
        self.cur_state.draw(self)
        # fill here
        draw_rectangle(*self.get_bb())
        pass


    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)
        # fill here
        pass
