def heal(current_health, amount_healed):
    if current_health + amount_healed > 100:
        amount_healed = abs(100 - current_health)
        current_health = 100
    else:
        current_health += amount_healed
    print(f"You healed for {amount_healed} hp.")
    print(f"Current health: {current_health} hp.")
    return current_health


def chest_loot(amount_found, current_coins):
    current_coins += amount_found
    print(f"You found {amount_found} bitcoins.")
    return current_coins


def monster(monster_name, attack, our_health):
    our_health -= attack
    if our_health <= 0:
        print(f"You died! Killed by {monster_name}.")
    else:
        print(f"You slayed {monster_name}.")
    return our_health


dungeon_rooms = input().split("|")

health = 100
coins = 0
current_room = 0
killed = False

for room in dungeon_rooms:
    enemy, amount = [int(x) if x.isdigit() else x for x in room.split()]
    current_room += 1

    if enemy == "potion":
        health = heal(health, amount)
    elif enemy == "chest":
        coins = chest_loot(amount, coins)
    else:
        health = monster(enemy, amount, health)
        if health <= 0:
            killed = True
            print(f"Best room: {current_room}")
            break
if not killed:
    print("You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")
