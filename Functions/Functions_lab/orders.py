def order(product: str, count: int):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1.00
    elif product == "snacks":
        price = 2.00
    return print(f"{price * count:.2f}")


command = input()
quantity = int(input())

order(command, quantity)