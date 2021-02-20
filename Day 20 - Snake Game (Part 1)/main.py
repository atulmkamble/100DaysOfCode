"""
This program implements the part 1 of the snake game
"""

from turtle import Turtle, Screen
from time import sleep
from snake import Snake


def main():
    # Setup the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)

    # Create snake object and bind keys for snake movement
    snake = Snake()
    screen.listen()
    screen.onkeypress(snake.up, 'Up')
    screen.onkeypress(snake.down, 'Down')
    screen.onkeypress(snake.left, 'Left')
    screen.onkeypress(snake.right, 'Right')

    # Start the game
    is_game_on = True
    while is_game_on:
        screen.update()
        sleep(0.1)
        snake.move()

    screen.exitonclick()


if __name__ == '__main__':
    main()
