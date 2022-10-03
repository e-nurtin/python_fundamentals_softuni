# string_of_numbers = input()
#
# numbers_as_list = list(string_of_numbers.split(" "))
# final_numbers = []
# for number in numbers_as_list:
#     result = int(number) * - 1
#     final_numbers.append(result)
# print(final_numbers)

list_of_numbers = input().split()
opposite_numbers = []
for element in list_of_numbers:
    opposite_numbers.append(-int(element))
print(opposite_numbers)