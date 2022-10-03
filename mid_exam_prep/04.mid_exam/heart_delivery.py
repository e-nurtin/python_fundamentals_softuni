neighborhood = list(map(int, input().split("@")))

places_with_valentines = []
valentines = 0
cupid_position = 0
command = input()
while command != "Love!":
    info, jump = [int(x) if x.isdigit() else x for x in command.split()]
    cupid_position += jump
    if cupid_position >= len(neighborhood):
        cupid_position = 0
        neighborhood[cupid_position] -= 2
    else:
        neighborhood[cupid_position] -= 2
    if neighborhood[cupid_position] <= 0:
        if cupid_position not in places_with_valentines:
            print(f"Place {cupid_position} has Valentine's day.")
            valentines += 1
            places_with_valentines.append(cupid_position)
        else:
            print(f"Place {cupid_position} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {cupid_position}.")
if len(places_with_valentines) == len(neighborhood):
    print("Mission was successful.")
else:
    diff = len(neighborhood) - len(places_with_valentines)
    print(f"Cupid has failed {diff} places.")