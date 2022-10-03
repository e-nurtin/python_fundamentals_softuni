original_list = input().split()

command_list = input().split()
while "end" not in command_list:
    current_command = command_list[0]
    first_value = command_list[1]
    manipulated_list = []
    first_half = []
    max_number = -1
    min_number = 1000

    if current_command == "exchange":
        if 0 <= int(first_value) < len(
                original_list):
            for index, number in enumerate(original_list):
                if index > int(first_value):
                    manipulated_list.append(number)
                else:
                    first_half.append(number)
            original_list = manipulated_list + first_half
        else:
            print("Invalid index")
    elif current_command == "max":
        if first_value == "even":
            for index, number in enumerate(original_list):
                current_number = int(number)
                if current_number % 2 == 0:
                    if current_number >= max_number:
                        max_number = int(number)
            if str(max_number) in original_list:
                max_number = -(original_list[::-1].index(max_number) + 1)
                print(max_number)
            else:
                print("No matches")
        elif first_value == "odd":
            for index, number in enumerate(original_list):
                current_number = int(number)
                if current_number % 2 != 0:
                    if current_number >= max_number:
                        max_number = int(number)
            if str(max_number) in original_list:
                max_number = -(original_list[::-1]).index()
                print(max_number)
            else:
                print("No matches")
    elif current_command == "min":
        if first_value == "even":
            for index, number in enumerate(original_list):
                current_number = int(number)
                if current_number % 2 == 0:
                    if current_number <= min_number:
                        min_number = int(number)
            if str(min_number) in original_list:
                for index, word in enumerate(original_list):
                    if str(min_number) == word:
                        min_number = index
                print(min_number)
            else:
                print("No matches")
        elif first_value == "odd":
            for index, number in enumerate(original_list):
                current_number = int(number)
                if current_number % 2 != 0:
                    if current_number <= min_number:
                        min_number = int(number)
            if str(min_number) in original_list:
                for index, word in enumerate(original_list):
                    if str(min_number) == word:
                        min_number = index
                print(min_number)
            else:
                print("No matches")
    elif current_command == "first":
        second_value = command_list[2]
        if int(first_value) <= len(original_list):
            if second_value == "even":
                for number in original_list:
                    if int(number) % 2 == 0:
                        manipulated_list.append(int(number))
            elif second_value == "odd":
                for number in original_list:
                    if int(number) % 2 != 0:
                        manipulated_list.append(int(number))
            if len(manipulated_list) > int(first_value):
                print(manipulated_list[:(int(first_value))])
            else:
                print(manipulated_list)
        else:
            print("Invalid count")
    elif current_command == "last":
        second_value = command_list[2]
        if int(first_value) <= len(original_list):
            if second_value == "even":
                for number in original_list:
                    if int(number) % 2 == 0:
                        manipulated_list.append(int(number))
            elif second_value == "odd":
                for number in original_list:
                    if int(number) % 2 != 0:
                        manipulated_list.append(int(number))
            if len(manipulated_list) >= int(first_value):
                print(manipulated_list[-(int(first_value))])
            else:
                print(manipulated_list)
        else:
            print("Invalid count")
    command_list = input().split()
final_list = []
for number in original_list:
    final_list.append(int(number))
print(final_list)