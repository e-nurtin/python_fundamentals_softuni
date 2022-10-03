
number_of_commands = int(input())
all_brackets = ""
last_bracket = "("
opening = 0
brackets_are_balanced = True
for i in range(1, number_of_commands + 1):
    current_command = input()
    if current_command == "(" or current_command == ")":
        all_brackets += current_command

for current_index, symbol in enumerate(all_brackets):
    if current_index == 0 and symbol != "(":
        brackets_are_balanced = False
        break
    if last_bracket != symbol:
        last_bracket = symbol
        brackets_are_balanced = True
    else:
        brackets_are_balanced = False
        break

if brackets_are_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
