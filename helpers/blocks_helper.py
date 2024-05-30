import turtle


# draw image from center
def create_block(x, y, picture):
    turtle_block = turtle.Turtle()
    turtle_block.penup()
    turtle_block.goto(x, y)
    turtle_block.shape(picture)


def draw_rectangle_from_center(t, center_x, center_y, width, height, color):
    # Move turtle to the calculated top-left corner based on the center coordinates
    start_x = center_x - width / 2
    start_y = center_y + height / 2

    t.penup()  # Don't draw when moving to the start position
    t.goto(start_x, start_y)
    t.pendown()  # Start drawing
    t.fillcolor(color)
    t.begin_fill()

    # Draw the rectangle
    for _ in range(2):
        t.forward(width)  # Move forward by the width of the rectangle
        t.right(90)  # Turn right 90 degrees
        t.forward(height)  # Move forward by the height of the rectangle
        t.right(90)  # Turn right 90 degrees

    t.end_fill()  # Complete the fill of the rectangle


def create_blocks(t, blocks):
    for block in blocks:
        if block['img'] is not None:
            create_block(block['center_x'], block['center_y'], block['img'])

        if block['color'] is not None:
            draw_rectangle_from_center(
                t,
                block['center_x'],
                block['center_y'],
                block['width'],
                block['height'],
                block['color'],
            )
