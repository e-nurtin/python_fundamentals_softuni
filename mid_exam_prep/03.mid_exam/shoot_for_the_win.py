def shoot_a_target(index_to_shoot, count_of_targets: int):
    if len(targets_to_shoot) > index_to_shoot:
        if targets_to_shoot[index_to_shoot] > -1:
            value_of_target = targets_to_shoot[index_to_shoot]
            targets_to_shoot[index_to_shoot] = -1
            count_of_targets = shot_targets(count_of_targets)
            correct_values(value_of_target)
    return count_of_targets


def shot_targets(count_of_targets: int):
    count_of_targets += 1
    return count_of_targets


def correct_values(value):
    for target in range(len(targets_to_shoot)):
        if -1 < targets_to_shoot[target] > value:
            targets_to_shoot[target] -= value
        elif -1 < targets_to_shoot[target] <= value:
            targets_to_shoot[target] += value


targets_to_shoot = list(map(int, input().split()))

count_of_shot_targets = 0
command = input()
while command != "End":
    index_to_shoot = int(command)
    count_of_shot_targets = shoot_a_target(index_to_shoot,
                                           count_of_shot_targets)

    command = input()

print(f"Shot targets: {count_of_shot_targets} ->", *targets_to_shoot, sep=' ')
