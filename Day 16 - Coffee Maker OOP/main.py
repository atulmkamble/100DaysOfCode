"""
This program implements a coffee maker machine in Object Oriented Programming (OOP) style
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from coffee_art import logo

# Create class objects
menu = Menu()
maker = CoffeeMaker()
machine = MoneyMachine()

# Initialize a variable to turn off the coffee machine
turn_off_machine = False

while not turn_off_machine:
    # Greet the user with logo
    print(logo)

    print('\nNote: Type "off" to turn of the coffee machine and "report" to get resources update')
    drink_name = input(f'What would you like? ({menu.get_items()}): ').casefold()
    if drink_name == 'off':
        turn_off_machine = True
    elif drink_name == 'report':
        maker.report()
        machine.report()
    else:
        drink = menu.find_drink(drink_name)
        if drink:
            can_make_drink = maker.is_resource_sufficient(drink)
            is_enough_money = machine.make_payment(drink.cost)
            if can_make_drink and is_enough_money:
                maker.make_coffee(drink)
