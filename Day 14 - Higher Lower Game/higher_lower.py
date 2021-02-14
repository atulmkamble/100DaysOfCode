"""
This program implements a game of higher lower
"""

from higher_lower_game_data import data
from random import choice
from higher_lower_art import logo, vs
from time import perf_counter
from time import process_time


def format_account(account):
    """
    Returns the formatted data of an account
    :param account: randomly selected account
    :return: returns the formatted data of input account
    """
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_desc}, from {account_country}'


def check_answer(guess, a_followers, b_followers):
    """
    Check the user guess to the actual followers of an account to verify if user's guess is correct
    :param guess: user's guess
    :param a_followers: number of followers of account a
    :param b_followers: number of followers of account b
    :return: if the user's guess is correct
    """
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def main():
    """
    implements game functionality
    :return: nothing
    """
    # Greet the user with game logo
    print(logo)

    # Initialize a variable to track the game score
    score = 0

    # Initialize a variable to repeat the game
    go_again = True

    # Create a random account. This will be assigned to account_a to make the code repeatable
    account_b = choice(data)

    while go_again:
        # Assign the value outside the loop to this variable
        account_a = account_b

        # Create a new value for account b
        account_b = choice(data)

        # Eliminate same entries for both the accounts
        while account_a == account_b:
            account_b = choice(data)

        # Print the account outputs
        print(f'Compare A: {format_account(account_a)}.')
        print(vs)
        print(f'Against B: {format_account(account_b)}.')

        # Take the user's guess and compare with the actual answer based on followers
        guess = input('Who has more followers? Type "A" or "B": ').casefold()
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            # If the guess is correct, increase the score
            score += 1
            print(f'You are right! Current score: {score}')
        else:
            # If the guess is wrong, end the game
            go_again = False
            print(f'Sorry, that is wrong. Final score: {score}')


if __name__ == '__main__':
    # Time Tracking Start
    tic1 = perf_counter()
    tic2 = process_time()

    # Call the main function
    main()

    # Time Tracking End
    toc1 = perf_counter()
    toc2 = process_time()

    # Print execution time
    print('\nExecution Time Details:')
    print(f'Total execution time including wait/sleep time: {round(toc1 - tic1, 2)}s')
    print(f'Total execution time excluding wait/sleep time: {round(toc2 - tic2, 2)}s')
