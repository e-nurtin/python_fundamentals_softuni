def add_stop(string, index, stop):
    if 0 <= index < len(string):
        string = string[:index] + stop + string[index:]
    return string


def remove_stop(start, end, string):
    if 0 <= start and end < len(string):
        string = string[:start] + string[end + 1:]
    return string


def switch_substring(old, new, string):
    if old in string:
        string = string.replace(old, new)
    return string


initial_plan = input()

command = input()
while command != "Travel":
    action, *info = [int(x) if x.isdigit() else x for x in command.split(":")]

    if action == "Add Stop":
        initial_plan = add_stop(initial_plan, info[0], info[1])
    elif action == "Remove Stop":
        initial_plan = remove_stop(info[0], info[1], initial_plan)
    elif action == "Switch":
        initial_plan = switch_substring(info[0], info[1], initial_plan)

    print(initial_plan)

    command = input()

print(f"Ready for world tour! Planned stops: {initial_plan}")
