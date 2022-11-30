def pick_heroes(count):
    for i in range(count):
        name, hp, mp = input().split()
        # HP is on index 0 and MP on 1
        data[name] = [int(hp), int(mp)]
    return data


def cast_spell(name, mp_need, spell):
    if data[name][1] >= mp_need:
        data[name][1] -= mp_need
        return f"{name} has successfully cast {spell} and now has {data[name][1]} MP!"
    return f"{name} does not have enough MP to cast {spell}!"


def take_damage(name, damage, attacker):
    data[name][0] -= damage
    if data[name][0] > 0:
        return f"{name} was hit for {damage} HP by {attacker} and now has " \
               f"{data[name][0]} HP left!"
    del data[name]
    return f"{name} has been killed by {attacker}!"


def recharge(name, amount):
    data[name][1] += amount
    if data[name][1] > 200:
        amount -= (data[name][1] - 200)
        data[name][1] = 200
    return f"{name} recharged for {amount} MP!"


def heal(name, amount):
    data[name][0] += amount
    if data[name][0] > 100:
        amount -= (data[name][0] - 100)
        data[name][0] = 100
    return f"{name} healed for {amount} HP!"


def game_on(hero_data):
    command = input()
    while command != "End":
        action, name, *info = [int(x) if x.isdigit() else x for x in command.split(' - ')]

        if action == "CastSpell":
            print(cast_spell(name, info[0], info[1]))

        elif action == "TakeDamage":
            print(take_damage(name, info[0], info[1]))

        elif action == "Recharge":
            print(recharge(name, info[0]))

        elif action == "Heal":
            print(heal(name, info[0]))

        command = input()
    return hero_data


data = {}
count_of_heroes = int(input())

pick_heroes(count_of_heroes)
data = game_on(data)

for hero, hp_mp in data.items():
    print(f"{hero}")
    print(f"HP: {hp_mp[0]}")
    print(f"MP: {hp_mp[1]}")

# def cast_spell(hero, mp_needed, spell, mp_d):
#     if data[hero][mp_d] >= mp_needed:
#         data[hero][mp_d] -= mp_needed
#         return f"{hero} has successfully cast {spell} and now has {data[hero][mp_d]} MP!"
#     else:
#         return f"{hero} does not have enough MP to cast {spell}!"
#
#
# def take_damage(hero, damage, attacker, hp_d):
#     data[hero][hp_d] -= damage
#     if data[hero][hp_d] > 0:
#         return f"{hero} was hit for {damage} HP by {attacker} and now has {data[hero][hp_d]} HP left!"
#     elif data[hero][hp_d] <= 0:
#         del data[hero]
#         return f"{hero} has been killed by {attacker}!"
#
#
# def recharge(hero, amount, mp_d):
#     max_mp = 200
#     if data[hero][mp_d] + amount > max_mp:
#         amount = max_mp - data[hero][mp_d]
#     data[hero][mp_d] += amount
#     return f"{hero} recharged for {amount} MP!"
#
#
# def heal(hero, amount, hp_d):
#     max_hp = 100
#     if data[hero][hp_d] + amount > max_hp:
#         amount = max_hp - data[hero][hp_d]
#     data[hero][hp_d] += amount
#     return f"{hero} healed for {amount} HP!"
#
#
# data = {}
# hp_d = 'hp'
# mp_d = 'mp'
#
# count_of_heroes = int(input())
#
# for i in range(count_of_heroes):
#     name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
#
#     data[name] = {}
#     data[name][hp_d] = hp
#     data[name][mp_d] = mp
#
# command = input()
#
# while command != "End":
#     action, hero_name, *info = command.split(' - ')
#
#     if action == "CastSpell":
#         mp_needed = int(info[0])
#         spell_name = info[1]
#         print(cast_spell(hero_name, mp_needed, spell_name, mp_d))
#     elif action == "TakeDamage":
#         damage = int(info[0])
#         attacker = info[1]
#         print(take_damage(hero_name, damage, attacker, hp_d))
#     elif action == "Recharge":
#         amount = int(info[0])
#         print(recharge(hero_name, amount, mp_d))
#     elif action == "Heal":
#         amount = int(info[0])
#         print(heal(hero_name, amount, hp_d))
#
#     command = input()
#
# for hero, info in data.items():
#     print(f"{hero}")
#     print(f"  HP: {info[hp_d]}")
#     print(f"  MP: {info[mp_d]}")
