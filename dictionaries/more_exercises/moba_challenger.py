def add_player(name, lane, points, data):
    if name not in data:
        data[name] = {}
        total_points[name] = 0
    if lane not in data[name]:
        data[name][lane] = 0
    if data[name][lane] < points:
        total_points[name] += points - data[name][lane]
        data[name][lane] = points


def duel(player_1, player_2):
    if player_1 in data and player_2 in data:
        player_2_keys = list(data[player_2].keys())
        for position, skills in data[player_1].items():
            if position in player_2_keys:
                if total_points[player_1] > total_points[player_2]:
                    del total_points[player_2]
                    del data[player_2]
                    break
                elif total_points[player_1] < total_points[player_2]:
                    del total_points[player_1]
                    del data[player_1]
                    break


total_points = {}
data = {}

command = input()
while command != "Season end":

    if 'vs' in command:
        player_one, player_two = command.split(' vs ')

        duel(player_one, player_two)

    else:
        player, position, skill_points = [int(x) if x.isdigit() else x for x
                                          in command.split(' -> ')]

        add_player(player, position, skill_points, data)

    command = input()

sort_total = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))
for player, total_skills in sort_total.items():
    print(f"{player}: {total_skills} skill")

    sort_skills = dict(sorted(data[player].items(), key=lambda x:(-x[1], x[0])))
    for role, skill in sort_skills.items():
        print(f"- {role} <::> {skill}")


data['Peter'].get('l', 0)



print(data)