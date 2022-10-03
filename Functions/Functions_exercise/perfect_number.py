def positive_divisors(number):
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor
    sum_of_divisors += number
    if sum_of_divisors / 2 == number:
        return "We have a perfect number!"
    return "It's not so perfect."


perfect_number = int(input())

print(positive_divisors(perfect_number))