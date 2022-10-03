list_of_racer_times = input().split()
left_racer = list_of_racer_times[:len(list_of_racer_times) // 2]
finish_line = list_of_racer_times[len(left_racer):len(left_racer) + 1]
right_racer = list_of_racer_times[:len(left_racer): -1]
left_racer_time = 0
right_racer_time = 0

for race in left_racer:
    if int(race) > 0:
        left_racer_time += int(race)
    else:
        left_racer_time *= 0.8
for race in right_racer:
    if int(race) > 0:
        right_racer_time += int(race)
    else:
        right_racer_time *= 0.8
if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
