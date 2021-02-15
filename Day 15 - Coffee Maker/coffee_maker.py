"""
This program implements a coffee maker machine
"""

from coffee_data import MENU, resources
from coffee_art import logo


def check_resources(coffee_type):
    """
    Check if there are sufficient resources in the coffee maker machine to make a coffee
    :param coffee_type: type selected by user
    :return: True (if resources are sufficient) or False
    """

    if coffee_type == 'espresso' or coffee_type == 'latte' or coffee_type == 'cappuccino':
        if resources['water'] < MENU[coffee_type]['ingredients']['water']:
            print('Sorry there is not enough water')
            return False
        elif resources['coffee'] < MENU[coffee_type]['ingredients']['coffee']:
            print('Sorry there is not enough coffee')
            return False
        elif coffee_type == 'latte' or coffee_type == 'cappuccino':
            # Handles the espresso case since it does not have milk
            if resources['milk'] < MENU[coffee_type]['ingredients']['milk']:
                print('Sorry there is not enough milk')
                return False
            else:
                # print('Enough resources')
                return True
        else:
            # print('Enough resources')
            return True
    else:
        print('Invalid coffee selection')
        return False


def process_coins():
    """
    Processes the coins entered by user in the coffee machine
    :return: The amount entered by the user in the coffee machine
    """

    print('Please insert coins')
    coins_quarters = int(input('How many quarters: '))
    coins_dimes = int(input('How many dimes: '))
    coins_nickles = int(input('How many nickles: '))
    coins_pennies = int(input('How many pennies: '))
    input_money = 0.25 * coins_quarters + 0.10 * coins_dimes + 0.05 * coins_nickles + 0.01 * coins_pennies
    return input_money


def make_coffee(input_money, coffee_type):
    """
    If the amount is sufficient for the coffee, provides the coffee and updates the resources
    :param input_money: The money provided by the user into coffee machine
    :param coffee_type: The type of coffee that user wants
    :return: Cost of the coffee
    """

    # The money is sufficient
    if input_money >= MENU[coffee_type]['cost']:
        change = round(input_money - MENU[coffee_type]['cost'], 2)
        if change != 0:
            # If there is some change, print it
            print(f'Here is ${change} in change.')
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
        if coffee_type == 'latte' or coffee_type == 'cappuccino':
            # Handles the case for espresso
            resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        print(f'Here is your {coffee_type} ☕. Enjoy!')
        return MENU[coffee_type]['cost']
    else:
        print('Sorry, that is not enough money. Money refunded.')


def get_report(total_money):
    """
    Gets the resources update
    :param total_money: Total money in the coffee maker
    :return: nothing
    """

    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${total_money}")


def coffee_maker():
    """
    Implements coffee maker functionality
    :return: nothing
    """

    turn_off_machine = False
    total_money = 0

    while not turn_off_machine:
        print(logo)
        print('\nNote: Type "off" to turn of the coffee machine and "report" to get resources update')
        coffee_type = input('What would you like? (espresso/latte/cappuccino): ').casefold()
        if coffee_type == 'off':
            turn_off_machine = True
        elif coffee_type == 'report':
            get_report(total_money)
        else:
            is_enough_resources = check_resources(coffee_type)
            if is_enough_resources:
                input_money = process_coins()
                coffee_price = make_coffee(input_money, coffee_type)
                if coffee_price is not None:
                    # If returned coffee price is not None, add the coffee price to total money
                    total_money += coffee_price


def main():
    # Calls the coffee maker function
    coffee_maker()


if __name__ == '__main__':
    main()
