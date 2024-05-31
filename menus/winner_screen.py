import turtle


def display_winner_screen(winner):
    turtle.TurtleScreen._RUNNING = True
    turtle.color("yellow")
    winner_screen = turtle.Screen()
    winner_screen.bgcolor("black")
    winner_screen.setup(width=1.0, height=1.0)

    print("winner:", winner)
    turtle.write(f"{winner} won!", align="center", font=("Impact", 70))
    turtle.hideturtle()

    winner_screen.mainloop()
