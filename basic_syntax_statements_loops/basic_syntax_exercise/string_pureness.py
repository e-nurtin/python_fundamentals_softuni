count_of_strings = int(input())

for string in range(count_of_strings):
    current_string = input()
    string_is_pure = True
    for i in current_string:
        if i == "," or i == '.' or i == "_":
            string_is_pure = False
    if string_is_pure:
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")
