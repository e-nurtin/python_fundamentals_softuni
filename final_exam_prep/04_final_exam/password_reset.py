initial_password = input()

command = input()
while command != "Done":
    info = [int(x) if x.isdigit() else x for x in command.split()]

    if info[0] == "TakeOdd":
        new_password = ""
        for index in range(len(initial_password)):
            if index % 2 != 0:
                new_password += initial_password[index]
        initial_password = new_password
        print(initial_password)

    elif info[0] == "Cut":
        index = info[1]
        end_index = info[1] + info[2]
        substring = initial_password[index:end_index]
        initial_password = initial_password.replace(substring, "", 1)
        print(initial_password)

    elif info[0] == "Substitute":
        if info[1] in initial_password:
            initial_password = initial_password.replace(info[1], info[2])
            print(initial_password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {initial_password}")