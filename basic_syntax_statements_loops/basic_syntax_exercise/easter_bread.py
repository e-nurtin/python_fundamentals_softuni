budget = float(input())
flour_price_per_kg = float(input())
budget_left = budget
eggs_per_pack_price = flour_price_per_kg * 0.75
milk_per_loaf_price = (flour_price_per_kg * 1.25) / 4
price_per_loaf = flour_price_per_kg + eggs_per_pack_price\
                 + milk_per_loaf_price
current_count_bread = 0
colored_eggs_count = 0
while budget_left > price_per_loaf:
    budget_left -= price_per_loaf
    current_count_bread += 1
    colored_eggs_count += 3
    if current_count_bread % 3 == 0:
        colored_eggs_count -= (current_count_bread - 2)
print(f"You made {current_count_bread} loaves of Easter bread!"
      f" Now you have {colored_eggs_count} "
      f"eggs and {budget_left:.2f}BGN left.")

