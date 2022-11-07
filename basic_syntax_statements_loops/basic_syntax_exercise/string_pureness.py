# count_of_strings = int(input())
#
# for string in range(count_of_strings):
#     current_string = input()
#     string_is_pure = True
#     for i in current_string:
#         if i == "," or i == '.' or i == "_":
#             string_is_pure = False
#     if string_is_pure:
#         print(f"{current_string} is pure.")
#     else:
#         print(f"{current_string} is not pure!")


count_of_strings = int(input())
forbidden_symbols = [',', '.', '_']
for i in range(count_of_strings):
    current_string = input()
    if any(x in current_string for x in forbidden_symbols):
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")