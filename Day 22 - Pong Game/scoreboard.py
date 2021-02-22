"""
This file implements the Scoreboard class
"""

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 50, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_point(self):
        """
        Increases the point of the left player
        :return: nothing
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increases the point of the right player
        :return: nothing
        """
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard and displays it on screen
        :return:
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
