from pico2d import *
import random

class Background:
    def __init__(self):
        self.image = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\Background\\5bf0a388b67da.jpg')
        self.image2 = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\\Background\\thumb-1920-989500.jpg')
        self.rand = random.randint(1,2)
        self.index = self.rand
    def update(self):
        pass
    def draw(self):
        #self.image.draw(960,540)
        if self.rand ==1:
            self.image.draw(960, 540)
        if self.rand ==2:
            self.image2.draw(960,540)

left = 192

#image * 1.4
#image2 * 1.5
#image3 *2  +20

class Stage:
    def __init__(self):
        self.image = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\\Background\\stage.png')
        self.image2 = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\\Background\\stage_sub_3.png')
        #self.image3 = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\\Background\\PC Computer - Puyo Puy'
                                 #'o Tetris - Character Boards.png')
        self.x, self.y = 480, 142
    def update(self):
        pass

    def get_bb(self):
        return self.x-150*1.49, self.y-33,self.x+150*1.49,self.y+30

    def draw(self):
        #self.image3.clip_draw(399, 1172, 192, 384, 480, 540, 415, 790)

        self.image.clip_draw(0, 202, 300, 44, 480, 939, 300*1.49, 66)
        self.image.clip_draw(0, 158, 300, 44, 480, 142, 300*1.49, 66)

        self.image.clip_draw(0, 202, 300, 44, 480+960, 939, 300*1.49, 66)
        self.image.clip_draw(0, 158, 300, 44, 480+960, 142, 300*1.49, 66)

        self.image2.clip_draw(141, 0, 12, 250, 692+960, 362, 12 * 1.49, 375)
        self.image2.clip_draw(124, 0, 12, 250, 265+960, 362, 12 * 1.49, 375)
        self.image2.clip_draw(59, 0, 12, 250, 692+960, 728, 12 * 1.49, 375)
        self.image2.clip_draw(42, 0, 12, 250, 265+960, 728, 12 * 1.49, 375)

        self.image2.clip_draw(141, 0, 12, 250, 692, 362, 12*1.49, 375)
        self.image2.clip_draw(124, 0, 12, 250, 265, 362, 12*1.49, 375)
        self.image2.clip_draw(59, 0, 12, 250, 692, 728, 12*1.49, 375)
        self.image2.clip_draw(42, 0, 12, 250, 265, 728, 12*1.49, 375)
        draw_rectangle(*self.get_bb())