import turtle
from time import sleep

from helpers.utils import pick_random_color

winner_screen = None


def change_text_color(text='', x=None, y=None, sleep_time=0):
    if sleep_time > 0:
        sleep(sleep_time)
    new_text_color = pick_random_color()
    turtle.color(new_text_color)
    turtle.write(text, align="center", font=("Impact", 70))
    winner_screen.ontimer(change_text_color(text, x, y, 0.5))


def display_winner_screen(winner_name):
    global winner_screen
    turtle.TurtleScreen._RUNNING = True
    winner_screen = turtle.Screen()
    winner_screen.bgcolor("black")
    winner_screen.setup(width=1.0, height=1.0)

    turtle.colormode(255)
    turtle.hideturtle()

    text_to_show = f"{winner_name} won!"
    change_text_color(text_to_show)

    print("winner:", winner_name)
    turtle.hideturtle()

    winner_screen.mainloop()
