energy_left = int(input())

won_battles = 0
no_energy_left = False
command = input()
while command != "End of battle":
    distance_to_enemy = int(command)

    if distance_to_enemy <= energy_left:
        energy_left -= distance_to_enemy
        won_battles += 1
        if won_battles % 3 == 0:
            energy_left += won_battles
    else:
        no_energy_left = True
        break
    command = input()

if no_energy_left:
    print(f"Not enough energy! Game ends with {won_battles} won battles and "
          f"{energy_left} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {energy_left}")