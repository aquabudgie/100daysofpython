from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True
while is_on:
    order = input(f"What would you like? {menu.get_items()}: ").lower()
    if order == "report":
        coffeemaker.report()
        moneymachine.report()
    elif order == "off":
        is_on = False
        print("Machine shutting down.")
    else:
        drink = menu.find_drink(order)
        if drink == None:
            continue
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
