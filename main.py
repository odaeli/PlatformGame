from game import start_game
from menus.name_selection_screen import display_name_selection
from menus.welcome_screen import display_welcome_screen


def main():
    play_button_clicked = display_welcome_screen()
    if not play_button_clicked:
        return

    continue_button_clicked, player1_name, player2_name = display_name_selection()
    if not continue_button_clicked:
        return

    print(f'player1_name = {player1_name}')
    print(f'player2_name = {player2_name}')

    winner = start_game()
    if not winner:
        return

    print(f'winner = {winner}')

    # TODO add winner screen


if __name__ == '__main__':
    main()
