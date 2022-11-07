def find_kate(graph):
    for row in range(len(graph)):
        for column in range(len(graph[row])):
            if graph[row][column] == "k":
                k_position = [row, column]
                return k_position


def path_is_valid(pos_col, pos_row, graph):
    if 0 <= pos_row < len(graph[0]) and 0 <= pos_col < len(graph):
        return True
    return False


def check_for_exit(position, graph):
    row, column = position[0], position[1]
    if (0 == row) or \
            ((len(graph) - 1) == row) or \
            (column == (len(graph[0]) - 1)) or \
            column == 0:
        return True
    return False


def move_kate(position, graph, count):
    horizontal = [1, -1, 0, 0]
    vertical = [0, 0, 1, -1]
    pos_row = position[0]
    pos_col = position[1]
    for move in range(len(horizontal)):
        # check for index validation. eg if index is inside graph
        if path_is_valid(pos_row + horizontal[move], pos_col + vertical[move], graph):
            # check for possible vertical moves
            if graph[pos_row + vertical[move]][pos_col] == " ":
                # Update Maze
                graph[pos_row][pos_col] = "v"
                graph[pos_row + vertical[move]][pos_col] = "k"
                # Change position
                position = [pos_row + vertical[move], pos_col]
                count += 1
            # check for possible horizontal moves
            if graph[pos_row][pos_col + horizontal[move]] == " ":
                # Update Maze
                graph[pos_row][pos_col] = "v"
                graph[pos_row][pos_col + horizontal[move]] = "k"
                # Change position
                position = [pos_row, pos_col + horizontal[move]]
                count += 1

    return position, count, graph


def clear_last_visit(graph, last_position):
    graph[last_position[0]][last_position[1]] = " "
    return graph


count_of_rows = int(input())
maze = [list(input()) for x in range(count_of_rows)]
moves = []
move = 0
current_position = find_kate(maze)
kate_escapes = False
last_position = []

while last_position != current_position:
    last_position = current_position
    current_position, move, maze = move_kate(current_position, maze, move)
    maze = clear_last_visit(maze, last_position)
    print(maze)
    if check_for_exit(current_position, maze):

        moves.append(move)
        move = 0
        continue


if kate_escapes:
    print(f"Kate got out in {move + 1} moves")
else:
    print("Kate cannot get out")
