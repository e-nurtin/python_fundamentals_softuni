food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
puppy_weight = float(input())

food_in_grams = food_quantity * 1000
hay_in_grams = hay_quantity * 1000
cover_in_grams = cover_quantity * 1000
puppy_weight_in_grams = puppy_weight * 1000
more_food_is_needed = False
for day in range(1, 30 + 1):
    food_in_grams -= 300

    if day % 2 == 0:
        hay_in_grams -= (food_in_grams * 0.05)

    if day % 3 == 0:
        cover_in_grams -= (puppy_weight_in_grams / 3)

    if food_in_grams < 0 or hay_in_grams < 0 or cover_in_grams < 0:
        more_food_is_needed = True
        break

if more_food_is_needed:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: "
          f"{food_in_grams / 1000:.2f},"
          f" Hay: {hay_in_grams / 1000:.2f}, Cover: "
          f"{cover_in_grams / 1000:.2f}.")
