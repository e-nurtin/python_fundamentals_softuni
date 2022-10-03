count_of_strings = int(input())
special_word = input()
all_strings = []

 # This is my original solution

# strings_with_special_word = []
# for string in range(count_of_strings):
#     current_string = input()
#     all_strings.append(current_string)
#     if special_word in current_string:
#         strings_with_special_word.append(current_string)
# print(all_strings)
# print(strings_with_special_word)

for i in range(count_of_strings):
    current_string = input()
    all_strings.append(current_string)
print(all_strings)

for index in range(len(all_strings) -1, -1, -1):
    element = all_strings[index]
    if special_word not in element:
        all_strings.remove(element)
print(all_strings)

