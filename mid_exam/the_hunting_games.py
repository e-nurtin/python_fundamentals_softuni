days_of_adventure = int(input())
count_of_players = int(input())
group_energy = float(input())

water_supply = float(input()) * (count_of_players * days_of_adventure)
food_supply = float(input()) * (count_of_players * days_of_adventure)


current_day = 1
while current_day <= days_of_adventure:
    energy_loss = float(input())
    group_energy -= energy_loss

    if group_energy <= 0:
        break

    if current_day % 2 == 0:
        group_energy += (group_energy * 0.05)
        water_supply = water_supply * 0.7

    if current_day % 3 == 0:
        group_energy += (group_energy * 0.10)
        food_supply -= (food_supply / count_of_players)

    current_day += 1


if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - "
          f"{group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with "
          f"{food_supply:.2f} food and {water_supply:.2f} water.")
