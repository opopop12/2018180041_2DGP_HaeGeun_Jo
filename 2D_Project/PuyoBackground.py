from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('5bf0a388b67da.jpg')

    def draw(self):
        self.image.draw(960, 540)