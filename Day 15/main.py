MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 200,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": {"amount": 300, "unit": "ml"},
    "Milk": {"amount": 200, "unit": "ml"},
    "Coffee": {"amount": 100, "unit": "g"},
}


quarters = 0.25
dimes = 0.10
nickels = 0.05
pennies = 0.01

money_balance = {
    "quarters_balance": 0.0,
    "dimes_balance": 0.0,
    "nickels_balance": 0.0,
    "pennies_balance": 0.0
}

total_money_balance = 0.0
user_menu_prompt = str

#def menu_function():

while user_menu_prompt != "off":
    user_menu_prompt = input("What would you like? (espresso/latte/cappuccino):")
    # TODO: 1. Print report of all coffee machine resources
    if user_menu_prompt == "report":
        for item, details in resources.items():
            amount = details["amount"]
            unit = details["unit"]
            print(f"{item}: {amount} {unit}")
        print(f"Money: ${total_money_balance}")

    if user_menu_prompt == "espresso":
        # TODO: 2. Check resources sufficient?
        if resources["Water"]["amount"] < MENU["espresso"]["ingredients"]["Water"]:
            print("Sorry there is not enough water.")
        # if resources["Milk"] < MENU["espresso"]["ingredients"]["Milk"]:
        #     print("Sorry there is not enough milk.")
        if resources["Coffee"]["amount"] < MENU["espresso"]["ingredients"]["Coffee"]:
            print("Sorry there is not enough coffee.")
        if resources["Water"]["amount"] >= MENU["espresso"]["ingredients"]["Water"] and resources["Coffee"]["amount"] >= MENU["espresso"]["ingredients"]["Coffee"]:
            # TODO: 3. Process coins
            money_balance["quarters_balance"] = int(input("How many quarters?:"))
            money_balance["dimes_balance"] = int(input("How many dimes?:"))
            money_balance["nickels_balance"] = int(input("How many nickels?:"))
            money_balance["pennies_balance"] = int(input("How many pennies?:"))
            espresso_transaction = (money_balance["quarters_balance"]*quarters) + (money_balance["dimes_balance"]*dimes) + (money_balance["nickels_balance"]*nickels) + (money_balance["pennies_balance"]*pennies)

            if espresso_transaction >= MENU["espresso"]["cost"]:
                total_money_balance += MENU["espresso"]["cost"]
                resources["Water"]["amount"] -= MENU["espresso"]["ingredients"]["Water"]
                # resources["Milk"]["amount"] -= MENU["espresso"]["ingredients"]["Milk"]
                resources["Coffee"]["amount"] -= MENU["espresso"]["ingredients"]["Coffee"]
                print(f"Here is your change: {espresso_transaction - MENU["espresso"]["cost"]}")
                print("Here is your espresso. Enjoy!")
            if espresso_transaction < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
        # print(total_money_balance)
        # print(money_balance)

    if user_menu_prompt == "latte":
        # TODO: 2. Check resources sufficient?
        if resources["Water"]["amount"] < MENU["latte"]["ingredients"]["Water"]:
            print("Sorry there is not enough water.")
        if resources["Milk"]["amount"] < MENU["latte"]["ingredients"]["Milk"]:
            print("Sorry there is not enough milk.")
        if resources["Coffee"]["amount"] < MENU["latte"]["ingredients"]["Coffee"]:
            print("Sorry there is not enough coffee.")
        if resources["Water"]["amount"] >= MENU["latte"]["ingredients"]["Water"] and resources["Coffee"]["amount"] >= MENU["latte"]["ingredients"]["Coffee"] and resources["Milk"]["amount"] >= MENU["latte"]["ingredients"]["Milk"]:
            # TODO: 3. Process coins
            money_balance["quarters_balance"] = int(input("How many quarters?:"))
            money_balance["dimes_balance"] = int(input("How many dimes?:"))
            money_balance["nickels_balance"] = int(input("How many nickels?:"))
            money_balance["pennies_balance"] = int(input("How many pennies?:"))
            latte_transaction = (money_balance["quarters_balance"]*quarters) + (money_balance["dimes_balance"]*dimes) + (money_balance["nickels_balance"]*nickels) + (money_balance["pennies_balance"]*pennies)

            if latte_transaction >= MENU["latte"]["cost"]:
                total_money_balance += MENU["latte"]["cost"]
                resources["Water"]["amount"] -= MENU["latte"]["ingredients"]["Water"]
                resources["Milk"]["amount"] -= MENU["latte"]["ingredients"]["Milk"]
                resources["Coffee"]["amount"] -= MENU["latte"]["ingredients"]["Coffee"]
                print(f"Here is your change: {latte_transaction - MENU["latte"]["cost"]}")
                print("Here is your latte. Enjoy!")
            if latte_transaction < MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
        # print(total_money_balance)
        # print(money_balance)

    if user_menu_prompt == "cappuccino":
        # TODO: 2. Check resources sufficient?
        if resources["Water"]["amount"] < MENU["cappuccino"]["ingredients"]["Water"]:
            print("Sorry there is not enough water.")
        if resources["Milk"]["amount"] < MENU["cappuccino"]["ingredients"]["Milk"]:
            print("Sorry there is not enough milk.")
        if resources["Coffee"]["amount"] < MENU["cappuccino"]["ingredients"]["Coffee"]:
            print("Sorry there is not enough coffee.")
        if resources["Water"]["amount"] >= MENU["cappuccino"]["ingredients"]["Water"] and resources["Coffee"]["amount"] >= MENU["cappuccino"]["ingredients"]["Coffee"] and resources["Milk"]["amount"] >= MENU["cappuccino"]["ingredients"]["Milk"]:
            # TODO: 3. Process coins
            money_balance["quarters_balance"] = int(input("How many quarters?:"))
            money_balance["dimes_balance"] = int(input("How many dimes?:"))
            money_balance["nickels_balance"] = int(input("How many nickels?:"))
            money_balance["pennies_balance"] = int(input("How many pennies?:"))
            cappuccino_transaction = (money_balance["quarters_balance"]*quarters) + (money_balance["dimes_balance"]*dimes) + (money_balance["nickels_balance"]*nickels) + (money_balance["pennies_balance"]*pennies)

            if cappuccino_transaction >= MENU["cappuccino"]["cost"]:
                total_money_balance += MENU["cappuccino"]["cost"]
                resources["Water"]["amount"] -= MENU["cappuccino"]["ingredients"]["Water"]
                resources["Milk"]["amount"] -= MENU["cappuccino"]["ingredients"]["Milk"]
                resources["Coffee"]["amount"] -= MENU["cappuccino"]["ingredients"]["Coffee"]
                print(f"Here is your change: {cappuccino_transaction - MENU["cappuccino"]["cost"]}")
                print("Here is your cappuccino. Enjoy!")
            if cappuccino_transaction < MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
        # print(total_money_balance)
        # print(money_balance)

    if user_menu_prompt == "off":
        print("Turning off... Machine is now off.")

# TODO: 4. Check transaction successful?
# TODO: 5. Make Coffee