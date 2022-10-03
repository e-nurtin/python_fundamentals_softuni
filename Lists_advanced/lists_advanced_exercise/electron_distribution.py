def shell_capacity(number):
    shells_filled = []
    level_of_shell = 1
    while number > 0:
        shell_cap = 2 * (level_of_shell ** 2)
        if shell_cap <= number:
            shells_filled.append(shell_cap)
            number -= shell_cap
        else:
            shells_filled.append(number)
            number -= number
        level_of_shell += 1
    return shells_filled


number_of_electrons = int(input())
print(shell_capacity(number_of_electrons))