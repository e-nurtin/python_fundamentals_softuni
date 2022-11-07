def cast_spell(hero, mp_needed, spell, mp_d):
    if data[hero][mp_d] >= mp_needed:
        data[hero][mp_d] -= mp_needed
        print(f"{hero} has successfully cast {spell} and now has {data[hero][mp_d]} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")


def take_damage(hero, damage, attacker, hp_d):
    data[hero][hp_d] -= damage
    if data[hero][hp_d] > 0:
        print(
            f"{hero} was hit for {damage} HP by {attacker} and now has {data[hero][hp_d]} HP left!")
    elif data[hero][hp_d] <= 0:
        print(f"{hero} has been killed by {attacker}!")
        del data[hero]


def recharge(hero, amount, mp_d):
    max_mp = 200
    if data[hero][mp_d] + amount > max_mp:
        amount = max_mp - data[hero][mp_d]
    data[hero][mp_d] += amount
    print(f"{hero} recharged for {amount} MP!")


def heal(hero, amount, hp_d):
    max_hp = 100
    if data[hero][hp_d] + amount > max_hp:
        amount = max_hp - data[hero][hp_d]
    data[hero][hp_d] += amount
    print(f"{hero} healed for {amount} HP!")


data = {}
hp_d = 'hp'
mp_d = 'mp'

count_of_heroes = int(input())

for i in range(count_of_heroes):
    name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]

    data[name] = {}
    data[name][hp_d] = hp
    data[name][mp_d] = mp

command = input()

while command != "End":
    action, hero_name, *info = command.split(' - ')

    if action == "CastSpell":
        mp_needed = int(info[0])
        spell_name = info[1]
        cast_spell(hero_name, mp_needed, spell_name, mp_d)
    elif action == "TakeDamage":
        damage = int(info[0])
        attacker = info[1]
        take_damage(hero_name, damage, attacker, hp_d)
    elif action == "Recharge":
        amount = int(info[0])
        recharge(hero_name, amount, mp_d)
    elif action == "Heal":
        amount = int(info[0])
        heal(hero_name, amount, hp_d)

    command = input()

for hero, info in data.items():
    print(f"{hero}")
    print(f"  HP: {info[hp_d]}")
    print(f"  MP: {info[mp_d]}")
