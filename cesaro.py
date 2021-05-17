import turtle
from turtle import Screen
my_turtle = turtle.Turtle()
window_size = turtle.Screen()
screen = Screen()  # To open a window for the user.
user_input = screen.numinput('Select Depth',
                             'Enter a desired depth:', minval=1)


def draw_cesaro(turtle, depth, w):
    """This function takes in the turtle,draw fractal of order 2.4 and width w.
    It is cesaro torn line fractal using recursive call of the function.
    """

    if depth == 0:
        turtle.forward(w)  # Cesaro fractal of a width w.
    else:
        draw_cesaro(turtle, depth - 1, w / 2.4)
        turtle.right(80)
        draw_cesaro(turtle, depth - 1, w / 2.4)
        turtle.left(160)
        draw_cesaro(turtle, depth - 1, w / 2.4)
        turtle.right(80)
        draw_cesaro(turtle, depth - 1, w / 2.4)


def main():
    '''This is the main function. here the turtle turns 85 degrees right
    and then the turtle turns 160 degrees left and then 80 degrees
    right again as defined in the draw_cesaro function.
    It ensures that the angle on the top of the triangle
    is about 10 degrees.
    '''
    my_turtle.penup()
    my_turtle.setx(-window_size.window_width() / 2)
    my_turtle.sety(window_size.window_height() / 2 - 10)
    my_turtle.pendown()
    my_turtle.speed('fastest')  # Makes turtle fast.
    draw_cesaro(my_turtle, user_input, window_size.window_width() - 20)
    window_size.exitonclick()  # Closing the window.

if __name__ == '__main__':  # Main.
        main()
