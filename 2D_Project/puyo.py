from pico2d import *

RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, Z_DOWN, X_DOWN,\
RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, Z_UP, X_UP = range(12)

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
            #puyo.gravity +=1
            pass

    @staticmethod
    def exit(puyo, event):
        pass
    @staticmethod
    def do(puyo):
        if puyo.y > 200:
            puyo.y -= puyo.gravity
        #puyo.x = 35*1.49*puyo.line
        #delay(100)
        pass
    @staticmethod
    def draw(puyo):
        puyo.image.clip_draw(0,453,35,35,puyo.x,puyo.y,35*2,35*2)

class DropState:
    @staticmethod
    def enter(puyo,event):
        if event == RIGHT_DOWN:
            puyo.line +=1
        elif event == LEFT_DOWN:
            puyo.line -=1

    @staticmethod
    def exit(puyo,event):
        pass
    @staticmethod
    def do(puyo):
        if puyo.line > 3:
            puyo.line = 3
        elif puyo.line < -2:
            puyo.line = -2
        puyo.x = 445+ 35*2*puyo.line
    @staticmethod
    def draw(puyo):
        puyo.image.clip_draw(0,453,35,35,puyo.x,puyo.y,35*2,35*2)
    pass


class RotateState:
    pass


next_state_table = {
    IdleState: {RIGHT_DOWN:DropState, LEFT_DOWN:DropState,
                DOWN_DOWN:DropState, RIGHT_UP:DropState,
                LEFT_UP:DropState, DOWN_UP:DropState,
                UP_DOWN:RotateState, Z_DOWN:RotateState,
                X_DOWN:RotateState, UP_UP:RotateState,
                X_UP:RotateState, Z_UP:RotateState},
    DropState: {RIGHT_DOWN:IdleState, LEFT_DOWN:IdleState,
                DOWN_DOWN:IdleState, RIGHT_UP:IdleState,
                LEFT_UP:IdleState, DOWN_UP:IdleState,
                UP_DOWN:RotateState, Z_DOWN:RotateState,
                X_DOWN:RotateState, UP_UP:RotateState,
                X_UP:RotateState, Z_UP:RotateState},
    RotateState: {Z_DOWN: DropState, X_DOWN: DropState,
                  UP_DOWN: DropState, Z_UP: DropState,
                  X_UP: DropState, UP_UP:DropState}
}

class Puyo:

    def __init__(self):
        self.x, self.y = 445,720
        self.image = load_image('PC Computer - Puyo Puyo Tetris - Puyo Puyo Elements12.png')
        self.lastline = 0
        self.line = 0
        self.gravity = 1
        self.gravtimer = 100
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self,None)
        pass


    def change_state(self,  state):
        if len(self.event_que)>0:
            event = self.event_que.pop()
            self.cur_state.exit(self,event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self,event)
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0,event)
        # fill here
        pass


    def update(self):
        # fill here
        self.cur_state.do(self)
        if len(self.event_que)>0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass


    def draw(self):
        self.cur_state.draw(self)
        # fill here
        pass


    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)
        # fill here
        pass
