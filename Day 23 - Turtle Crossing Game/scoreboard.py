"""
This file implements the Scoreboard class
"""

from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 250)
        self.update_scoreboard()

    def increase_level(self):
        """
        Increases and displays the level
        :return: nothing
        """
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard
        :return: nothing
        """
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def game_over(self):
        """
        Displays the GAME OVER text, in case the player collides with any of the cars
        :return: nothing
        """
        self.goto(0, 0)
        self.write(f'GAME OVER', align='CENTER', font=FONT)
