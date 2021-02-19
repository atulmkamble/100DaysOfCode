"""
This program implements a Turtle Race. Place your bet on a turtle and tune on to see who wins.
"""

# Import required modules
from turtle import Turtle, Screen
from random import randint
from turtle_race_art import logo


def main():
    """
    Creates turtles and puts them up for the race
    :return: nothing
    """

    # Greet the user with logo
    print(logo)

    # Initialize the required variables
    colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
    all_turtles = []
    is_game_on = True

    # Setup the screen
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title='Make your bet',
                                prompt='Which turtle will win the race? Enter a color (purple, blue, green, yellow, '
                                       'orange, red): ').casefold()
    # Set the y axis position of turtles
    y = -100

    for t in range(len(colors)):
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(colors[t])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y)
        all_turtles.append(new_turtle)
        y += 40

    # If the user has entered the bet, start the race
    if user_bet:
        while is_game_on:
            for turt in all_turtles:
                # If the turtle is at finish line
                if turt.xcor() >= 220:
                    is_game_on = False
                    winner = turt.pencolor()
                    if user_bet == winner:
                        print(f'You won! The {winner} turtle is the winner.')
                    else:
                        print(f'You lost! The {winner} turtle is the winner.')
                    break
                else:
                    turt.forward(randint(1, 10))
        screen.exitonclick()
    else:
        print('You have not placed your bet!')


if __name__ == '__main__':
    main()
