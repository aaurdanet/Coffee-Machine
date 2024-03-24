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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def get_report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money}$")


def make_espresso(amount_of_quarters, amount_of_dimes, amount_of_nickles, amount_of_pennies):
    making_coffee = True
    water = MENU['espresso']['ingredients']['water']
    coffee = MENU['espresso']['ingredients']['coffee']

    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    value = MENU['espresso']['cost']
    total = amount_of_quarters * quarters
    total += amount_of_dimes * dimes
    total += amount_of_nickles * nickles
    total += amount_of_pennies * pennies

    if total < value:
        return 1

    # checking water
    current_water = resources['water']
    if water > current_water:
        print("Sorry there is not enough water.")
        making_coffee = False
    else:
        final_water = current_water - water
        resources['water'] = final_water

    # checking coffee
    current_coffee = resources['coffee']
    if coffee > current_coffee:
        print("Sorry there is not enough coffee.")
        making_coffee = False
    else:
        final_coffee = current_coffee - coffee
        resources['coffee'] = final_coffee

    if not making_coffee:
        return 0
    else:
        return 1


def make_latte(amount_of_quarters, amount_of_dimes, amount_of_nickles, amount_of_pennies):
    making_coffee = True
    water = MENU['latte']['ingredients']['water']
    milk = MENU['latte']['ingredients']['milk']
    coffee = MENU['latte']['ingredients']['coffee']

    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    value = MENU['latte']['cost']
    total = amount_of_quarters * quarters
    total += amount_of_dimes * dimes
    total += amount_of_nickles * nickles
    total += amount_of_pennies * pennies

    if total < value:
        return 1

    # checking water
    current_water = resources['water']
    if water > current_water:
        print("Sorry there is not enough water.")
        making_coffee = False
    else:
        final_water = current_water - water
        resources['water'] = final_water

    # checking milk
    current_milk = resources['milk']
    if milk > current_milk:
        print("Sorry there is not enough milk.")
        making_coffee = False
    else:
        final_milk = current_milk - milk
        resources['milk'] = final_milk

    # checking coffee
    current_coffee = resources['coffee']
    if coffee > current_coffee:
        print("Sorry there is not enough coffee.")
        making_coffee = False
    else:
        final_coffee = current_coffee - coffee
        resources['coffee'] = final_coffee

    if not making_coffee:
        return 0
    else:
        return 1


def make_cappuccino(amount_of_quarters, amount_of_dimes, amount_of_nickles, amount_of_pennies):
    making_coffee = True
    water = MENU['cappuccino']['ingredients']['water']
    milk = MENU['cappuccino']['ingredients']['milk']
    coffee = MENU['cappuccino']['ingredients']['coffee']

    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    value = MENU['cappuccino']['cost']
    total = amount_of_quarters * quarters
    total += amount_of_dimes * dimes
    total += amount_of_nickles * nickles
    total += amount_of_pennies * pennies

    if total < value:
        return 1

    # checking water
    current_water = resources['water']
    if water > current_water:
        print("Sorry there is not enough water.")
        making_coffee = False
    else:
        final_water = current_water - water
        resources['water'] = final_water

    # checking milk
    current_milk = resources['milk']
    if milk > current_milk:
        print("Sorry there is not enough milk.")
        making_coffee = False
    else:
        final_milk = current_milk - milk
        resources['milk'] = final_milk

    # checking coffee
    current_coffee = resources['coffee']
    if coffee > current_coffee:
        print("Sorry there is not enough coffee.")
        making_coffee = False
    else:
        final_coffee = current_coffee - coffee
        resources['coffee'] = final_coffee

    if not making_coffee:
        return 0
    else:
        return 1


def payment(chosen_coffee, amount_of_quarters, amount_of_dimes, amount_of_nickles, amount_of_pennies):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    if chosen_coffee == "espresso":
        value = MENU['espresso']['cost']
        total = amount_of_quarters * quarters
        total += amount_of_dimes * dimes
        total += amount_of_nickles * nickles
        total += amount_of_pennies * pennies
        if total > value:
            float_coins = total - value
            rounded_coins = round(float_coins, 2)
            refund = f"Here is ${rounded_coins} in change."
            resources['money'] += value
            return refund
        elif total == value:
            resources['money'] += value
            return ("NO CHANGE")
        elif total < value:
            return 0

    if chosen_coffee == "latte":
        value = MENU['latte']['cost']
        total = amount_of_quarters * quarters
        total += amount_of_dimes * dimes
        total += amount_of_nickles * nickles
        total += amount_of_pennies * pennies
        if total > value:
            float_coins = total - value
            rounded_coins = round(float_coins, 2)
            refund = f"Here is ${rounded_coins} in change."
            resources['money'] += value
            return refund
        elif total == value:
            resources['money'] += value
            return ("NO CHANGE")
        elif total < value:
            return 0

    if chosen_coffee == "cappuccino":
        value = MENU['cappuccino']['cost']
        total = amount_of_quarters * quarters
        total += amount_of_dimes * dimes
        total += amount_of_nickles * nickles
        total += amount_of_pennies * pennies
        if total > value:
            float_coins = total - value
            rounded_coins = round(float_coins, 2)
            refund = f"Here is ${rounded_coins} in change."
            resources['money'] += value
            return refund
        elif total == value:
            resources['money'] += value
            return "NO CHANGE"
        elif total < value:
            return 0


def machine():
    serving = True

    while serving:

        option = input("What would you like? (espresso/latte/cappuccino):\n")

        if option == "off":
            print("Coffe machine is shutting down....")
            serving = False
            exit()

        if option == "report":
            get_report()
            machine()

        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        if option == "espresso":
            espresso = make_espresso(quarters, dimes, nickles, pennies)
            if espresso == 1:
                coins = payment(option, quarters, dimes, nickles, pennies)
                if coins == 0:
                    error = "You do not have enough money. Money refunded"
                    print(error)
                else:
                    print("Here is your espresso ☕️. Enjoy!")
                print(f"{coins}")
            elif espresso == 0:
                coins = payment(option, quarters, dimes, nickles, pennies)
                serving = False
                
        elif option == "latte":
            latte = make_latte(quarters, dimes, nickles, pennies)
            if latte == 1:
                coins = payment(option, quarters, dimes, nickles, pennies)
                if coins == 0:
                    error = "You do not have enough money. Money refunded"
                    print(error)
                else:
                    print("Here is your latte ☕️. Enjoy!")
                print(f"{coins}")
            elif latte == 0:
                coins = payment(option, quarters, dimes, nickles, pennies)
                serving = False
                
        elif option == "cappuccino":
            cappuccino = make_cappuccino(quarters, dimes, nickles, pennies)
            if cappuccino == 1:
                coins = payment(option, quarters, dimes, nickles, pennies)
                if coins == 0:
                    error = "You do not have enough money. Money refunded"
                    print(error)
                else:
                    print("Here is your cappuccino ☕️. Enjoy!")
                print(f"{coins}")
            elif cappuccino == 0:
                coins = payment(option, quarters, dimes, nickles, pennies)
                serving = False


machine()
