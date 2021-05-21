from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create Objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_coffee_machine_on = True
while is_coffee_machine_on:
    # Use the menu object method to get the selection of coffee available
    options = menu.get_items()
    user_choice = input(f'What Would You Like? {options}: ')

    if user_choice == 'off':
        is_coffee_machine_on = False
    elif user_choice == 'report':
        # Use the methods available to the objects to generate a report.
        coffee_maker.report()
        money_machine.report()
    else:
        # Use the menu object to make sure the drink the user chose exist.
        drink = menu.find_drink(user_choice)

        # Use the coffee maker object to check if resources are sufficient and money machine object to take payment.
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
