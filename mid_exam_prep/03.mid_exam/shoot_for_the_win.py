def shoot_a_target(index_to_shoot, count_of_targets: int):
    if len(targets_to_shoot) > index_to_shoot:
        if targets_to_shoot[index_to_shoot] > -1:
            value_of_target = targets_to_shoot[index_to_shoot]
            targets_to_shoot[index_to_shoot] = -1
            count_of_targets += 1
            correct_values(value_of_target)
    return count_of_targets


def correct_values(last_target_value):
    for target in range(len(targets_to_shoot)):
        if -1 < targets_to_shoot[target] > last_target_value:
            targets_to_shoot[target] -= last_target_value
        elif -1 < targets_to_shoot[target] <= last_target_value:
            targets_to_shoot[target] += last_target_value


targets_to_shoot = list(map(int, input().split()))

count_of_shot_targets = 0
command = input()
while command != "End":
    index = int(command)
    count_of_shot_targets = shoot_a_target(index, count_of_shot_targets)

    command = input()

print(f"Shot targets: {count_of_shot_targets} ->", *targets_to_shoot, sep=' ')
