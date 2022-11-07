def add_username(data, name, contest, points, points_by_user):
    if name not in data[contest]:
        data[contest][name] = points
        points_by_user[name] += points
    elif data[contest][name] < points:
        total_points_by_user[name] += points - data[contest][name]
        data[contest][name] = points
    return data, points_by_user


data = {}
total_points_by_user = {}

command = input()
while command != "no more time":
    username, contest, points = [int(x) if x.isdigit() else x for x in
                                 command.split(' -> ')]
    if contest not in data:
        data[contest] = {}
    if username not in total_points_by_user:
        total_points_by_user[username] = 0

    data, total_points_by_user = add_username(data, username, contest, points,
                                              total_points_by_user)

    command = input()

for topic, values in data.items():
    print(f"{topic}: {len(values)} participants")
    ordered = dict(sorted(values.items(), key=lambda x: (-x[1], x[0])))
    for index, (name, points) in enumerate(ordered.items(), 1):
        print(f"{index}. {name} <::> {points}")

print("Individual standings:")

ordered = dict(
    sorted(total_points_by_user.items(), key=lambda x: (-x[1], x[0])))
for index, (name, total_points) in enumerate(ordered.items(), 1):
    print(f"{index}. {name} -> {total_points}")
