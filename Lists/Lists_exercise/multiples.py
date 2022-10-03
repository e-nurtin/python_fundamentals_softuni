factor_number = int(input())
count_of_multiplies = int(input())
current_number = 0
list_of_multiplied_numbers = []
for current_factor in range(1, count_of_multiplies + 1):
    current_number = current_factor * factor_number
    list_of_multiplied_numbers.append(current_number)
print(list_of_multiplied_numbers)
