"""
This file implements the Ball class
"""

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """
        Moves the ball
        :return:
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Bounces the ball based on y axis
        :return: nothing
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Bounces the ball based on x axis
        :return: nothing
        """
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """
        Resets the ball position post scoring a point
        :return: nothing
        """
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
