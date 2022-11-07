def check_for_moves(maze, free_spaces, kate_position):
    current_free_space = 0
    moves = 0
    while current_free_space < len(free_spaces):
        row = free_spaces[current_free_space][0]
        index = free_spaces[current_free_space][1]

        # moving right
        if row == kate_position[0] and index - kate_position[1] == 1:
            moves += 1
            kate_position = free_spaces.pop(current_free_space)
            current_free_space = 0
        # moving left
        elif row == kate_position[0] and kate_position[1] - index == 1:
            moves += 1
            kate_position = free_spaces.pop(current_free_space)
            current_free_space = 0
            # moving up
        elif index == kate_position[1] and kate_position[0] - row == 1:
            moves += 1
            kate_position = free_spaces.pop(current_free_space)
            current_free_space = 0
            # moving down
        elif index == kate_position[1] and row - kate_position[0] == 1:
            moves += 1
            kate_position = free_spaces.pop(current_free_space)
            current_free_space = 0
        else:
            current_free_space += 1

    if kate_position[0] == 0 or kate_position[1] == 0 or kate_position[0] == \
            (len(maze) - 1) or kate_position[1] == len(maze[0]):
        return f"Kate got out in {moves + 1} moves"
    return "Kate cannot get out"


def find_kate(maze):
    kate_position = []
    for row, column in enumerate(maze):
        for index, element in enumerate(column):
            if element == "k":
                kate_position.append(row)
                kate_position.append(index)
    return kate_position


def check_for_empty_space(maze):
    spaces = []
    for row in range(len(maze)):
        for index, element in enumerate(maze[row]):
            if element == " ":
                current_space = [row, index]
                spaces.insert(0, current_space)
    print(spaces)
    return spaces


maze_rows = int(input())
maze = [list(input()) for x in range(maze_rows)]

position = find_kate(maze)
empty_spaces = check_for_empty_space(maze)
result = check_for_moves(maze, empty_spaces, position)

print(result)
