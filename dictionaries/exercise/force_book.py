def force_add(name, side):
    user_has_side = False
    if side not in force_users.keys():
        force_users[side] = []
    for user in force_users.values():
        if name in user:
            user_has_side = True
    if not user_has_side:
        force_users[side].append(name)


def force_change(name, side):
    user_has_side = False
    if side not in force_users.keys():
        force_users[side] = []
    for current_side, user in force_users.items():
        if name in user:
            user_has_side = True
            user_side = current_side
    if user_has_side:
        force_users[user_side].remove(name)
        force_users[side].append(name)
        print(f"{name} joins the {side} side!")
    else:
        force_users[side].append(name)
        print(f"{name} joins the {side} side!")


force_users = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        side_add, name_add = command.split(" | ")
        force_add(name_add, side_add)
    elif "->" in command:
        name_change, side_change = command.split(" -> ")
        force_change(name_change, side_change)

    command = input()

for force_side in force_users:
    if len(force_users[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(force_users[force_side])}")
        for user in force_users[force_side]:
            print(f"! {user}")
