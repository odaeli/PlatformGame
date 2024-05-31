import turtle
from tkinter import *
from turtle import Screen

from helpers.utils import pick_random_color

play_button_clicked = False


def change_title_color(x, y):
    new_text_color = pick_random_color()
    turtle.color(new_text_color)
    turtle.write("PLATFORM GAME", align="center", font=("Impact", 70))


def handle_play_button():
    global play_button_clicked
    print("start game")
    play_button_clicked = True
    turtle.bye()


def display_welcome_screen():
    welcome_screen = Screen()
    welcome_screen.bgcolor("black")
    welcome_screen.setup(width=1.0, height=1.0)

    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()

    turtle.colormode(255)

    change_title_color(0, 0)
    welcome_screen.onclick(change_title_color)

    turtle.hideturtle()

    canvas = welcome_screen.getcanvas()
    button = Button(
        canvas.master,
        text="PLAY",
        command=handle_play_button,
        font=("Ariel", 30),
        bg="white",
    )

    button.pack()
    button.place(relx=0.5, rely=0.5, anchor="center")

    welcome_screen.mainloop()

    return play_button_clicked
