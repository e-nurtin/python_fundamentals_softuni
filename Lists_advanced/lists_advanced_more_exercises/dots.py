def find_dots(board):
    row_dots = []
    for row, elements in enumerate(board):
        row_dots.append([])
        for index in range(len(elements)):
            if board[row][index] == '.':
                row_dots[row].append(index)
    return row_dots


#    0       1     2     3       4
# [[0, 1], [0, 1], [], [3, 4], [3, 4]]
def check_horizontal(row_dots):
    largest_count = 0
    index_dots = 0
    row = 0
    for row, elements in enumerate(board):
        if row == 0:
            for index, element in enumerate(elements):
                if element == '.':
                    if len(elements) - 1 > index:
                        if board[row + 1][index] == element or\
                                board[row][index + 1] == element:
                            largest_count += 1
                    else:
                        if board[row][index - 1] == element:
                            pass

                # [index]
        # row 0 # . . - - -
        #  1    # . . - - -
        #  2    # - - - - -
        # 3     # - - - . .
        # 4     # - - - . .


count_of_rows = int(input())
board = [list(input().split()) for x in range(count_of_rows)]

dots = find_dots(board)
check_horizontal(dots)
