# def force_add(name, side):
#     user_has_side = False
#     if side not in force_users.keys():
#         force_users[side] = []
#     for user in force_users.values():
#         if name in user:
#             user_has_side = True
#     if not user_has_side:
#         force_users[side].append(name)
#
#
# def force_change(name, side):
#     user_has_side = False
#     if side not in force_users.keys():
#         force_users[side] = []
#     for current_side, user in force_users.items():
#         if name in user:
#             user_has_side = True
#             user_side = current_side
#     if user_has_side:
#         force_users[user_side].remove(name)
#         force_users[side].append(name)
#         print(f"{name} joins the {side} side!")
#     else:
#         force_users[side].append(name)
#         print(f"{name} joins the {side} side!")
#
#
# force_users = {}
# command = input()
# while command != "Lumpawaroo":
#     if "|" in command:
#         side_add, name_add = command.split(" | ")
#         force_add(name_add, side_add)
#     elif "->" in command:
#         name_change, side_change = command.split(" -> ")
#         force_change(name_change, side_change)
#
#     command = input()
#
# for force_side in force_users:
#     if len(force_users[force_side]) > 0:
#         print(f"Side: {force_side}, Members: {len(force_users[force_side])}")
#         for user in force_users[force_side]:
#             print(f"! {user}")

def check_user(force_side, user):
    if force_side not in data:
        data[force_side] = []
    for key, values in data.items():
        if user in values:
            return
    data[force_side].append(user)


def change_side(force_side, user):
    user_has_side = ''
    if force_side not in data:
        data[force_side] = []
    for key, values in data.items():
        if user in values:
            user_has_side = key
            break
    if user_has_side:
        data[user_has_side].remove(user)
    data[force_side].append(user)
    return f"{user} joins the {force_side} side!"


data = {}

command = input()

while command != "Lumpawaroo":
    if '|' in command:
        side, force_user = command.split(' | ')
        check_user(side, force_user)

    elif '->' in command:
        force_user, side = command.split(' -> ')
        print(change_side(side, force_user))

    command = input()

for side, members in data.items():
    if len(data[side]) > 0:
        print(f"Side: {side}, Members: {len(data[side])}")
        for member in members:
            print(f"! {member}")

