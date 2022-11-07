def insert_space(message, index):
    message = message[:index] + ' ' + message[index:]
    return message


def reverse(substring, message):
    if substring in message:
        message = message.replace(substring, '', 1)
        substring = substring[::-1]
        message = message + substring
        return message
    else:
        return "error"


def change_all(substring, replacement, message):
    message = message.replace(substring, replacement)
    return message


concealed_message = input()

command = input()
while command != 'Reveal':
    action, *info = [int(x) if x.isdigit() else x for x in command.split(':|:')]
    temporary_message = ""

    if action == "InsertSpace":
        temporary_message = insert_space(concealed_message, info[0])
    elif action == "Reverse":
        temporary_message = reverse(info[0], concealed_message)
    elif action == "ChangeAll":
        temporary_message = change_all(info[0], info[1], concealed_message)

    if temporary_message != "error":
        concealed_message = temporary_message

    print(temporary_message)

    command = input()

print(f"You have a new text message: {concealed_message}")
