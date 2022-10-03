def merge(item, action):
    start_index = int(action[1])
    end_index = int(action[2])
    if start_index < 0:
        start_index = 0
    if start_index < end_index:
        if end_index >= len(item):
            end_index = len(item) - 1
        for index in range(start_index, end_index):
            item[start_index] += f"{item.pop(start_index + 1)}"
    return item


def divide(item, action):
    index_to_divide = int(action[1])
    pieces = int(action[2])
    length_of_each_element = len(item[index_to_divide]) // pieces
    current_element = item.pop(index_to_divide)
    for element in range(1, pieces + 1):
        if element < pieces:
            piece = current_element[:length_of_each_element]
            current_element = current_element[length_of_each_element:]
            item.insert(index_to_divide, piece)
            index_to_divide += 1
        else:
            item.insert(index_to_divide, current_element)
    return item


input_line = input().split()
command = input().split()
while len(command) > 2:
    if command[0] == "merge":
        result = merge(input_line, command)
    elif command[0] == "divide":
        result = divide(input_line, command)

    command = input().split()
print(" ".join(result))
