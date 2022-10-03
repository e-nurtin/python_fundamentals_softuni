commands_list = input().split("|")
gained_energy = 0
current_energy = 100
coins = 100
cannot_afford_ingredient = False
for command in commands_list:
    current_event = []
    event_value = 0
    for element in command.split("-"):
        current_event.append(element)
    event_value = int(current_event[-1])
    if "rest" in current_event:
        if current_energy + event_value <= 100:
            current_energy += event_value
        else:
            event_value = abs(100 - current_energy)
            current_energy = 100
        print(f"You gained {event_value} energy.")
        print(f"Current energy: {current_energy}.")
    elif "order" in current_event:
        if current_energy >= 30:
            current_energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        ingredient = current_event[0]
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {ingredient}.")
        else:
            cannot_afford_ingredient = True
            print(f"Closed! Cannot afford {ingredient}.")
            break
if not cannot_afford_ingredient:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")
