from welcome_screen import display_welcome_screen
from name_selection_screen import display_name_selection


def main():
    play_button_clicked = display_welcome_screen()
    if not play_button_clicked:
        return

    continue_button_clicked, player1_name, player2_name = display_name_selection()
    if not continue_button_clicked:
        return

    print(f'player1_name = {player1_name}')
    print(f'player2_name = {player2_name}')


if __name__ == '__main__':
    main()
