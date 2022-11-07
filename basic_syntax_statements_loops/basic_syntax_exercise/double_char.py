# current_command = input()
#
# while current_command != "End":
#     new_double_char_string = ""
#     if current_command == "SoftUni":
#         current_command = input()
#         continue
#     else:
#         for i in current_command:
#             new_double_char_string += i + i
#
#     print(new_double_char_string)
#     current_command = input()

string = input()
while string != "End":
    new_string = ""
    if string != "SoftUni":
        for character in string:
            new_string += character * 2
        print(new_string)
    string = input()