count_of_actions = int(input())
parked_users = {}
for i in range(count_of_actions):
    action, *info = [x for x in input().split()]
    user = info[0]
    if action == "register":
        license_plate = info[1]
        if user not in parked_users:
            parked_users[user] = license_plate
            print(f"{user} registered {license_plate} successfully")
        elif license_plate == parked_users[user]:
            print(f"ERROR: already registered with plate number "
                  f"{parked_users[user]}")
        elif license_plate != parked_users[user]:
            parked_users[user] = license_plate
    elif action == "unregister":
        if user not in parked_users:
            print(f"ERROR: user {user} not found")
        else:
            del parked_users[user]
            print(f"{user} unregistered successfully")

for user, plate in parked_users.items():
    print(f"{user} => {plate}")
print(parked_users)