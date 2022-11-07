# first_number = int(input())
# second_number = int(input())
# divider_number = int(input())
# multiplier_number = int(input())
#
# added_numbers = first_number + second_number
# divided_numbers = added_numbers // divider_number
# final_number = int(divided_numbers * multiplier_number)
#
# print(final_number)

numbers = [int(input()) for i in range(4)]
result = ((numbers[0] + numbers[1]) // numbers[2]) * numbers[3]
print(result)