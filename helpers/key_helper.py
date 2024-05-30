from helpers.blocks_helper import create_blocks
from helpers.movement_helper import is_rect_collide
from state.player_state import plr_state
import turtle

keys_creator = turtle.Turtle()


def create_key(keys):
    for key in keys:
        if key['is_blank']:
            pass

        keys_creator.penup()
        keys_creator.goto(key['center_x'], key['center_y'])
        keys_creator.shape('images/key.gif')


def key_collision(plr, keys):
    for key in keys:
        if key['is_blank'] != True:
            key_left = key['center_x'] - (key['width'] / 2)
            key_top = key['center_y'] - (key['height'] / 2)
            key_width = key['width']
            key_height = key['height']

            player_left = plr.xcor() - (plr_state['PLAYER_WIDTH'] / 2)
            player_top = plr.ycor() - (plr_state['PLAYER_HEIGHT'] / 2)

            if is_rect_collide(
                    key_left,
                    key_top,
                    key_width,
                    key_height,
                    player_left,
                    player_top,
                    plr_state['PLAYER_WIDTH'],
                    plr_state['PLAYER_HEIGHT']
            ):
                keys_creator.shape('blank')
                key['is_blank'] = True
                plr_state['keys_collected'] += 1
                break
