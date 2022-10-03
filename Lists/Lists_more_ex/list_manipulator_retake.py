initial_list = [int(x) for x in input().split()]
commands_list = input().split()

while "end" not in commands_list:
    first_value = commands_list[1]
    current_command = commands_list[0]

    even_numbers = [x for x in initial_list if x % 2 == 0]
    odd_numbers = [x for x in initial_list if x % 2 != 0]

    if current_command == "exchange":
        if 0 <= int(first_value) < len(initial_list):
            initial_list = initial_list[int(first_value) + 1:] + \
                           initial_list[:int(first_value) + 1]
        else:
            print("Invalid index")
    elif current_command == "max":
        if first_value == "odd" and odd_numbers:
            print(len(initial_list) - initial_list[::-1].index(max(
                odd_numbers)) - 1)
        elif first_value == "even" and even_numbers:
            print(len(initial_list) - initial_list[::-1].index(max(
                even_numbers)) - 1)
        else:
            print("No matches")

    elif current_command == "min":
        if first_value == "odd" and odd_numbers:
            print(len(initial_list) - initial_list[::-1].index(min(
                odd_numbers)) - 1)
        elif first_value == "even" and even_numbers:
            print(len(initial_list) - initial_list[::-1].index(min(
                even_numbers)) - 1)
        else:
            print("No matches")

    elif current_command == "first":
        if int(first_value) <= len(initial_list):
            if commands_list[2] == "odd":
                print(odd_numbers[:int(first_value)])
            elif commands_list[2] == "even":
                print(even_numbers[:int(first_value)])
        else:
            print("Invalid count")
    elif current_command == "last":
        if int(first_value) <= len(initial_list):
            if commands_list[2] == "odd":
                print(odd_numbers[-int(first_value):])
            elif commands_list[2] == "even":
                print(even_numbers[-int(first_value):])
        else:
            print("Invalid count")
    commands_list = input().split()
print(initial_list)
