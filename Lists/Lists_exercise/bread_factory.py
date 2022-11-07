events_list = input().split("|")
gained_energy = 0
current_energy = 100
coins = 100
closed = False
for event in events_list:
    current_event, value = event.split('-')
    value = int(value)
    if current_event == "rest":
        current_energy += value
        if current_energy > 100:
            value -= abs(100 - current_energy)
            current_energy = 100
        print(f"You gained {value} energy.")
        print(f"Current energy: {current_energy}.")
    elif current_event == "order":
        if current_energy >= 30:
            current_energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {current_event}.")
        else:
            closed = True
            print(f"Closed! Cannot afford {current_event}.")
            break
if not closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")
