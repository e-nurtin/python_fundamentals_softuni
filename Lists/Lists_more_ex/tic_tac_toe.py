# first_line = input().split()
# second_line = input().split()
# third_line = input().split()
# board_list = []
# first_player = []
# second_player = []
# first_player_won = False
# second_player_won = False
# winning_combination = [[0, 1, 2],
#                        [3, 4, 5],
#                        [6, 7, 8],
#                        [0, 3, 6],
#                        [1, 4, 7],
#                        [2, 5, 8],
#                        [0, 4, 8],
#                        [2, 4, 6],
#                        ]
# for player in first_line:
#     board_list.append(player)
# for player in second_line:
#     board_list.append(player)
# for player in third_line:
#     board_list.append(player)
#
# for index, element in enumerate(board_list):
#     if "1" in element:
#         first_player.append(index)
#     elif "2" in element:
#         second_player.append(index)
#
# for combination in winning_combination:
#     if combination == first_player:
#         first_player_won = True
#         break
#     elif combination == second_player:
#         second_player_won = True
#         break
# if first_player_won:
#     print("First player won")
# elif second_player_won:
#     print("Second player won")
# else:
#     print("Draw!")
#
#
#


def check_for_win(combinations, board, player):
    for combination in combinations:
        count = 0
        for index in combination:
            if board[index] == player:
                count += 1
                if count == 3:
                    return True
    return False


first_line = input().split()
second_line = input().split()
third_line = input().split()
board_list = []
board_list.extend(first_line)
board_list.extend(second_line)
board_list.extend(third_line)

winning_combination = [[0, 1, 2],
                       [3, 4, 5],
                       [6, 7, 8],
                       [0, 3, 6],
                       [1, 4, 7],
                       [2, 5, 8],
                       [0, 4, 8],
                       [2, 4, 6],
                       ]
if check_for_win(winning_combination, board_list, '1'):
    print("First player won")
elif check_for_win(winning_combination,board_list, '2'):
    print("Second player won")
else:
    print("Draw!")