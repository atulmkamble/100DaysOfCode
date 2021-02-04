"""
This program is a game of rock, paper and scissors. You and the program compete in this game to emerge as a
winner. The program is not aware of your choice and it's a fair game. Please follow the directions in the program.
"""

from random import randint
from time import perf_counter
from time import process_time

# Time Tracking Start
tic1 = perf_counter()
tic2 = process_time()

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Define a list with ASCII images of rock, paper, and scissors
game_options = [rock, paper, scissors]

# Display a welcome message and get the player choice
print('Welcome to Rock Paper Scissors!\nLet us see if you can beat the program and emerge as a winner. Let\'s Go!!!\n')
player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

# Handle invalid inputs and compare the choices to determine the winner
if 0 <= player_choice <= 2:
    print(game_options[player_choice])
    program_choice = randint(0, 2)
    print('Computer chose:')
    print(game_options[program_choice])
    if player_choice == program_choice:
        print('Result: It\'s a Draw!')
    # Considered only player win scenarios
    elif (player_choice == 0 and program_choice == 2) or (player_choice == 2 and program_choice == 1) or (
            player_choice == 1 and program_choice == 0):
        print('Result: You Won!')
    else:
        print('Result: You Lose!')
else:
    print('Invalid choice! You Lose!')

# Time Tracking End
toc1 = perf_counter()
toc2 = process_time()

# Print execution time
print('\nExecution Time Details:')
print(f'Total execution time including wait/sleep time: {round(toc1 - tic1, 2)}s')
print(f'Total execution time excluding wait/sleep time: {round(toc2 - tic2, 2)}s')
