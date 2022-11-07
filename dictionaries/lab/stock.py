stock = input().split()
products_to_look_for = input().split()
inventory = {stock[i]: stock[i + 1] for i in range(0, len(stock), 2)}
# inventory = {}
# for i in range(0, len(stock), 2):  # Creating dictionary using for cycle
#     key = stock[i]
#     value = stock[i + 1]
#     inventory[key] = value
for product in products_to_look_for:
    if product in inventory:
        print(f"We have {inventory[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
