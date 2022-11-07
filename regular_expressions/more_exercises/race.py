import re


def ordinal_number(number):
    value = str(number)
    if len(value) > 1:
        second_to_last_value = value[-2]
        if second_to_last_value == '1':
            return 'th'
    last_digit = value[-1]
    if last_digit == '1':
        return 'st'
    elif last_digit == '2':
        return 'nd'
    elif last_digit == '3':
        return 'rd'
    else:
        return 'th'


list_of_participants = input().split(', ')
data = {}
pattern_for_digits = r"[\d]"

command_line = input()
while command_line != "end of race":
    current_racer = ""
    current_racer_distance = 0
    for participant in list_of_participants:

        pattern_for_name = r"[^\d\W\s\_]"
        current_racer = re.findall(pattern_for_name, command_line)

        if participant in ''.join(current_racer):
            current_racer_digits = re.findall(pattern_for_digits, command_line)

            for digit in current_racer_digits:
                current_racer_distance += int(digit)

            if participant in data:
                data[participant] += current_racer_distance
            else:
                data[participant] = current_racer_distance

    command_line = input()


for position, (name, distance) in enumerate(sorted(data.items(), key=lambda x: -x[1]), 1):
    print(f"{position}{ordinal_number(position)} place: {name}")
    if position == 3:
        break


