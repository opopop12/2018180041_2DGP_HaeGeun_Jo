import game_framework
import pico2d

import title_stage

pico2d.open_canvas(1920,1080)
game_framework.run(title_stage)
pico2d.close_canvas()