from pico2d import *
import  game_world
import random

class Puyos:
    image = None
    frame = random.randint(1,5)

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Puyos.image == None:
            Puyos.image = load_image('PC Computer - Puyo Puyo Tetris - Puyo Puyo Elements12.png')
            self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.clip_draw(0,488-self.frame*35,35,35,self.x,self.y,35*2,35*2)

    def update(self):
        #if self.y >200:
        #   self.y -=self.velocity
        pass
