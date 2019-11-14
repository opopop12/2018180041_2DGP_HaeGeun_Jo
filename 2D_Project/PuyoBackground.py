from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('5bf0a388b67da.jpg')
    def update(self):
        pass
    def draw(self):
        self.image.draw(960, 540)

left = 192

#image * 1.4
#image2 * 1.5
#image3 *2  +20
class Stage:
    def __init__(self):
        self.image = load_image('stage.png')
        self.image2 = load_image('stage_sub_3.png')
        self.image3 = load_image('PC Computer - Puyo Puyo Tetris - Character Boards.png')

    def update(self):
        pass
    def draw(self):
        self.image3.clip_draw(399, 1172, 192, 384, 480, 540, 415, 790)

        self.image.clip_draw(0, 202, 300, 44, 480, 939, 300*1.49, 66)
        self.image.clip_draw(0, 158, 300, 44, 480, 142, 300*1.49, 66)

        self.image2.clip_draw(141, 0, 12, 250, 692, 362, 12*1.49, 375)
        self.image2.clip_draw(124, 0, 12, 250, 265, 362, 12*1.49, 375)
        self.image2.clip_draw(59, 0, 12, 250, 692, 728, 12*1.49, 375)
        self.image2.clip_draw(42, 0, 12, 250, 265, 728, 12*1.49, 375)