"""
This file implements the code to create Hirst's dot painting
"""

from turtle import Turtle, colormode, Screen
from random import choice

# Initialize a color palette extracted from Hirst's dot painting
COLORS_LIST = [
    (131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157),
    (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55),
    (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110),
    (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)
]


def draw_painting(tim):
    """
    Draws dots in the painting by choosing the color from color palette randomly
    :param tim: Turtle object
    :return: nothing
    """

    # Get 10 dots in a row
    for _ in range(10):
        tim.pendown()
        tim.dot(20, choice(COLORS_LIST))
        tim.penup()
        tim.forward(50)

    # Move to the row above and first position
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


def main():
    # Set the colormode to use rgb colors
    colormode(255)

    # Initialize the object
    tim = Turtle()

    # Set the speed to fastest to plot the dots quicker
    tim.speed('fastest')

    # Hide the turtle while drawing
    tim.hideturtle()

    # Don't draw at the beginning while setting the initial position
    tim.penup()

    # Set initial position
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)

    # Plot 10 dots in 10 rows
    for _ in range(10):
        draw_painting(tim)

    # Pause to show the dots until user click on the screen
    screen = Screen()
    screen.exitonclick()


if __name__ == '__main__':
    main()
