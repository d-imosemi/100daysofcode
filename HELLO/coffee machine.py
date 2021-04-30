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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def suff(order_ing):
    for items in order_ing:
        if order_ing[items] >= resources[items]:
            print(f"sorry there is not enough {items}")
            return False
    return True


def process_coin():
    """returns the total calculated coins insrted"""
    print("please insert coins.")
    total = int(input("how many quater?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total



def trans_succ(money_recived, drink_cost):
    """return true if the payment is accpted or false if is insufficient"""
    if money_recived >- drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's nor enough money, money refunded")
        return False


def make_coffe(drink_name, order_ing):
    for item in order_ing:
        resources[item] -= order_ing[item]
    print(f"here is your {drink_name}")


cont = True
while cont:
    order = input("what would you like? (espressor/latte/cappuccino): ").lower()
    if order == "off":
        cont = False
    elif  order == "report":
        print(f"water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}g")
        print(f"money : ${profit}")
    else:
        drink = MENU[order]
        if suff(drink['ingredients']):
            payment = process_coin()
            if trans_succ(payment, drink["cost"]):
                make_coffe(order, drink["ingredients"])






 