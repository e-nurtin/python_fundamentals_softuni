# Solution # 1
# This is much more complicated IMHO.

# numbers = list(map(int, input().split(', ')))
# indices_of_even = map(lambda x: x if numbers[x] % 2 == 0 else 'no',
#                       range(len(numbers)))
# result = list(filter(lambda a: a != "no", indices_of_even))
# print(result)


# Solution # 2
# Much more readable and easy to understand.
numbers = input()
even_numbers_indexes = []
list_of_numbers = numbers.split(',')
for index, number in enumerate(list_of_numbers):
    if int(number) % 2 == 0:
        even_numbers_indexes.append(index)
print(even_numbers_indexes)
