def is_number_palindrome(number):
    temporary_number = number
    rev_number = 0
    while number > 0:
        last_digit = number % 10
        rev_number = rev_number * 10 + last_digit
        number //= 10
    if rev_number == temporary_number:
        return True
    return False


# list_of_numbers = list(map(int, input().split(", ")))
list_of_numbers = [int(x) for x in input().split(", ")]

for current_number in list_of_numbers:
    print(is_number_palindrome(current_number))

