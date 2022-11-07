numbers_as_list = input().split()
count_of_numbers_to_remove = int(input())
# Option 1
for removal in range(count_of_numbers_to_remove):
    smallest_number = 651651959

    for number in numbers_as_list:
        if int(number) < smallest_number:
            smallest_number = int(number)
    numbers_as_list.remove(str(smallest_number))

result = ", ".join(numbers_as_list)
print(result)

# Option 2
numbers_as_list = list(map(int, input().split()))
count_of_numbers_to_remove = int(input())

for removal in range(count_of_numbers_to_remove):
    numbers_as_list.remove(min(numbers_as_list))

print(*numbers_as_list, sep=", ")