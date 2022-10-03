def check_for_free_space(people_to_lift):
    for index in range(len(wagons_on_lift)):
        while wagons_on_lift[index] < 4:
            wagons_on_lift[index] += 1
            people_to_lift -= 1
            if people_to_lift == 0:
                break
        if people_to_lift == 0:
            break
    return people_to_lift


def lift_has_empty_spaces():
    for wagon in wagons_on_lift:
        if wagon < 4:
            return True
    return False


people_waiting_for_lift = int(input())
wagons_on_lift = list(map(int, input().split()))

result = check_for_free_space(people_waiting_for_lift)

if result == 0 and lift_has_empty_spaces():
    print(f"The lift has empty spots!")
    print(*wagons_on_lift, sep=" ")
elif result > 0:
    print(f"There isn't enough space! {result} people in a queue!")
    print(*wagons_on_lift, sep=" ")
elif not lift_has_empty_spaces():
    print(*wagons_on_lift, sep=" ")