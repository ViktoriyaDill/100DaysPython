from resources import MENU, resources

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
total = 0


def is_change(drink):
    global total
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    total1 = QUARTERS * quarter + DIMES * dime + NICKLES * nickle + PENNIES * penny

    difference = round(total1 - MENU[drink]['cost'], 2)
    if MENU[drink]['cost'] > total1:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif MENU[drink]['cost'] <= total1:
        total += MENU[drink]['cost']
        print(f"Here is ${difference} in change.")
        return True


def is_resources(drink):
    drink_obj = MENU[drink]
    for key in drink_obj['ingredients']:
        if resources[key] < drink_obj['ingredients'][key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def get_coffee():
    global total
    off = False
    new_resourse = {}
    while not off:
        offer = input("What would you like? (espresso/latte/cappuccino)")
        if offer == 'report':
            print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\nmoney: ${total}")
        elif offer == 'off':
            off = True
        else:
            if offer == "espresso" or offer == "latte" or offer == "cappuccino":
                if is_resources(offer):
                    for key in MENU[offer]["ingredients"]:
                        new_resourse[key] = resources[key] - MENU[offer]["ingredients"][key]
                        resources.update(new_resourse)
                    if is_change(offer):
                        print(f"Here is your {offer} ☕. Enjoy!")


get_coffee()

















