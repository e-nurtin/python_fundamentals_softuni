budget = float(input())
flour_per_kg = float(input())
eggs_per_pack = flour_per_kg * 0.75
milk_per_loaf = (flour_per_kg * 1.25) / 4
price_per_loaf = flour_per_kg + milk_per_loaf + eggs_per_pack

current_bread_count = 0
colored_eggs_count = 0
while budget > price_per_loaf:
    current_bread_count += 1
    budget -= price_per_loaf
    colored_eggs_count += 3

    if current_bread_count % 3 == 0:
        colored_eggs_count -= (current_bread_count - 2)

print(f"You made {current_bread_count} loaves of Easter bread! Now you have "
      f"{colored_eggs_count} eggs and {budget:.2f}BGN left.")
