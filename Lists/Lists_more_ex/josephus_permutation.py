list_of_people = input().split()
step = int(input()) - 1
person_to_execute = step
execution_order = []
while len(list_of_people) > 0:
    for number in range(len(list_of_people)):
        if person_to_execute < len(list_of_people):
            execution_order.append(int(list_of_people.pop(
                person_to_execute)))
            person_to_execute += step
        if person_to_execute >= len(list_of_people):
            person_to_execute = abs(person_to_execute - len(list_of_people))
print("[", end="")
print(*execution_order, sep=",", end="")
print("]")
