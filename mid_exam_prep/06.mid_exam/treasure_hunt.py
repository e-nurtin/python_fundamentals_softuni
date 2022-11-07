def loot(items):
    for item in items:
        if item not in treasure_chest:
            treasure_chest.insert(0, item)


def drop(index):
    if len(treasure_chest) > index:
        treasure_chest.append(treasure_chest.pop(index))


def steal(count_of_items, treasures):
    remove = treasures[- count_of_items:]
    treasures = treasures[: -count_of_items]
    print(', '.join(remove))
    return treasures


treasure_chest = input().split('|')

command = input()
while command != "Yohoho!":
    action, *info = [x if x.isalpha() else int(x) for x in command.split()]
    if action == "Loot":
        loot(info)
    elif action == "Drop":
        drop(info[0])
    elif action == "Steal":
        treasure_chest = steal(info[0], treasure_chest)
    command = input()

if len(treasure_chest) > 0:
    average_treasure = sum(len(x) for x in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_treasure:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")