from pico2d import *
import game_framework

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\Background\\thumb-1920-671798.jpg')


def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()