from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('5bf0a388b67da.jpg')

    def draw(self):
        self.image.draw(960, 540)

class Stage:
    def __init__(self):
        self.image = load_image('stage.png')
    def draw(self):
        self.image.clip_draw(0,158,298,84,480,540,447,126)