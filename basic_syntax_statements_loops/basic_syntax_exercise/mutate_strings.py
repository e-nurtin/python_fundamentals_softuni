first_string = input()
second_string = input()

for current_index in range(len(first_string)):
    if second_string[current_index] != first_string[current_index]:
        first_string = second_string[:current_index + 1] + first_string[
            current_index + 1:]
        print(first_string)