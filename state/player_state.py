from state.game_state import (CLOUD_HEIGHT, FLOOR_HEIGHT,
                              LEFT_SCREEN_WALL_WIDTH, LEFT_SCREEN_WALL_X,
                              SCREEN_HEIGHT, SCREEN_WIDTH)

plr_state = {
    'player_lives': 3,
    'PLAYER_WIDTH': 63,
    'PLAYER_HEIGHT': 59,
    'keys_collected': 0,
    'door_unlocked': 0,
}

PLAYER_SPAWN_POINT = {
    'center_x': -SCREEN_WIDTH / 2
    + LEFT_SCREEN_WALL_X
    + plr_state['PLAYER_WIDTH'] / 2
    + LEFT_SCREEN_WALL_WIDTH,
    'center_y': -SCREEN_HEIGHT / 2
    + plr_state['PLAYER_HEIGHT'] / 2
    + CLOUD_HEIGHT
    + FLOOR_HEIGHT,
}
