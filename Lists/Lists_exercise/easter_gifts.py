# gifts_as_list = input().split()
# commands_list = []
# index_of_gifts = []
#
# command = input()
# while command != "No Money":
#     commands_list = command.split()
#     if "OutOfStock" in commands_list:
#         if commands_list[1] in gifts_as_list:
#             for index, gift in enumerate(gifts_as_list):
#                 if commands_list[1] == gift:
#                     index_of_gifts.append(index)
#             for index in index_of_gifts:
#                 gifts_as_list[index] = None
#     elif "Required" in commands_list:
#         if 0 <= int(commands_list[2]) < len(gifts_as_list):
#             gifts_as_list[int(commands_list[2])] = commands_list[1]
#     elif "JustInCase" in commands_list:
#         gifts_as_list[-1] = commands_list[1]
#     command = input()
#
# filtered_list = list(filter(None, gifts_as_list))
# result = " ".join(filtered_list)
# print(result)

def out_of_stock(out_of_stock_gift):
    for gift in gifts_to_buy:
        if gift == out_of_stock_gift:
            gifts_to_buy[gifts_to_buy.index(gift)] = "None"


def required(gift, index):
    if 0 <= index < len(gifts_to_buy):
        gifts_to_buy[index] = gift


def just_in_case(gift):
    gifts_to_buy[-1] = gift


gifts_to_buy = input().split()

command = input()
while command != "No Money":
    action, *info = [x if x.isalpha() else int(x) for x in command.split()]

    if action == "OutOfStock":
        out_of_stock(info[0])
    elif action == "Required":
        required(info[0], info[1])
    elif action == "JustInCase":
        just_in_case(info[0])

    command = input()

result = list(filter(lambda x: x != "None", gifts_to_buy))
print(' '.join(result))
