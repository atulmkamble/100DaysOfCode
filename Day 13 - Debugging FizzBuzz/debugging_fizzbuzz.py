"""
This program implements a FizzBuzz game.
This program had multiple bugs. Fixed the bugs using debugging methodologies.
"""

# # Original Code
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


# Code After Debugging:

# Print numbers from 1 to 100
for number in range(1, 101):
    # # TODO: Remove after debugging the code'
    # print(f'Currently on number {number}')
    # If number is divisible by both 3 AND 5, so remove the 'or' and replaced it with 'and'
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # The next few conditions check the code if the number is not divisible by 3 and 5
    # Hence, these should be a part of elif
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        # We don't want the number to be a list, hence removed square brackets
        print(number)
