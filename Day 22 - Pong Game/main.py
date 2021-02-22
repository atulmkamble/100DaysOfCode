"""
This program implements a game of Pong
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep


def main():
    print('For controlling the paddle, the right player uses "Up" and "Down" arrow keys while the left player uses '
          '"w" and "s" keys')

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title('Pong Game')
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(r_paddle.up, 'Up')
    screen.onkeypress(r_paddle.down, 'Down')
    screen.onkeypress(l_paddle.up, 'w')
    screen.onkeypress(l_paddle.down, 's')

    is_game_on = True
    while is_game_on:
        screen.update()
        sleep(ball.ball_speed)
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddles
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
                ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Detect Right paddle miss
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Detect Left paddle miss
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

    screen.exitonclick()


if __name__ == '__main__':
    main()
