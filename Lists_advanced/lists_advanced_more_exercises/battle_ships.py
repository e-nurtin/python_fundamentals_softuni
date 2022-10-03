rows_of_field = int(input())

# battlefield = []
# for row in range(rows_of_field):
#     battlefield.append(list(map(int, input().split())))
# same thing with comprehension
battlefield = [list(map(int, input().split())) for x in range(rows_of_field)]
attacks = input().split()
ships_destroyed = 0
for attack in attacks:
    current_attack = attack.split('-')
    row = int(current_attack[0])
    ship = int(current_attack[1])
    if battlefield[row][ship] > 0:
        battlefield[row][ship] -= 1
        if battlefield[row][ship] == 0:
            ships_destroyed += 1
print(ships_destroyed)
