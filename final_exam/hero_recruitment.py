def check_hero(name):
    if name in data:
        return True
    return False


def check_spell(hero_name, spell_name):
    if spell_name in data[hero_name]:
        return True
    return False


def enroll_hero(name):
    if check_hero(name):
        print(f"{name} is already enrolled.")
    else:
        data[name] = []


def learn_spell(name, spell):
    if not check_hero(name):
        print(f"{name} doesn't exist.")
    elif check_spell(name, spell):
        print(f"{name} has already learnt {spell}.")
    else:
        data[name].append(spell)


def unlearn_spell(name, spell):
    if not check_hero(name):
        print(f"{name} doesn't exist.")
    elif not check_spell(name, spell):
        print(f"{name} doesn't know {spell}.")
    else:
        data[name].remove(spell)


data = {}
command = input()

while command != "End":
    action, *info = command.split()

    if action == "Enroll":
        enroll_hero(info[0])
    elif action == "Learn":
        learn_spell(info[0], info[1])
    elif action == "Unlearn":
        unlearn_spell(info[0], info[1])

    command = input()

print("Heroes:")
for hero, spells in data.items():
    print(f"== {hero}: {', '.join(spells)}")
