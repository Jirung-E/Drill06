from pico2d import *


open_canvas(1280, 1024)
hide_cursor()

background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

frame = 0
running = True
x, y = 640, 512
PADDING = 50
target_list = []
cursor_x, cursor_y = 0, 0
move_count = 0
MOVE_MAX = 100

def handle_events():
    events = get_events()
    for event in events:
        global running
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            target_list.append((event.x, 1024 - 1 - event.y))
        elif event.type == SDL_MOUSEMOTION:
            global cursor_x, cursor_y
            cursor_x, cursor_y = event.x, 1024 - 1 - event.y

while running:
    clear_canvas()
    background.draw(640, 512)
    for t in target_list:
        hand_arrow.draw(t[0], t[1])
    hand_arrow.draw(cursor_x, cursor_y)
    
    if move_count == 0:
        print('move start')
        start_x, start_y = x, y
        target_x, target_y = 100, 100
        d = 0 if target_x < start_x else 1

    t = move_count / MOVE_MAX
    x = (1-t)*start_x + t*target_x
    y = (1-t)*start_y + t*target_y
    character.clip_draw(frame * 100, 100 * d, 100, 100, x, y)
    move_count = (move_count + 1) % MOVE_MAX
    if move_count == 0:
        print('move end')
    
    update_canvas()

    handle_events()
    
    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()
