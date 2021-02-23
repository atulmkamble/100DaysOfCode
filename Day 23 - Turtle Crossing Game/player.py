"""
This file implements the Player class
"""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        """
        Moves the player upwards in the game
        :return: nothing
        """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """
        Reset the position of player after leveling up
        :return: nothing
        """
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """
        Checks if the player is at finish line
        :return: nothing
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
