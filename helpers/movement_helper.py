from state.player_state import plr_state, PLAYER_SPAWN_POINT


def player_spawn(plr):
    plr.goto(PLAYER_SPAWN_POINT['center_x'], PLAYER_SPAWN_POINT['center_y'])


def is_rect_collide(x1, y1, w1, h1, x2, y2, w2, h2):
    return ((x1 <= x2 + w2) and
            (x1 + w1 >= x2) and
            (y1 <= y2 + h2) and
            y1 + h1 >= y2)


def move(movement, blocks, plr, game_props):
    is_collide = False
    for block in blocks:
        block_left = block['center_x'] - (block['width'] / 2)
        block_top = block['center_y'] - (block['height'] / 2)
        block_width = block['width']
        block_height = block['height']

        player_left = movement['center_x'] + movement['dx'] - (plr_state['PLAYER_WIDTH'] / 2)
        player_top = movement['center_y'] + movement['dy'] - (plr_state['PLAYER_HEIGHT'] / 2)

        if is_rect_collide(
                block_left,
                block_top,
                block_width,
                block_height,

                player_left,
                player_top,
                plr_state['PLAYER_WIDTH'],
                plr_state['PLAYER_HEIGHT']
        ):
            is_collide = True

            if block['bad_block']:
                plr_state['player_lives'] -= 1
                player_spawn(plr)

            if block['exit_block'] and plr_state['door_unlocked']:
                game_props['IsEnd'] = True
            break

    if not is_collide:
        plr.setx(movement['center_x'] + movement['dx'])
        plr.sety(movement['center_y'] + movement['dy'])

    return is_collide
