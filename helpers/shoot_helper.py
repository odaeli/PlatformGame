import turtle

from helpers.movement_helper import is_rect_collide, player_spawn
from state.player_state import plr_state

create_block = None
BULLET_WIDTH = 20
BULLET_HEIGHT = 10
BULLET_VELOCITY = 20

bullets = []


def init_shoot_helper():
    global create_block
    create_block = turtle.Turtle()
    create_block.penup()
    create_block.hideturtle()


def create_rectangle(bull):
    create_block.goto(bull['x'], bull['y'])
    create_block.setheading(90)
    create_block.fillcolor('red')

    create_block.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            create_block.forward(BULLET_HEIGHT)
            create_block.right(90)
        else:
            create_block.forward(BULLET_WIDTH)
            create_block.right(90)
    create_block.end_fill()


def draw_bullets(blocks, plr):
    create_block.clear()

    player_left = plr.xcor() - (plr_state['PLAYER_WIDTH'] / 2)
    player_top = plr.ycor() - (plr_state['PLAYER_HEIGHT'] / 2)

    for bull in bullets:
        if is_rect_collide(
                bull['x'],
                bull['y'],
                BULLET_WIDTH,
                BULLET_HEIGHT,
                player_left,
                player_top,
                plr_state['PLAYER_WIDTH'],
                plr_state['PLAYER_HEIGHT']
        ):
            bullets.remove(bull)
            plr_state['player_lives'] -= 1
            player_spawn(plr)
            break

        for block in reversed(blocks):
            if block['bullet_not_wall']:
                continue

            block_left = block['center_x'] - (block['width'] / 2)
            block_top = block['center_y'] - (block['height'] / 2)
            block_width = block['width']
            block_height = block['height']

            if is_rect_collide(
                    bull['x'],
                    bull['y'],
                    BULLET_WIDTH,
                    BULLET_HEIGHT,
                    block_left,
                    block_top,
                    block_width,
                    block_height
            ):
                bullets.remove(bull)
                break

        bull['velocity'] += 1
        bull['x'] += bull['velocity']

        create_rectangle(bull)


def shoot(bull, blocks, plr):
    bullets.append(bull)
    draw_bullets(blocks, plr)
