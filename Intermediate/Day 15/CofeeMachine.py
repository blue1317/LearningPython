# Coffee Machine Program
# Starting Resources: Water 300, Milk 200, Coffee 100, Money 0.00

orderCompleted = True

quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 250,
    "money": 0.00
}

espresso = {"water": 50, "milk": 0, "coffee": 18, "cost": 2.50}
latte = {"water": 200, "milk": 150, "coffee": 24, "cost": 3.50}
cappuccino = {"water": 250, "milk": 100, "coffee": 24, "cost": 4.00}


def resourceCheck(item):
    haveWater = haveMilk = haveCoffee = False
    error = ""
    if item == "latte":
        if latte["water"] <= resources["water"]:
            haveWater = True
        if latte["milk"] <= resources["milk"]:
            haveMilk = True
        if latte["coffee"] <= resources["coffee"]:
            haveCoffee = True
    elif item == "espresso":
        if espresso["water"] <= resources["water"]:
            haveWater = True
        if espresso["milk"] <= resources["milk"]:
            haveMilk = True
        if espresso["coffee"] <= resources["coffee"]:
            haveCoffee = True
    elif item == "cappuccino":
        if cappuccino["water"] <= resources["water"]:
            haveWater = True
        if cappuccino["milk"] <= resources["milk"]:
            haveMilk = True
        if cappuccino["coffee"] <= resources["coffee"]:
            haveCoffee = True

    if haveWater == True and haveMilk == True and haveCoffee == True:
        return True
    else:
        if not haveWater:
            return "Sorry there is not enough water."
        elif not haveMilk:
            return "Sorry there is not enough milk."
        else:
            return "Sorry there is not enough coffee."


def calculateChange(item, money):
    change = 0.00
    if item == "latte":
        if money > latte["cost"]:
            change = round(abs(money - latte["cost"]), 2)
            return change
        elif money < latte["cost"]:
            return -1
        else:
            return 0
    elif item == "espresso":
        if money > espresso["cost"]:
            change = round(abs(money - espresso["cost"]), 2)
            return change
        elif money < espresso["cost"]:
            return -1
        else:
            return 0
    elif item == "cappuccino":
        if money > cappuccino["cost"]:
            change = round(abs(money - cappuccino["cost"]), 2)
            return change
        elif money < cappuccino["cost"]:
            return -1
        else:
            return 0


while orderCompleted:
    order = input("What would you like drink? (espresso/latte/cappuccino): ")

    if order == "off":
        print("Turning machine Off ...")
        break
    elif order == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \n"
              f"Money: ${resources['money']:.2f} \n")
        orderCompleted = True
    elif order == "":
        orderCompleted = True
    else:
        orderCompleted = False

        haveEnoughResources = resourceCheck(order)
        if haveEnoughResources != True:
            print(haveEnoughResources + " Please try again later")
            break
        else:
            # print("Do we have enough resources? " + str(haveEnoughResources))
            if order == "latte":
                print(f"The {order} cost ${latte['cost']:.2f}. You will be prompted to enter your money next.")
            if order == "espresso":
                print(f"The {order} cost ${espresso['cost']:.2f}. You will be prompted to enter your money next.")
            if order == "cappuccino":
                print(f"The {order} cost ${cappuccino['cost']:.2f}. You will be prompted to enter your money next.")

            quarterEntered = int(input("How many quarters are you putting into the machine? "))
            dimeEntered = int(input("How many dimes are you putting into the machine? "))
            nickleEntered = int(input("How many nickles are you putting into the machine? "))
            pennyEntered = int(input("How many pennies are you putting into the machine? "))

            moneyEntered = quarterEntered * quarter + dimeEntered * dime + nickleEntered * nickle + pennyEntered * penny

            refund = calculateChange(order, moneyEntered)
            if refund == -1:
                print("Sorry that's not enough money. Money refunded.")
                orderCompleted = True
            elif refund == 0:
                print(f"Depositing money and making {order}...")
                resources["money"] += moneyEntered
                if order == "latte":
                    resources["water"] -= latte["water"]
                    resources["milk"] -= latte["milk"]
                    resources["coffee"] -= latte["coffee"]
                elif order == "espresso":
                    resources["water"] -= latte["water"]
                    resources["milk"] -= latte["milk"]
                    resources["coffee"] -= latte["coffee"]
                elif order == "cappuccino":
                    resources["water"] -= latte["water"]
                    resources["milk"] -= latte["milk"]
                    resources["coffee"] -= latte["coffee"]

                print(f"Here is your {order}. Enjoy!")
                orderCompleted = True
            else:
                print(f"Here is ${refund:.2f} in change.")
                print(f"Depositing money and making {order}...")
                resources["money"] += moneyEntered - refund
                if order == "latte":
                    resources["water"] -= latte["water"]
                    resources["milk"] -= latte["milk"]
                    resources["coffee"] -= latte["coffee"]
                elif order == "espresso":
                    resources["water"] -= latte["water"]
                    resources["milk"] -= latte["milk"]
                    resources["coffee"] -= latte["coffee"]
                elif order == "cappuccino":
                    resources["water"] -= latte["water"]
                    resources["milk"] -= latte["milk"]
                    resources["coffee"] -= latte["coffee"]

                print(f"Here is your {order}. Enjoy!")
                orderCompleted = True

