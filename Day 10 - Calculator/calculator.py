"""
This program implements the classic calculator functionality (Addition, Subtraction, Multiplication & Division)
"""

from calculator_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    """
    This function get the numbers from user and operate on them recursively
    :return: returns nothing
    """

    # Greet the user
    print(logo)
    print('Note: You can close the program/window to exit')
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    # Get the first number
    num1 = float(input('What\'s the first number?: '))

    # Print the operations
    for key in operations:
        print(key)

    # Initialize a variable to start a new calculation
    go_again = True
    while go_again:
        # Get the operation and second number
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What\'s the next number?: '))

        # Call the respective function as per the input operation
        answer = operations[operation_symbol](num1, num2)

        # Print the output
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        # Get a response to start a new calculation or continue with the current answer
        response = input(
            f'Type "y" to continue calculating with {answer} or type "n" start a new calculation: ').casefold()
        if response == 'n':
            go_again = False
            # Use recursion
            calculator()
        elif response == 'y':
            num1 = answer


# Execute the calculator function
calculator()
