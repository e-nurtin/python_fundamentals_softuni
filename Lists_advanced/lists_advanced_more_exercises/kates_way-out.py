def maze_check_for_moves(maze: list, kate_r, kate_i, count_moves):
    for element in maze[row]:
        if element == " ":
            move = maze.index(element, 0, -1)
            print(move)

maze_rows = int(input())

# rows = []
# for i in range(maze_rows):
#     current_row = input()
#     rows.append(current_row)
kate_index = 0
kate_row = 0
kate_is_found = False
maze = [list(input()) for x in range(maze_rows)]
for row, column in enumerate(maze):
    for index, element in enumerate(column):
        if element == "k":
            kate_index = index
            kate_row = row
            kate_is_found = True
moves = 0
if kate_is_found:
    maze_check_for_moves(maze,kate_row,kate_index,moves)
print(kate_row)
print(kate_index)
