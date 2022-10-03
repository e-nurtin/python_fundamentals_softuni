number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = int(input())
    message = ""
    if current_command == 88:
        message = "Hello"
    elif current_command == 86:
        message = "How are you?"
    elif current_command < 88:
        message = "GREAT!"
    elif current_command > 88:
        message = "Bye."
    print(message)