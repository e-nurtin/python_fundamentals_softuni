def swap_elements(index_1, index_2):
    initial_list[index_1], initial_list[index_2] = \
        initial_list[index_2], initial_list[index_1]


def multiply(index_1, index_2):
    initial_list[index_1] *= initial_list[index_2]


def decrease_value():
    for number in range(len(initial_list)):
        initial_list[number] -= 1


initial_list = list(map(int, input().split()))
command = input()

while command != "end":

    action, *info = [int(x) if x.isdigit() else x for x in command.split()]

    if action == "swap":
        swap_elements(info[0], info[1])
    elif action == "multiply":
        multiply(info[0], info[1])
    elif action == "decrease":
        decrease_value()

    command = input()

print(*initial_list, sep=", ")