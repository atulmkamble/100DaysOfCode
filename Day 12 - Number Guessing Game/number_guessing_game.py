"""
This program implements a guessing game. User has to choose a level (easy/hard) and get some guesses.
In those assigned guesses, user has to guess the number that the computer has randomly generated from 1 to 100.
"""

from random import randint
from number_guessing_game_art import logo
from time import perf_counter
from time import process_time

# Set global constants for level based guesses
EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = 5


def get_number():
    """
    Generates random number between 1 and 100
    :return: random number between 1 and 100
    """

    return randint(1, 100)


def get_difficulty():
    """
    Gets difficulty level from user and sets the number of guesses accordingly
    :return: number of guesses as per the selected level
    """

    difficulty = input('Choose a difficulty. Type "easy" or "hard": ').casefold()
    if difficulty == 'easy':
        return EASY_LEVEL_GUESSES
    elif difficulty == 'hard':
        return HARD_LEVEL_GUESSES
    else:
        print('Invalid input. You lose.')
        return 0


def guessing_game():
    """
    Generates random number and checks the user guesses corresponding to it
    :return: nothing
    """

    # Greet the user with game logo
    print(logo)
    print('Welcome to the Number Guessing Game!')

    # Generate a random number to guess
    computer_number = get_number()
    print('I have chosen a number between 1 and 100.')

    # Initialize a variable to track the end of game
    is_game_over = False

    guesses = get_difficulty()

    # If user has entered invalid input for difficulty level, end the game
    if guesses == 0:
        is_game_over = True

    # Until the game is not over, get the user guess and compare it with computer generated number
    while not is_game_over:
        print(f'You have {guesses} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))

        if guess == computer_number:
            print(f'You got it! You won. The number was {computer_number}.')
            # If the user wins, end the game
            is_game_over = True
        elif guess < computer_number:
            print(f'You guessed low. Guess higher.')
        else:
            print(f'You guessed high. Guess lower.')

        # Reduce the number of guesses for each new guess
        guesses -= 1

        # End the game if guesses become 0
        if guesses == 0:
            print(f'The number of guesses are exhausted. You lose. The number was {computer_number}.')
            is_game_over = True


def main():
    # Time Tracking Start
    tic1 = perf_counter()
    tic2 = process_time()

    # Start the game
    guessing_game()

    # Time Tracking End
    toc1 = perf_counter()
    toc2 = process_time()

    # Print execution time
    print('\nExecution Time Details:')
    print(f'Total execution time including wait/sleep time: {round(toc1 - tic1, 2)}s')
    print(f'Total execution time excluding wait/sleep time: {round(toc2 - tic2, 2)}s')


if __name__ == '__main__':
    main()
