def merge(start_index, end_index):
    if start_index < 0:
        start_index = 0
    if start_index < end_index:
        if end_index >= len(list_of_strings):
            end_index = len(list_of_strings) - 1
        for index in range(start_index, end_index):
            list_of_strings[start_index] += list_of_strings.pop(start_index + 1)


def divide(index, partitions):
    piece_to_divide = list_of_strings.pop(index)
    length_of_piece = len(piece_to_divide) // partitions
    for partition in range(1, partitions + 1):
        if partition < partitions:
            list_of_strings.insert(index, piece_to_divide[:length_of_piece])
            piece_to_divide = piece_to_divide[length_of_piece:]
            index += 1
        else:
            list_of_strings.insert(index, piece_to_divide)


list_of_strings = input().split()
command = input()
while command != "3:1":
    action, start, pieces = [x if x.isalpha() else int(x) for x in command.split()]
    if action == "merge":
        merge(start, pieces)
    elif action == "divide":
        divide(start, pieces)
    command = input()
result = ' '.join(list_of_strings)
print(result)
