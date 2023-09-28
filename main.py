from pico2d import *
import random


open_canvas(1280, 1024)

background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

frame = 0
running = True
x, y = 640, 512
PADDING = 50

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

while running:
    start_x, start_y = x, y
    target_x, target_y = random.randint(PADDING, 1280-PADDING), random.randint(PADDING, 1024-PADDING)
    d = 0 if target_x < start_x else 1

    for i in range(0, 100+1, 5):
        clear_canvas()
        background.draw(640, 512)
        hand_arrow.draw(target_x, target_y)
        
        t = i/100
        x = (1-t)*start_x + t*target_x
        y = (1-t)*start_y + t*target_y
        character.clip_draw(frame * 100, 100 * d, 100, 100, x, y)
        
        update_canvas()

        handle_events()
        
        frame = (frame + 1) % 8
        delay(0.05)


close_canvas()
