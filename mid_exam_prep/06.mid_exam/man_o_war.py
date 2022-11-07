def fire(index, damage):
    if 0 <= index < len(warship_sections):
        warship_sections[index] -= damage
        if warship_sections[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()


def defend(start_index, end_index, damage):
    if 0 <= start_index < len(pirate_ship_sections) and \
            end_index < len(pirate_ship_sections):
        for section in range(start_index, end_index + 1):
            pirate_ship_sections[section] -= damage
            if pirate_ship_sections[section] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()


def repair(index, heal):
    if 0 <= index < len(pirate_ship_sections):
        pirate_ship_sections[index] += heal
        if pirate_ship_sections[index] > max_health_per_section:
            pirate_ship_sections[index] = max_health_per_section


def status():
    count = 0
    for section in pirate_ship_sections:
        if section < max_health_per_section * 0.2:
            count += 1
    return f"{count} sections need repair."


pirate_ship_sections = list(map(int, input().split('>')))
warship_sections = list(map(int, input().split('>')))
max_health_per_section = int(input())

command = input()
while command != "Retire":
    action, *info = [x if x.isalpha() else int(x) for x in command.split()]

    if action == "Fire":
        fire(info[0],info[1])
    elif action == "Defend":
        defend(info[0],info[1], info[2])
    elif action == "Repair":
        repair(info[0],info[1])
    elif action == "Status":
        print(status())
    command = input()

if command == "Retire":
    print(f"Pirate ship status: {sum(pirate_ship_sections)}")
    print(f"Warship status: {sum(warship_sections)}")