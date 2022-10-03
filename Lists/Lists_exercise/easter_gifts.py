gifts_as_list = input().split()
commands_list = []
index_of_gifts = []

command = input()
while command != "No Money":
    commands_list = command.split()
    if "OutOfStock" in commands_list:
        if commands_list[1] in gifts_as_list:
            for index, gift in enumerate(gifts_as_list):
                if commands_list[1] == gift:
                    index_of_gifts.append(index)
            for index in index_of_gifts:
                gifts_as_list[index] = None
    elif "Required" in commands_list:
        if 0 <= int(commands_list[2]) < len(gifts_as_list):
            gifts_as_list[int(commands_list[2])] = commands_list[1]
    elif "JustInCase" in commands_list:
        gifts_as_list[-1] = commands_list[1]
    command = input()

filtered_list = list(filter(None, gifts_as_list))
result = " ".join(filtered_list)
print(result)
