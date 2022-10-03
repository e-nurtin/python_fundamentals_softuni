initial_string = input()
list_of_numbers = [int(x) for x in initial_string if x.isdigit()]
list_of_characters = [x for x in initial_string if not x.isdigit()]
# take_list = [element for index, element in enumerate(list_of_numbers)
#              if index % 2 == 0]
# skip_list = [element for index, element in enumerate(list_of_numbers)
#              if index % 2 != 0]
result = ""
for index, digit in enumerate(list_of_numbers):
    if index % 2 == 0:
        result += ''.join(list_of_characters[:list_of_numbers[index]])
        list_of_characters = list_of_characters[list_of_numbers[index]:]
    if index % 2 != 0:
        list_of_characters = list_of_characters[list_of_numbers[index]:]

print(result)
