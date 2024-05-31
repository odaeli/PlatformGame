from game import start_game
from menus.name_selection_screen import display_name_selection
from menus.welcome_screen import display_welcome_screen
from menus.winner_screen import display_winner_screen


def main():
    play_button_clicked = display_welcome_screen()
    if not play_button_clicked:
        return

    continue_button_clicked, good_player_name, evil_player_name = display_name_selection()
    if not continue_button_clicked:
        return

    print(f'good_player_name = {good_player_name}')
    print(f'evil_player_name = {evil_player_name}')

    winner = start_game()
    if not winner:
        return

    print(f'winner = {winner}')

    if winner == 'good':
        display_winner_screen(good_player_name)
    else:
        display_winner_screen(evil_player_name)


if __name__ == '__main__':
    main()
