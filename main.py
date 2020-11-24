MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":50,
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

resources_available = False
payment_ok = True
check_maintenance = True

def check_resourse(coffee_name):
    coffee=MENU[coffee_name]
    if coffee['ingredients']['water'] <= resources['water']:
        if coffee['ingredients']['milk'] <= resources['milk']:
            if coffee['ingredients']['coffee'] <= resources['coffee']:
                return True
            else:
                print("You don't have enough coffee")
                return False
        else:
            print("You don't have enough milk")
            return False
    else:
        print("You don't have enough Water")
        return False


def add_payment(payment):
    previous_payments=resources["money"]
    return previous_payments + payment

def sub_resourse(coffee_name):
    coffee = MENU[coffee_name]['ingredients']
    resources['water'] -= coffee['water']
    resources['milk'] -= coffee['milk']
    resources['coffee'] -= coffee['coffee']

def check_transaction(quaters,dimes,nickels,pennies,coffee_name):
    add_coins= (0.25*quaters)+( 0.1*dimes)+(0.05*nickels)+(0.01*pennies)
    coffee = MENU[coffee_name]
    if coffee["cost"] < add_coins:
        changes= add_coins - coffee["cost"]
        sub_resourse(coffee_name)
        resources["money"] = add_payment(coffee["cost"])
        print(f"Here is your changes {coffee_name}")
        print(f"Here is your changes {round(changes,2)}")
        return True
    elif coffee["cost"] == add_coins:
        sub_resourse(coffee_name)
        resources["money"] = add_payment(coffee["cost"])
        print(f"Here is your changes {coffee_name}")
        return True
    else:
        print("Not enough Money")
        return False

while check_maintenance:
    user_input=input("What would you like? (espresso/latte/cappuccino):").lower()

    if(user_input == "off"):
        check_maintenance = False

    if user_input== "report":
        print(f"Water = {resources['water']}ml \nMilk = {resources['milk']}ml \nCoffee = {resources['coffee']}g \nMoney = ${resources['money']}")

    if user_input == "espresso":
        resources_available = check_resourse("espresso")
    elif user_input == "latte":
        resources_available = check_resourse("latte")
    elif user_input == "cappuccino":
        resources_available = check_resourse("cappuccino")

    if resources_available:
        print("Please Insert Coins")
        quaters = int(input("For Quarters "))
        dimes = int(input("For Dimes "))
        nickels = int(input("For Nickels "))
        pennies = int(input("For Pennices "))
        payment_ok = check_transaction(quaters,dimes,nickels,pennies,user_input)
        resources_available = False

