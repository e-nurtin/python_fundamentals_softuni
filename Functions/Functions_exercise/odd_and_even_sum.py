def odd_and_even_sum(numbers: str):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0

    for n in numbers:
        if int(n) % 2 == 0:
            sum_of_even_digits += int(n)
        else:
            sum_of_odd_digits += int(n)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

number = input()

print(odd_and_even_sum(number))