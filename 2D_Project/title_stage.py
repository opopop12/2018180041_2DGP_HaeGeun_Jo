from pico2d import *
import game_framework
import main_state

name = "TitleState"
image = None
image2 = None
bgm = None

def enter():
    global image, image2,bgm
    image = load_image('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\Background\\thumb-1920-671798.jpg')
    image2 = load_image("6481489.jpg")
    bgm = load_music('D:\\github\\2018180041_2DGP_HaeGeun_Jo\\2D_Project\\Sound\\PC Computer - Puyo Puyo Tetris - Sound Effects\\Other Sound Effects\\03 It is Main Menu!.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image,image2,bgm
    del (image)
    del (image2)
    del (bgm)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(960, 540)
    image2.draw(960, 540)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass