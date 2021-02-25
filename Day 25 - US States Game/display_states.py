"""
This file implements the DisplayStates class
"""

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 8, 'normal')


class DisplayStates(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def mark_state(self, x, y, state_name):
        self.goto(x, y)
        self.write(f'{state_name}', align=ALIGNMENT, font=FONT)
