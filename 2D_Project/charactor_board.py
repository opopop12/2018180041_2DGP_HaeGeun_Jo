from pico2d import *

class Charactor_Board:
    def __init__(self):
        self.image = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\\Background\\PC Computer - Puyo Puy'
                                 'o Tetris - Character Boards.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(399, 1172, 192, 384, 480, 540, 415, 790)
