data = {}
hat_d = 'hat'
physic_d = 'physic'
hat_len = 'len'
names_d = 'name'

command = input()
while command != "Once upon a time":
    name, color, physic = [int(x) if x.isdigit() else x for x in
                           command.split(" <:> ")]

    if color not in data:
        data[color] = {}
    if name not in data[color]:
        data[color][name] = physic
    if color in data and name in data[color]:
        if data[color][name] < physic:
            data[color][name] = physic

    command = input()

list_for_sorting = []

for hat in data:
    for name, value in data[hat].items():
        list_for_sorting.append(
            {hat_len: len(data[hat]), names_d: name, physic_d:
                value, hat_d: hat})

sorted_list = sorted(list_for_sorting, key=lambda x: (-x[physic_d], -x[hat_len]))

for item in sorted_list:
    print(f"({item[hat_d]}) {item[names_d]} <-> {item[physic_d]}")
