from random import randint


def pick_random_color():
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    print(f"r:{r}, g:{g}, b:{b}")
    return r, g, b
