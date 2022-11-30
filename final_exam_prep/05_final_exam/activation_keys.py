def check_substring(substr, key):
    if substr in key:
        return f"{key} contains {substr}"
    return "Substring not found!"


def flip_case(key, letter_case, start, end):
    if letter_case == 'Lower':
        key = key[:start] + key[start:end].lower() + key[end:]
    elif letter_case == 'Upper':
        key = key[:start] + key[start:end].upper() + key[end:]
    return key


def slice_key(key, start, end):
    key = key[:start] + key[end:]
    return key


raw_key = input()

while True:
    command = input()

    if command == "Generate":
        print(f"Your activation key is: {raw_key}")
        break

    elif "Contains" in command:
        action, substring = command.split('>>>')
        print(check_substring(substring, raw_key))

    elif "Flip" in command:
        action, case, start_index, end_index = [int(x) if x.isdigit() else
                                                x for x in command.split('>>>')]
        raw_key = flip_case(raw_key, case, start_index, end_index)
        print(raw_key)

    elif "Slice" in command:
        action, start_index, end_index = [int(x) if x.isdigit()
                                          else x for x in command.split('>>>')]
        raw_key = slice_key(raw_key, start_index, end_index)
        print(raw_key)


# def flip_or_slice(key, info, action):
#
#     if action == "Flip":
#         case_letters, start_i, end_i = info[0], int(info[1]), int(info[2])
#
#         if case_letters == "Upper":
#             letters_to_add = key[start_i:end_i].upper()
#             key = key[:start_i] + letters_to_add + key[end_i:]
#         elif case_letters == "Lower":
#             letters_to_add = key[start_i:end_i].lower()
#             key = key[:start_i] + letters_to_add + key[end_i:]
#
#     elif action == "Slice":
#         start_i, end_i = int(info[0]), int(info[1])
#         key = key[:start_i] + key[end_i:]
#
#     return key
#
#
# activation_key = input()
# command = input()
#
# while command != "Generate":
#     action, *info = command.split(">>>")
#
#     if action == "Contains":
#         substring = info[0]
#
#         if substring in activation_key:
#             print(f"{activation_key} contains {substring}")
#         else:
#             print("Substring not found!")
#
#     elif action == "Flip" or action == "Slice":
#         activation_key = flip_or_slice(activation_key, info, action)
#         print(activation_key)
#
#     command = input()
#
# print(f"Your activation key is: {activation_key}")
