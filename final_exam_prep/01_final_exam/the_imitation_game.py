def move(string, number):
    string = string[number:] + string[:number ]
    return string


def insert(string, index, value):
    string = string[:index] + value + string[index :]
    return string


def change_all(string, substring, replacement):
    string = string.replace(substring, replacement)
    return string


message = input()

command = input()
while command != "Decode":
    action, *info = [int(x) if x.isdigit() else x for x in command.split('|')]

    if action == "Move":
        message = move(message, info[0])
    elif action == "Insert":
        message = insert(message, info[0], info[1])
    elif action == "ChangeAll":
        message = change_all(message, info[0], info[1])

    command = input()

print(f"The decrypted message is: {message}")
