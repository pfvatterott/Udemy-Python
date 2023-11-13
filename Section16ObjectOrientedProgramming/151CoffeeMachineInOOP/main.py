from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


def coffee_machine():
    drink = input(f"What would you like? ({menu.get_items()})?: ").lower()
    if drink == "report":
        maker.report()
        coffee_machine()
    elif drink == "off":
        return
    else:
        if maker.is_resource_sufficient(menu.find_drink(drink)) == False:
            coffee_machine()
        else:
            cost = menu.find_drink(drink).cost
            print(f"That will be ${cost}")
            if money.make_payment(cost):
                maker.make_coffee(menu.find_drink(drink))
                coffee_machine()
    

coffee_machine()