from pico2d import *
import  game_world
import random

class Puyos:
    image = None
    frame = random.randint(1,5)

    def __init__(self, x=400, y= 300, gravity = 1):
        if Puyos.image == None:
            Puyos.image = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\\Puyo\\PC Computer - Puyo Puyo Tetris - Puyo Puyo Elements12.png')
            self.x, self.y, self.gravity = x, y, gravity

    def draw(self):
        self.image.clip_draw(0,488-self.frame*35,35,35,self.x,self.y,35*2,35*2)
        pass
    def update(self):
        #if self.y >200:
        #   self.y -=self.velocity
        pass
