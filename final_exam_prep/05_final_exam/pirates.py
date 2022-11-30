def update_city(town, people, money, people_d, money_d):
    if town not in data:
        data[town] = {}
        data[town][people_d] = 0
        data[town][money_d] = 0
    data[town][people_d] += people
    data[town][money_d] += money


def plunder(town, people, money, people_d, money_d):
    data[town][people_d] -= people
    data[town][money_d] -= money
    print(f"{town} plundered! {money} gold stolen, {people} citizens killed.")
    if data[town][people_d] <= 0 or data[town][money_d] <= 0:
        del data[town]
        print(f"{town} has been wiped off the map!")


def prosper(town, money, money_d):
    if money < 0:
        print("Gold added cannot be a negative number!")
        return
    data[town][money_d] += money
    print(f"{money} gold added to the city treasury. {town} now has {data[town][money_d]} gold.")


data = {}
population_d = 'population'
gold_d = 'gold'

command = input()
while command != "Sail":
    city, population, gold = [int(x) if x.isdigit() else x for x in command.split('||')]
    update_city(city, population, gold, population_d, gold_d)
    command = input()

command = input()
while command != "End":
    action, city, *info = command.split('=>')

    if action == "Plunder":
        plunder(city, int(info[0]), int(info[1]), population_d, gold_d)
    elif action == "Prosper":
        prosper(city, int(info[0]), gold_d)

    command = input()
if data:
    print(f"Ahoy, Captain! There are {len(data)} wealthy settlements to go to:")
    for town, info in data.items():
        print(f"{town} -> Population: {info[population_d]} citizens, Gold: {info[gold_d]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")