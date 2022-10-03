def add_urgent(item):
        shopping_list.insert(0, item)


def remove_unnecessary(item):
        shopping_list.remove(item)


def correct_item(old_item, new_item):
        index = shopping_list.index(old_item)
        shopping_list[index] = new_item


def rearrange_to_last(item):
        index = shopping_list.index(item)
        shopping_list.append(shopping_list[index])
        shopping_list.pop(index)


shopping_list = input().split('!')

command = input()
while command != "Go Shopping!":
    action, *info = [x for x in command.split()]
    if action == "Urgent" and info[0] not in shopping_list:
        add_urgent(info[0])
    elif action == "Unnecessary" and info[0] in shopping_list:
        remove_unnecessary(info[0])
    elif action == "Correct" and info[0] in shopping_list:
        correct_item(info[0], info[1])
    elif action == "Rearrange" and info[0] in shopping_list:
        rearrange_to_last(info[0])

    command = input()
print(', '.join(shopping_list))