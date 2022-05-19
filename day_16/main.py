from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
OFF = False

while not OFF:
    order = input(f"What would you like? {menu.get_items()} ")
    if order == 'off':
        OFF = True
    elif order == 'report':
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)












