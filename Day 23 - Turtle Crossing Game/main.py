"""
This program implements a game of Turtle Crossing
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(player.move_up, 'Up')

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()

        # Detect collision with car
        for car in car_manager.all_cars:
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()

        # Check if the player has reached finish line
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.increase_speed()
            scoreboard.increase_level()

    screen.exitonclick()


if __name__ == '__main__':
    main()
