from machine_details import MENU, resources

def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] - MENU[drink]["ingredients"][ingredient] < 0:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


def insert_coins(price):
    print(f"Please insert ${price} in coins")
    total = 0
    total += int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input("How many nickles?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    if total > price:
        change = round(total - price, 2)
        print(f"Here is ${change} in change.")
    elif total < price:
        return False
    resources["money"] += price
    return True


def deduct_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]


def coffee_machine():
    drink = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if drink == "report":
        print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${resources["money"]}")
        coffee_machine()
    elif drink == "off":
        return
    else:
        if check_resources(drink) == False:
            coffee_machine()
        else:
            enough_coins = insert_coins(MENU[drink]["cost"])
            if enough_coins:
                deduct_resources(drink)
                print(f"Here is your {drink}. Enjoy!")
                coffee_machine()
            else:
                print("Sorry, that's not enough money. Money refunded.")
                coffee_machine()
    
        
        
coffee_machine()