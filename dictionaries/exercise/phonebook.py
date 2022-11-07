phonebook = {}
command = input().split('-')
while command[0].isalpha():
    phonebook[command[0]] = command[1]

    command = input().split('-')

for i in range(int(command[0])):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")