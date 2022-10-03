list_of_numbers = input().split(", ")
ordered_integers = []
for number in list_of_numbers:
    if number == "0":
        list_of_numbers.remove(number)
        list_of_numbers.append("0")
for n in list_of_numbers:
    ordered_integers.append(int(n))
print(ordered_integers)