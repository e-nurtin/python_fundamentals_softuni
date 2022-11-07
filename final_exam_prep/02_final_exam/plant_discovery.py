def rate(name, rating, rate_):
    if name in data:
        data[name][rate_].append(rating)
    else:
        print("error")


def update(name, new_rarity, rarity_):
    if name in data:
        data[name][rarity_] = new_rarity
    else:
        print("error")


def reset(name, rate_):
    if name in data:
        data[name][rate_] = []
    else:
        print("error")


data = {}
rate_d = 'rating'
rarity_d = 'rarity'
avg_rating = 0
count_of_info_lines = int(input())

for i in range(count_of_info_lines):
    plant, rarity = input().split('<->')
    data[plant] = {}
    data[plant][rarity_d] = rarity
    data[plant][rate_d] = []

command = input()
while command != "Exhibition":
    action, *info = [int(x) if x.isdigit() else x for x in command.split()]

    if action == "Rate:":
        rate(info[0], info[2], rate_d)
    elif action == "Update:":
        update(info[0], info[2], rarity_d)
    elif action == "Reset:":
        reset(info[0], rate_d)

    command = input()

print(f"Plants for the exhibition:")
for plant, info in data.items():

    if len(info[rate_d]) > 0:
        avg_rating = sum(info[rate_d]) / len(info[rate_d])

    print(f"- {plant}; Rarity: {info[rarity_d]}; Rating: {avg_rating:.2f}")
