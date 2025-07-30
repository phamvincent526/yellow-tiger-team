menu = {
    "Pizza": 2.99,
    "Burger": 3.99,
    "Hot dog": 1.99,
    "Cheese": 0.59,
    "Ice cream": 1.49,
    "Churro": 0.79,
    "Soda": 0.89
}

def total_price(item1, item2):
    total = menu[item1] + menu[item2]
    return total

def price_difference(item1, item2):
    difference = menu[item1] - menu[item2]
    return abs(difference)

def inflation(item, inflation):
    menu[item] = menu[item] * inflation
    return menu

def deflation(item, deflation):
    menu[item] = menu[item] / deflation
    return menu

def discount(item, discount):
    menu[item] = menu[item] * (1 - discount / 100)
    return menu[item]

print(total_price("Cheese", "Hot dog"))
print(price_difference("Burger", "Cheese"))
print(inflation("Pizza", 2))
print(deflation("Pizza", 2))
print(discount("Pizza", 99))

