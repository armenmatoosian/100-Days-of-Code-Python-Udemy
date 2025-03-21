from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_power = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while machine_power:
    order_name = input(f"What would you like? {menu.get_items()}: ")

    if order_name == "off":
        print("Machine powering down... Machine is now off")
        machine_power = False

    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()

    elif menu.find_drink(order_name):
        if coffee_maker.is_resource_sufficient(menu.find_drink(order_name)) is True:
            if money_machine.make_payment(menu.find_drink(order_name).cost) is True:
                coffee_maker.make_coffee(menu.find_drink(order_name))