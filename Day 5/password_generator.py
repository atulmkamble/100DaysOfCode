"""
This program generates a password based on user's need. The program asks user for the number of letters, symbols,
and numbers to create the password. This password is not saved anywhere so feel free to use it.
"""

import random
from time import perf_counter
from time import process_time

# Time Tracking Start
tic1 = perf_counter()
tic2 = process_time()

# Declare variables to use choose the letters, symbols, and numbers
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Greet the user
print("Welcome to the PyPassword Generator!")

# Get the number letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Select random characters for the password
password = ''
for letter in range(nr_letters):
    password += random.choice(letters)

for symbol in range(nr_symbols):
    password += random.choice(symbols)

for symbol in range(nr_numbers):
    password += random.choice(numbers)

# Convert the password string to list. Shuffle it to randomize the sequence and convert it back to string.
password_list = list(password)
random.shuffle(password_list)
password_string = ''.join(password_list)

# # Alternate method to convert list to string:
# password_string = ''
# for char in password_list:
#     password_string += char

# Display the generated password to the user
print(f'Here is your password: {password_string}')

# Time Tracking End
toc1 = perf_counter()
toc2 = process_time()

# Print execution time
print('\nExecution Time Details:')
print(f'Total execution time including wait/sleep time: {round(toc1 - tic1, 2)}s')
print(f'Total execution time excluding wait/sleep time: {round(toc2 - tic2, 2)}s')
