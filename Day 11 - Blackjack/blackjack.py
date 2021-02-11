"""
This program implements a game of blackjack.
"""

from random import choice
from blackjack_art import logo
from time import perf_counter
from time import process_time

def get_card():
    """
    Returns a random card from the deck
    :return: random card
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def get_score(cards):
    """
    Get the score by adding up all the items in a list
    :param cards: cards list
    :return: score
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def get_winner(user_score, dealer_score):
    """
    Compares the user's and dealer's cards to find out a winner
    :param user_score: sum of all the user's cards
    :param dealer_score: sum of all the dealer's cards
    :return: winner with the lowest score
    """
    if user_score == dealer_score:
        print('Draw')
    elif dealer_score == 0:
        print('You lose, dealer has Blackjack')
    elif user_score == 0:
        print('You win with a Blackjack')
    elif user_score > 21:
        print('You went over. You lose')
    elif dealer_score > 21:
        print('Dealer went over. You win')
    elif user_score > dealer_score:
        print('You win')
    else:
        print('You lose')


def play_game():
    """
    Executes the game logic
    :return: nothing
    """
    user_cards = []
    dealer_cards = []
    is_game_over = False

    # Gets the first two cards for the user and dealer
    for _ in range(2):
        user_cards.append(get_card())
        dealer_cards.append(get_card())

    # Loop until the score is over 21 or Blackjack
    while not is_game_over:
        user_score = get_score(user_cards)
        dealer_score = get_score(dealer_cards)
        print(f'\tYour cards {user_cards}, current score: {user_score}')
        print(f'\tDealer\'s first card: {dealer_cards[0]}')

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input('Type "y" to get another card, type "n" to pass: ').casefold()
            if another_card == 'y':
                user_cards.append(get_card())
            else:
                is_game_over = True

    # Get dealer cards after the user's turn
    # If the dealer's score is less than 17, the program will get cards until is it greater than or equal to 17
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(get_card())
        dealer_score = get_score(dealer_cards)

    # Display the final results
    print(f'\tYour final hand {user_cards}, final score: {user_score}')
    print(f'\tDealer\'s final hand: {dealer_cards}, final score: {dealer_score}')
    get_winner(user_score, dealer_score)


def main():
    # If user wan't to play the game, greet the user with game logo and start the game
    while input('\nDo you want to play a game of Blackjack? Type "y" or "n": ').casefold() == 'y':
        print(logo)
        play_game()


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
