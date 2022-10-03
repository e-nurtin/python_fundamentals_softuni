def version_upgrade(number_1, number_2, number_3):
    number_3 += 1
    if number_3 > 9:
        number_3 = 0
        number_2 += 1
        if number_2 > 9:
            number_2 = 0
            number_1 += 1
    return str(number_1), str(number_2), str(number_3)


current_version = list(map(int, input().split('.')))
upgraded_to = version_upgrade(current_version[0], current_version[1],
                               current_version[2])

print(".".join(upgraded_to))
