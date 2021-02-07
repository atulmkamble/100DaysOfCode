"""
This program is a hangman game. Guess the name chosen by program before you run out of lives.
Please refer to the link below to know more about the game:
https://en.wikipedia.org/wiki/Hangman_(game)
"""

# Import the required modules
from random import choice
from hangman_art import stages, logo
from hangman_words import word_list
from time import perf_counter
from time import process_time

# Time Tracking Start
tic1 = perf_counter()
tic2 = process_time()

# Greet the user with game logo
print(logo)

# Choose a word randomly
chosen_word = choice(word_list)
# # See the chosen word for debugging purposes
# print(f'The chosen word is: {chosen_word}')

# Initialize a variable to track the wrong guesses
end_of_game = False
lives = 6

# Initialize a list for blanks equal to the chosen word length
display = []
for _ in range(len(chosen_word)):
    display.append('_')

while not end_of_game:
    guess = input('Please enter your guess alphabet:\n').casefold()

    # Check if the guess is already made for an alphabet (present in the chosen word) and let the user know about it
    if guess in display:
        print('You have already guessed this alphabet!')

    # Check the guessed alphabet and update it in the list if the guess is correct
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess

    # Let the user know about incorrect guess and end the game when the number of lives are exhausted
    if guess not in chosen_word:
        lives -= 1
        print(f'The alphabet {guess} is not in the chosen word. You lose a life! Lives Remaining: {lives}')
        if lives == 0:
            end_of_game = True
            print('You lose.')

    # If all the alphabets are guessed correctly, end the game
    if '_' not in display:
        end_of_game = True
        print('You win.')

    # Print the guessed word at each iteration
    print('Guessed Word:', ' '.join(display))

    # Print the ASCII hangman art as per the number of lives remaining
    print(stages[lives])

# Time Tracking End
toc1 = perf_counter()
toc2 = process_time()

# Print execution time
print('\nExecution Time Details:')
print(f'Total execution time including wait/sleep time: {round(toc1 - tic1, 2)}s')
print(f'Total execution time excluding wait/sleep time: {round(toc2 - tic2, 2)}s')
