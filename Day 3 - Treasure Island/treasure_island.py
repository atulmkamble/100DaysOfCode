"""
This program takes user's input as per the conditions in the game.
Follow the instructions and choose wisely to win the game else it's Game Over!
"""

from time import perf_counter
from time import process_time

# Time Tracking Start
tic1 = perf_counter()
tic2 = process_time()

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print('Welcome to Treasure Island. The Treasure awaits YOU.')
print("Your mission is to find the treasure. Can you find it? Let's check it out!!!")

# Present scenario 1 and get the user's input
tunnel = input(
    'You are in a tunnel. There are two ways inside it. Where do you want to go? Type "left" or "right"\n').casefold()
# Direct the user as per the input
if tunnel == 'left':
    # Present scenario 2 and get the user's input
    lake = input(
        'There is a lake inside the tunnel with an island in the middle of it. Type "wait" to wait for the boat. Type '
        '"swim" to swim across it\n').casefold()
    # Direct the user as per the input
    if lake == 'wait':
        # Present scenario 2 and get the user's input
        box = input(
            'You arrive on the island. There are three boxes in front of you. One red, one yellow and one blue. Which '
            'box do you choose?\n').casefold()
        # Direct the user as per the input
        if box == 'red':
            print('You die out of an explosion. Game Over!')
        elif box == 'yellow':
            print('You found the treasure; You won! Congratulations!')
        else:
            print('You die by smelling poisonous gas in the box. Game Over!')
    else:
        print('You are eaten by a shark. Game Over!')
else:
    print('You are eaten by a bear. Game Over!')

# Time Tracking End
toc1 = perf_counter()
toc2 = process_time()

print('\nExecution Time Details:')
print(f'Total execution time including wait/sleep time: {round(toc1 - tic1, 2)}s')
print(f'Total execution time excluding wait/sleep time: {round(toc2 - tic2, 2)}s')
