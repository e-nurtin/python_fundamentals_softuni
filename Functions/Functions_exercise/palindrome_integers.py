# def is_number_palindrome(number):
#     temporary_number = number
#     rev_number = 0
#     while number > 0:
#         last_digit = number % 10
#         rev_number = rev_number * 10 + last_digit
#         number //= 10
#     if rev_number == temporary_number:
#         return True
#     return False
#
#
# # list_of_numbers = list(map(int, input().split(", ")))
# list_of_numbers = [int(x) for x in input().split(", ")]
#
# for current_number in list_of_numbers:
#     print(is_number_palindrome(current_number))

def check_palindrome(num_to_check):
    num_backwards = num_to_check[::-1]
    if num_to_check == num_backwards:
        return True
    return False


number_list = input().split(', ')
result = []

for number in number_list:
    result.append(check_palindrome(number))

# print(*result, sep='\n')
for boolean in result:
    print(boolean)
