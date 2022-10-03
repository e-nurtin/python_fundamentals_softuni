sequence_of_numbers = input().split()
initial_string = input()
message = ""
list_of_characters_on_string = []
for character in initial_string:
    list_of_characters_on_string.append(character)
for current_number in sequence_of_numbers:
    sum_of_current_index = 0
    for current_digit in current_number:
        sum_of_current_index += int(current_digit)
    if sum_of_current_index >= len(list_of_characters_on_string):
        sum_of_current_index -= len(list_of_characters_on_string)
    message += list_of_characters_on_string.pop(sum_of_current_index)
print(message)