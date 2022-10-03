def factorial_number(number: int):
    factorial_n = 1
    count = 0
    while count < number:
        count += 1
        factorial_n *= count
    return factorial_n


first_number = int(input())
second_number = int(input())

result = factorial_number(first_number) / factorial_number(second_number)
print(f"{result:.2f}")
