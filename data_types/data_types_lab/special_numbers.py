number = int(input())

for current_number in range(1, number + 1):
    # sum_of_digits = 0
    # digits = current_number
    # while digits > 0:
    #     sum_of_digits += digits % 10
    #     digits = int(digits / 10)
    # if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
    #     print(f"{current_number} -> True")
    # else:
    #     print(f"{current_number} -> False")
    sum_of_digits = 0
    number_as_string = str(current_number)
    for i in number_as_string:
        n = int(i)
        sum_of_digits += n
    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")