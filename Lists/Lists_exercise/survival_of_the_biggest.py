numbers_as_list = input().split()
count_of_numbers_to_remove = int(input())
# Option 1
# for removal in range(count_of_numbers_to_remove):
#     smallest_number = maxsize
#     for number in numbers_as_list:
#         if int(number) < smallest_number:
#             smallest_number = int(number)
#     numbers_as_list.remove(str(smallest_number))
# Option 2
for removal in range(count_of_numbers_to_remove):
    min_number = min(numbers_as_list)
    numbers_as_list.remove(min_number)
result = ", ".join(numbers_as_list)
print(result)