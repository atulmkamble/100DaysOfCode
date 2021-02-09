"""
This program implements blind auction functionality.
A bidder should input his/her name and the bid amount. The subsequent bidders should follow the same process.
The program will find out the winner once all the bidders complete the process.
"""

# Import required modules
from blind_auction_art import logo
from time import perf_counter
from time import process_time

# Time Tracking Start
tic1 = perf_counter()
tic2 = process_time()

# Greet the user
print(logo)
print('Welcome to the secret auction program!')

# Initialize a list to store all the bids
secret_bids = []


def add_new_bid(bidder_name, bid_amount):
    """
    This function adds a new bid to the secret_bids list
    :param bidder_name: Name of the bidder
    :param bid_amount:  Bid amount
    :return: This function does not return anything
    """
    new_bid = {'name': bidder_name, 'bid': bid_amount}
    secret_bids.append(new_bid)


def find_highest_bidder(all_bids):
    """
    This function finds the winning bid
    :param all_bids: list which stores all the bids
    :return: This function does not return anything
    """
    winner_name = ''
    winning_bid_amount = 0
    for item in all_bids:
        if item['bid'] > winning_bid_amount:
            winning_bid_amount = item['bid']
            winner_name = item['name']
    print(f'The winner is {winner_name} with a bid of ${winning_bid_amount}')


# Initialize a variable to exit out of loop
go_again = True

# Use a loop to get all the bids
while go_again:
    name = input('What is your name?: ').casefold()
    bid = int(input('What is your bid?: $'))
    add_new_bid(bidder_name=name, bid_amount=bid)
    response = input('Are there any other bidders? Type "yes" or "no": \n').casefold()
    if response == 'no':
        go_again = False
        find_highest_bidder(all_bids=secret_bids)

# Time Tracking End
toc1 = perf_counter()
toc2 = process_time()

# Print execution time
print('\nExecution Time Details:')
print(f'Total execution time including wait/sleep time: {round(toc1 - tic1, 2)}s')
print(f'Total execution time excluding wait/sleep time: {round(toc2 - tic2, 2)}s')
