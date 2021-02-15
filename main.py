MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "water": 800,
    "milk": 800,
    "coffee": 800,
}

profit = 0


def check_resources(choice, res):
    checker = MENU[choice]['ingredients']
    if checker['water'] > res['water']:
        print("Sorry not enough water")
    elif checker['milk'] > res['milk']:
        print("Sorry not enough milk")
    elif checker['coffee'] > res['coffee']:
        print("Sorry not enough coffee")
    else:
        return True


def use_resources(choice, res):
    checker = MENU[choice]['ingredients']
    for i in res:
        res[i] -= checker[i]
    print(res)


# PRINT REPORT TO SHOW THE EXISTING RESOURCES
def report(x):
    for i in x:
        print(f"{i.capitalize()} : {x[i]}ml")
    print(f"Money: ${profit}")


def drink(choice, amount):
    checker = MENU[choice]['cost']
    if checker == amount:
        print('Here is your drink! Enjoy!')
        global profit
        profit += checker
        use_resources(choice, resources)
        return True
    elif checker > paid:
        print("Sorry that's not enough money, Money refunded")
        return False
    elif checker < paid:
        print(f'Here is your drink and your change {round((paid - checker), 2)}')
        profit += checker
        use_resources(choice, resources)
        return True


dispense_new_drink = True

while dispense_new_drink:
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')

    if user_choice == 'off':
        exit()
    elif user_choice == "report":
        report(resources)

    chk_res = check_resources(user_choice, resources)
    if chk_res:
        # TODO FIX VALUE ERROR IF NO VALUE ENTERED FOR MONEY
        print("Please insert coins: ")
        quarters = int(input('how many quarters?: '))
        dimes = int(input('how many dimes?: '))
        nickels = int(input('how many nickels?: '))
        pennies = int(input('how many pennies?: '))
        paid = float(0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies)
        print(f"You gave me ${round(paid, 2)}")
        drink(user_choice, paid)
        
        should_continue = input("Do you want another drink? ")
        if should_continue == 'y':
            dispense_new_drink = True
        elif should_continue == "report":
            report(resources)
        else:
            dispense_new_drink = False

