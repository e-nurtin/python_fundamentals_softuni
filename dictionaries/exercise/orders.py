products = {}
command = input()
while command != "buy":
    name, price, quantity = [int(x) if x.isdigit() else x for x
                             in command.split()]
    if name not in products:
        products[name] = []
        products[name].append(price)
        products[name].append(0)
    elif products[name][0] != price:
        products[name][0] = price
    products[name][1] += quantity
    command = input()
for product_name, values in products.items():
    print(f"{product_name} -> {float(values[0])*values[1]:.2f}")