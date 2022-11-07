start_range = input()
end_range = input()
string_to_check = input()

start = ord(start_range) + 1
end = ord(end_range)

sum_of_ascii_values = 0

for symbol in range(start, end):
    if chr(symbol) in string_to_check:
        count = string_to_check.count(chr(symbol))
        sum_of_ascii_values += (symbol * count)

print(sum_of_ascii_values)
