def check_username(name):
    if 3 <= len(name) <= 16:
        if name.isalnum() or "-" in name or "_" in name:
            return True
    return False


usernames = input().split(', ')
for name in usernames:
    if check_username(name):
        print(name)
