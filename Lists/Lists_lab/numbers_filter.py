count_of_numbers = int(input())

all_numbers = []
for i in range(count_of_numbers):
    current_number = int(input())
    all_numbers.append(current_number)

current_command = input()
filtered = []
if current_command == "even":
    for number in all_numbers:
        if number % 2 == 0:
            filtered.append(number)
elif current_command == "odd":
    for number in all_numbers:
        if number % 2 != 0:
            filtered.append(number)
elif current_command == "negative":
    for number in all_numbers:
        if number < 0:
            filtered.append(number)
elif current_command == "positive":
    for number in all_numbers:
        if number >= 0:
            filtered.append(number)
print(filtered)
