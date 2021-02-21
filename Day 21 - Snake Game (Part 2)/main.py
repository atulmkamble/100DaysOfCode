"""
This program implements the complete snake game
"""

from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def main():
    # Setup the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)

    # Create snake, food & score object and bind keys for snake movement
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkeypress(snake.up, 'Up')
    screen.onkeypress(snake.down, 'Down')
    screen.onkeypress(snake.left, 'Left')
    screen.onkeypress(snake.right, 'Right')

    # Start the game
    is_game_on = True
    while is_game_on:
        scoreboard.display_score()
        screen.update()
        sleep(0.1)
        snake.move()

        # Detect collision with the food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.update_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            is_game_on = False

        # Detect collision with tail
        for square in snake.snake_list[1:]:
            if snake.head.distance(square) < 10:
                is_game_on = False
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()
