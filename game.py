import turtle
from time import sleep

from helpers.blocks_helper import create_blocks
from helpers.key_helper import create_key, init_key_helper, key_collision
from helpers.movement_helper import move, player_spawn
from helpers.shoot_helper import (BULLET_VELOCITY, draw_bullets,
                                  init_shoot_helper, shoot)
from state.game_state import (CLOUD_HEIGHT, FLOOR_HEIGHT,
                              LEFT_SCREEN_WALL_WIDTH, LEFT_SCREEN_WALL_X,
                              SCREEN_HEIGHT, SCREEN_WIDTH)
from state.player_state import plr_state

# Global variables ----------------------------
t = None
s = None
hearts = None
doors = None
plr = None
sec_plr = None

ANIMATION_STEP = 5
GRAVITY = 0.1
VELOCITY_JUMP = 0.2

velocity = 0

keys_pressed = None

game_props = None

# block centers -----------------------
blocks_good_plr = None
blocks_evil_plr = None
keys = None

winner = None  # 'good' / 'evil'


# ---------------------------------------------


def draw():
    t.goto(0, -s.window_height() / 2)

    s.addshape('images/floor.gif')
    s.addshape('images/plr.gif')
    s.addshape('images/block.gif')
    s.addshape('images/cloud.gif')
    s.addshape('images/evil_plr.gif')
    s.addshape('images/winter_bg.gif')
    s.addshape('images/evil_circle2.gif')
    s.addshape('images/key.gif')
    s.addshape('images/full_hearts.gif')
    s.addshape('images/door_locked.gif')

    # s.bgpic('images/winter_bg.gif')

    # plr.goto(200, 0)
    hearts.goto(-170, SCREEN_HEIGHT / 2 - 50)
    hearts.shape('images/full_hearts.gif')

    doors.goto(SCREEN_WIDTH / 2 - 40, 190)
    doors.shape('images/door_locked.gif')

    plr.shape('images/plr.gif')
    player_spawn(plr)

    sec_plr.goto(-340, 0)
    sec_plr.shape('images/evil_circle2.gif')

    t.goto(0, -s.window_height() / 2)

    create_blocks(t, blocks_good_plr)
    create_key(keys)


def init_events():
    def on_key_press(key):
        if key in keys_pressed:
            keys_pressed[key] = True

    def on_key_release(key):
        if key in keys_pressed:
            keys_pressed[key] = False

    s.onkeypress(lambda: on_key_press('Up'), 'Up')
    s.onkeypress(lambda: on_key_press('Down'), 'Down')
    s.onkeypress(lambda: on_key_press('Left'), 'Left')
    s.onkeypress(lambda: on_key_press('Right'), 'Right')
    s.onkeyrelease(lambda: on_key_release('Up'), 'Up')
    s.onkeyrelease(lambda: on_key_release('Down'), 'Down')
    s.onkeyrelease(lambda: on_key_release('Left'), 'Left')
    s.onkeyrelease(lambda: on_key_release('Right'), 'Right')

    s.onkeypress(lambda: on_key_press('w'), 'w')
    s.onkeypress(lambda: on_key_press('s'), 's')
    s.onkeypress(lambda: on_key_press('z'), 'z')
    s.onkeyrelease(lambda: on_key_release('w'), 'w')
    s.onkeyrelease(lambda: on_key_release('s'), 's')
    s.onkeyrelease(lambda: on_key_release('z'), 'z')


def move_player_1():
    movement = {
        'center_x': plr.xcor(),
        'center_y': plr.ycor(),
        'dx': 0,
        'dy': 0,
    }

    if keys_pressed['Left']:
        movement['dx'] = -ANIMATION_STEP
        move(movement, blocks_good_plr, plr, game_props)

    if keys_pressed['Right']:
        movement['dx'] = ANIMATION_STEP
        move(movement, blocks_good_plr, plr, game_props)

    if keys_pressed['Down']:
        movement['dy'] = -ANIMATION_STEP
        move(movement, blocks_good_plr, plr, game_props)

    if keys_pressed['Up']:
        movement['dy'] = ANIMATION_STEP
        move(movement, blocks_good_plr, plr, game_props)

    global velocity
    velocity += GRAVITY

    is_collide = move(
        {
            'center_x': plr.xcor(),
            'center_y': plr.ycor(),
            'dx': 0,
            'dy': -velocity,
        },
        blocks_good_plr,
        plr,
        game_props,
    )

    if is_collide:
        velocity = -velocity * VELOCITY_JUMP


def move_evil_player():
    movement = {
        'center_x': sec_plr.xcor(),
        'center_y': sec_plr.ycor(),
        'dx': 0,
        'dy': 0,
    }

    if keys_pressed['w']:
        movement['dy'] = ANIMATION_STEP
        move(movement, blocks_evil_plr, sec_plr, game_props)

    if keys_pressed['s']:
        movement['dy'] = -ANIMATION_STEP
        move(movement, blocks_evil_plr, sec_plr, game_props)

    if keys_pressed['z']:
        shoot(
            {
                'x': sec_plr.xcor(),
                'y': sec_plr.ycor(),
                'velocity': BULLET_VELOCITY,
            },
            blocks_good_plr,
            plr,
        )


def check_hearts():
    s.addshape('images/half_hearts.gif')
    s.addshape('images/almost_no_hearts.gif')
    s.addshape('images/no_hearts.gif')

    if plr_state['player_lives'] == 2:
        hearts.shape('images/half_hearts.gif')
    elif plr_state['player_lives'] == 1:
        hearts.shape('images/almost_no_hearts.gif')
    elif plr_state['player_lives'] == 0:
        hearts.shape('images/no_hearts.gif')


def check_doors():
    s.addshape('images/door.gif')
    if plr_state['keys_collected'] == 1:
        doors.shape('images/door.gif')
        plr_state['door_unlocked'] += 1


def game_loop():
    global winner
    check_hearts()
    check_doors()

    if plr_state['player_lives'] == 0 or game_props['IsEnd']:
        if game_props['IsEnd']:
            winner = 'good'
        else:
            winner = 'evil'
        end_game()
    else:
        move_player_1()
        move_evil_player()
        draw_bullets(blocks_good_plr, plr)
        key_collision(plr, keys)
        s.ontimer(game_loop, 5)


def end_game():
    print('end game')
    sleep(1)
    s.bye()


def init_globals():
    global t, s, hearts, doors, plr, sec_plr, keys_pressed, game_props, blocks_good_plr, blocks_evil_plr, keys
    turtle.TurtleScreen._RUNNING = True

    t = turtle.Turtle()
    s = turtle.Screen()

    hearts = turtle.Turtle()
    doors = turtle.Turtle()

    plr = turtle.Turtle()
    sec_plr = turtle.Turtle()

    s.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    keys_pressed = {
        'Right': False,
        'Left': False,
        'Up': False,
        'Down': False,
        'w': False,
        's': False,
        'z': False,
    }

    game_props = {'IsEnd': False}

    # block centers -----------------------
    blocks_good_plr = [
        {
            'id': 'left_screen_wall',
            'center_x': -SCREEN_WIDTH / 2 + LEFT_SCREEN_WALL_X,
            'center_y': 0,
            'width': LEFT_SCREEN_WALL_WIDTH,
            'height': SCREEN_HEIGHT,
            'img': None,
            'color': 'grey',
            'bullet_not_wall': True,
            'bad_block': False,
            'exit_block': False,
        },
        {
            'id': 'right_screen_wall',
            'center_x': SCREEN_WIDTH / 2 + 1,
            'center_y': 0,
            'width': 1,
            'height': SCREEN_HEIGHT,
            'img': None,
            'color': None,
            'bullet_not_wall': False,
            'bad_block': False,
            'exit_block': False,
        },
        {
            'id': 'top_screen_wall',
            'center_x': 0,
            'center_y': -SCREEN_HEIGHT / 2 - 1,
            'width': SCREEN_WIDTH,
            'height': 1,
            'img': None,
            'color': None,
            'bullet_not_wall': False,
            'bad_block': False,
            'exit_block': False,
        },
        {
            'id': 'bot_screen_wall',
            'center_x': 0,
            'center_y': SCREEN_HEIGHT / 2 + 1,
            'width': SCREEN_WIDTH,
            'height': 1,
            'img': None,
            'color': None,
            'bullet_not_wall': False,
            'bad_block': False,
            'exit_block': False,
        },
        {
            'id': 'floor',
            'center_x': 124,
            'center_y': -SCREEN_HEIGHT / 2,
            'width': 800,
            'height': FLOOR_HEIGHT,
            'img': 'images/floor.gif',
            'color': None,
            'bullet_not_wall': False,
            'bad_block': True,
            'exit_block': False,
        },
        {
            'id': 'cloud',
            'center_x': -215,
            'center_y': -SCREEN_HEIGHT / 2 + 54,
            'width': 126,
            'height': CLOUD_HEIGHT,
            'img': 'images/cloud.gif',
            'color': None,
            'bullet_not_wall': False,
            'bad_block': False,
            'exit_block': False,
        },
        {
            'id': 'rect1',
            'center_x': 190,
            'center_y': -190,
            'width': 194,
            'height': 62,
            'img': 'images/block.gif',
            'color': None,
            'bullet_not_wall': False,
            'bad_block': False,
            'exit_block': False,
        },
        {
            'id': 'rect2',
            'center_x': -100,
            'center_y': 0,
            'width': 194,
            'height': 62,
            'img': 'images/block.gif',
            'color': None,
            'bullet_not_wall': False,
            'bad_block': False,
            'exit_block': False,
        },
        {
            'id': 'rect3',
            'center_x': SCREEN_WIDTH / 2,
            'center_y': 100,
            'width': 194,
            'height': 62,
            'img': 'images/block.gif',
            'color': None,
            'bullet_not_wall': False,
            'bad_block': False,
            'exit_block': True,
        },
    ]

    blocks_evil_plr = [
        {
            'id': 'top_screen_wall',
            'center_x': 0,
            'center_y': -SCREEN_HEIGHT / 2 - 1,
            'width': SCREEN_WIDTH,
            'height': 1,
            'img': None,
            'color': None,
            'bad_block': False,
            'exit_block': False,
        },
        {
            'id': 'bot_screen_wall',
            'center_x': 0,
            'center_y': SCREEN_HEIGHT / 2 + 1,
            'width': SCREEN_WIDTH,
            'height': 1,
            'img': None,
            'color': None,
            'bad_block': False,
            'exit_block': False,
        },
    ]

    keys = [
        {
            'id': 'key1',
            'center_x': -100,
            'center_y': 80,
            'width': 104,
            'height': 59,
            'img': 'images/key.gif',
            'color': None,
            'bullet_not_wall': False,
            'bad_block': False,
            'is_blank': False,
        },
    ]


def init():
    init_globals()
    init_shoot_helper()
    init_key_helper()

    #  lift the "pen" off the drawing canvas
    #  so that moving the turtle does not draw lines.
    plr.penup()
    sec_plr.penup()
    hearts.penup()
    doors.penup()
    t.penup()

    # prevent default step-animation on screen load
    s.delay(0)

    draw()

    s.listen()

    init_events()

    game_loop()

    s.mainloop()


def start_game():
    init()
    return winner
