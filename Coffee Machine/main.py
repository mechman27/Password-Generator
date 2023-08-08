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
profit = 0
resources = {
            "water": 300, 
            "milk": 200, 
            "coffee": 100
            }


def process_payment(payment, drink_cost):
    change = round(payment - drink_cost, 2)
    if payment < drink_cost:
        print(f"Sorry, you need ${drink_cost - payment} more")
        return False
    elif payment > drink_cost:
        print(f"Here is your change: ${change}")
        return True
    else:
        return True


def resource_check(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True


def process_coins():
    print("Please Insert Coins")
    total = int(input("How many Quarters?:")) * 0.25
    total += int(input("How many Dimes?:")) * 0.10
    total += int(input("How many Nickels?:")) * 0.05
    total += int(input("How many Pennies?:")) * 0.01
    return total


def make_order(resources, order_ingredients):
    for items in resources:
        resources[items] -= order_ingredients[items]
    print(f"You ordered has been made.")


def run_machine(profit):
    is_on = True
    while is_on:
        choice = input("What would you like? (Espresso/Latte/Cappuccino):").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(
                f"Water: {resources['water']}"
                f"\nMilk: {resources['milk']}"
                f"\nCoffee: {resources['coffee']}"
                f"\nMoney: ${profit}"
            )
        else:
            order = MENU[choice]
            if resource_check(order["ingredients"]):
                payment = process_coins()
                if process_payment(payment, MENU[choice]["cost"]):
                    profit += order["cost"]
                    make_order(resources, order["ingredients"])


run_machine(profit)
