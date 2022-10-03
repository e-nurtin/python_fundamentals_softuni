def shoot(index_to_shoot, power):
    if 0 <= index_to_shoot < len(targets_to_shoot):
        targets_to_shoot[index_to_shoot] -= power
        if targets_to_shoot[index_to_shoot] <= 0:
            del targets_to_shoot[index_to_shoot]


def add_target(index_to_add, value_to_add):
    if 0 <= index_to_add < len(targets_to_shoot):
        targets_to_shoot.insert(index_to_add, value_to_add)
    else:
        print("Invalid placement!")


def strike(index_strike, radius_of_strike):
    start_index = index_strike - radius_of_strike
    finish_index = index_strike + radius_of_strike + 1
    if 0 <= start_index < len(targets_to_shoot) and\
            start_index < finish_index <= len(targets_to_shoot):
        del targets_to_shoot[start_index:finish_index]
    else:
        print("Strike missed!")


targets_to_shoot = list(map(int, input().split()))
command = input()
while command != "End":
    action, index, value = [x if x.isalpha() else int(x) for x in
                            command.split()]

    if action == "Shoot":
        shoot(index, value)
    elif action == "Add":
        add_target(index, value)
    elif action == "Strike":
        strike(index, value)

    command = input()
print(*targets_to_shoot, sep="|")
