"""
This program encodes/decodes text given to it as an input.
It takes three arguments as an input:
1. Action: Encode/Decode
1. Text to be encoded/decoded
2. Shift value (The value by which the alphabets will be shifted)
"""

from caesar_art import logo
from time import perf_counter
from time import process_time

# Time Tracking Start
tic1 = perf_counter()
tic2 = process_time()

# Print the caesar cipher logo
print(logo)

# Initialize alphabets list. The letter sequence is included twice in order to include the shift amount greater than
# alphabet 'z'
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(action, input_text, shift_amount):
    """
    This function encodes/decodes the text
    :param action: Encode/Decode value
    :param input_text: The text that will be encoded/decoded
    :param shift_amount: The amount by which the alphabets will be shifted
    :return: This function does not return a value but prints the transformed string
    """

    transformed_text = ''

    # If the action is decode, make the shift_amount as negative
    if action == 'decode':
        shift_amount *= -1

    # Add/Subtract the shift value to get the index from alphabets list
    for alphabet in input_text:
        if alphabet in alphabets:
            index = alphabets.index(alphabet)
            new_index = index + shift_amount
            new_alphabet = alphabets[new_index]
            transformed_text += new_alphabet
        else:
            transformed_text += alphabet

    # Print the result
    print(f'The {action}d text is {transformed_text}')


# Initialize a variable to end the program
go_again = True

# Check if the user wants to run the program again and get the inputs accordingly
while go_again:
    enc_dec = input('Type "encode" to encrypt, type "decode" to decrypt:\n').casefold()
    text = input('Type your message:\n').casefold()
    shift = int(input('Type the shift number:\n'))
    caesar(action=enc_dec, input_text=text, shift_amount=shift)
    response = input('If you want to go again, type "yes" otherwise type "no":\n').casefold()

    # Exit the program if user does not want to continue
    if response == 'no':
        go_again = False
        print('Thank you for using this program.')

# Time Tracking End
toc1 = perf_counter()
toc2 = process_time()

# Print execution time
print('\nExecution Time Details:')
print(f'Total execution time including wait/sleep time: {round(toc1 - tic1, 2)}s')
print(f'Total execution time excluding wait/sleep time: {round(toc2 - tic2, 2)}s')
