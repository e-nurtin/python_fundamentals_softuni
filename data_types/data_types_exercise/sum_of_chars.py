number_of_chars = int(input())
current_char_as_ascii_char = 0
total_number = 0
for i in range(number_of_chars):
    current_char = input()

    current_char_as_ascii_char = ord(current_char)
    total_number += current_char_as_ascii_char
print(f"The sum equals: {total_number}")
