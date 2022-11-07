# first_string, second_string = input().split()
# total_ascii_sum = 0
# leftover_string = ""
# if len(first_string) > len(second_string):
#     leftover_string = first_string[len(second_string):]
#     first_string = first_string[:len(second_string)]
# elif len(second_string) > len(first_string):
#     leftover_string = second_string[len(first_string):]
#     second_string = second_string[:len(first_string)]
#
# for index in range(len(first_string)):
#     total_ascii_sum += (ord(first_string[index]) * ord(second_string[index]))
#
# for letter in leftover_string:
#     total_ascii_sum += ord(letter)
#
# print(total_ascii_sum)


def find_longer_string(first_str, second_str):
    longer_str = second_str
    short_str = first_str
    if len(first_str) > len(second_str):
        longer_str = first_str
        short_str = second_str
    return longer_str, short_str


def sum_ascii_values(short_str, long_str, total):
    for index in range(len(long_str)):
        # Check if index is in range of the shorter string and multiply if it is.
        if len(short_str) > index:
            total += ord(long_str[index]) * ord(short_str[index])
        # If index not in range of short string, add the remaining numbers.
        else:
            total += ord(long_str[index])
    return total


first_string, second_string = input().split()
total_ascii_sum = 0

long_string, short_sting = find_longer_string(first_string, second_string)
total_ascii_sum = sum_ascii_values(short_sting, long_string, total_ascii_sum)

print(total_ascii_sum)
