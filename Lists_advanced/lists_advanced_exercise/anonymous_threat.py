input_data = input().split(" ")

command = input()
while command != "3:1":
	action, *info = [x if x.isalpha() else int(x) for x in command.split(" ")]

	if action == "merge":
		start_index = info[0] if 0 <= info[0] < len(input_data) else 0
		end_index = info[1] if 0 <= info[1] < len(input_data) else len(input_data) - 1
		input_data = input_data[:start_index] + [''.join(input_data[start_index: end_index + 1])] + input_data[end_index + 1:]

	elif action == "divide":
		partitions, index = info[1], info[0]
		word_to_divide = input_data.pop(index)
		elements_per_part = len(word_to_divide) // partitions

		for i in range(1, partitions + 1):
			if i < partitions:
				input_data.insert(index + i, word_to_divide[:elements_per_part])
				word_to_divide = word_to_divide[elements_per_part:]
				index += 1
			else:
				input_data.insert(index, word_to_divide)

	command = input()

print(' '.join(input_data))



# def merge(start_index, end_index):
#     if start_index < 0:
#         start_index = 0
#     if start_index < end_index:
#         if end_index >= len(list_of_strings):
#             end_index = len(list_of_strings) - 1
#         for index in range(start_index, end_index):
#             list_of_strings[start_index] += list_of_strings.pop(start_index + 1)


# def divide(index, partitions):
#     piece_to_divide = list_of_strings.pop(index)
#     length_of_piece = len(piece_to_divide) // partitions
#     for partition in range(1, partitions + 1):
#         if partition < partitions:
#             list_of_strings.insert(index, piece_to_divide[:length_of_piece])
#             piece_to_divide = piece_to_divide[length_of_piece:]
#             index += 1
#         else:
#             list_of_strings.insert(index, piece_to_divide)


# list_of_strings = input().split()
# command = input()
# while command != "3:1":
#     action, start, pieces = [x if x.isalpha() else int(x) for x in command.split()]
#     if action == "merge":
#         merge(start, pieces)
#     elif action == "divide":
#         divide(start, pieces)
#     command = input()
# result = ' '.join(list_of_strings)
# print(result)
