MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}


coffees = ("espresso", "latte", "cappuccino")


# 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
def take_order():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order not in coffees:
        if order in actions:
            actions[order]()
            order = take_order()
        else:
            print("Please enter one of the available options")
            order = take_order()
    return order


# 2. Turn off the coffee machine by entering "Off" to the prompt
def off():
    print("Machine powering off.")
    exit()


# 3. Print report of all coffee machine resources
def report():
    """E.g. Water: 100ml, Milk: 50ml Coffee: 76g Money: $2.5"""
    template = f"""Water: {resources['water']}
Milk: {resources['milk']}
Coffee: {resources['coffee']}
Money: {money['value']}
"""
    print(template)
    return


#  4. Check resources are sufficient
def check_resources(order):
    """E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: "Sorry there is not enough water."""
    required_resources = MENU[order]["ingredients"]
    resource_names = required_resources.keys()
    sufficient_resources = True
    # subtract resources for drink from resources
    for name in resource_names:
        sufficient_resources = resources[name] >= required_resources[name]
        # evaluate if any of the resources becomes negative
        if not sufficient_resources:
            # Print missing resource
            print(f"Sorry, there is not enough {name}.")
            sufficient_resources = False
            break
    return sufficient_resources, required_resources


# 5. Process coins
def process_coins(order):
    """If sufficient resources, prompt user to to insert coins, quarter = 0.25, dime 0.10, nickles = 0.05, pennies = 0.01.
    also include price of their coffee"""
    value = 0
    cost = MENU[order]["cost"]
    print(f"A {order} costs ${cost}, please insert coins")
    coins = {}
    coins["quarters"] = {"count": int(input("How many quarters?: ")), "value": 0.25}
    coins["dimes"] = {"count": int(input("How many dimes?: ")), "value": 0.10}
    coins["nickles"] = {"count": int(input("How many nickles?: ")), "value": 0.05}
    coins["nickles"] = {"count": int(input("How many nickles?: ")), "value": 0.01}

    for key in coins:
        value += coins[key]["count"] * coins[key]["value"]
    return cost, value


# todo: 6. check transaction successful,
def check_transaction(cost, value):
    """check if user inserted enough money 'sorry that's not enough money. money refunded.' if sufficient, add cost of drink to profit as a resource. if the user has inserted too much money, offer change"""
    if value > cost:
        successful = True
        print(f"here is your change ${round(value - cost, 2)}")
    elif value == cost:
        successful = True
    else:
        print(f"insufficient coins inserted, here is your refund of ${round(value, 2)}")
        successful = False
    return successful


def add_money(cost):
    money["value"] += cost


# todo: 7. make a coffee
def make_coffee(order, required_resources):
    """if transaction successful, deduct sufficicient resources and tell user 'here is your {coffee}. enjoy!'"""
    resource_names = required_resources.keys()
    for name in resource_names:
        resources[name] -= required_resources[name]
        # evaluate if any of the resources becomes negative
        if resources[name] < 0:
            # have an error message for fun that should theoretically never proc
            print(f"Error, insufficient {name}, aborting")
            off()
    print(f"Here is your {order}. Enjoy!")


actions = {"report": report, "off": off}
continue_loop = True
while continue_loop:
    order = take_order()
    sufficient_resources, required_resources = check_resources(order)
    if sufficient_resources:
        cost, value = process_coins(order)
        transaction_successful = check_transaction(cost, value)
        if transaction_successful:
            add_money(cost)
            make_coffee(order, required_resources)

off()
