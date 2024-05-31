import turtle

from helpers.utils import pick_random_color


def change_text_color(text='', x=None, y=None):
    new_text_color = pick_random_color()
    turtle.color(new_text_color)
    turtle.write(text, align="center", font=("Impact", 70))


def display_winner_screen(winner_name):
    turtle.TurtleScreen._RUNNING = True
    winner_screen = turtle.Screen()
    winner_screen.bgcolor("black")
    winner_screen.setup(width=1.0, height=1.0)

    turtle.colormode(255)

    text_to_show = f"{winner_name} won!"
    change_text_color(text_to_show)
    winner_screen.onclick(lambda x, y: change_text_color(text_to_show, x, y))

    print("winner:", winner_name)
    turtle.hideturtle()

    winner_screen.mainloop()
