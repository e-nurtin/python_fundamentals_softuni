# sent_off_players = input().split()
#
# team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9",
#           "A-10", "A-11"]
# team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9",
#           "B-10", "B-11"]
#
# game_is_terminated = False
# for current_player in sent_off_players:
#     if current_player in team_a:
#         team_a.remove(current_player)
#     elif current_player in team_b:
#         team_b.remove(current_player)
#     if len(team_b) < 7 or len(team_a) < 7:
#         game_is_terminated = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#
# if game_is_terminated:
#     print("Game was terminated")


sent_off_players = input().split()
teams = {
    "A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "B": [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11]
}

game_is_terminated = False
for current_player in sent_off_players:
    team, number = [int(x) if x.isdigit() else x for x in current_player.split('-')]
    if number in teams[team]:
        teams[team].remove(number)
    if len(teams["A"]) < 7 or len(teams["B"]) < 7:
        game_is_terminated = True
        break

print(f"Team A - {len(teams['A'])}; Team B - {len(teams['B'])}")
if game_is_terminated:
    print("Game was terminated")
