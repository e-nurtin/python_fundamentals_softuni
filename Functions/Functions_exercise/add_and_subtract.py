def sum_numbers(a, b):
    return a + b


def subtract(sum_result, c):
    return sum_result - c


def add_and_subtract(one, two, three):
    sum_of_first_two = sum_numbers(one, two)
    result = subtract(sum_of_first_two, three)
    return print(result)


number_one = int(input())
number_two = int(input())
number_three = int(input())

add_and_subtract(number_one, number_two, number_three)