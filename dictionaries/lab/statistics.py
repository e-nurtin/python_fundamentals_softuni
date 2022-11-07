inventory = {}
command = input()
while command != "statistics":
    product, quantity = [int(x) if x.isdigit() else x for x in
                         command.split(': ')]

    if product not in inventory:
        inventory[product] = quantity
    else:
        inventory[product] += quantity

    command = input()

result = [f"- {key}: {value}" for key,value in inventory.items()]
print("Products in stock:")
print('\n'.join(result))
print(f"Total Products: {len(inventory)}")
print(f"Total Quantity: {sum(inventory.values())}")
