# def version_upgrade(number_1, number_2, number_3):
#     number_3 += 1
#     if number_3 > 9:
#         number_3 = 0
#         number_2 += 1
#         if number_2 > 9:
#             number_2 = 0
#             number_1 += 1
#     return str(number_1), str(number_2), str(number_3)
#
#
# current_version = list(map(int, input().split('.')))
# upgraded_to = version_upgrade(current_version[0], current_version[1],
#                                current_version[2])
#
# print(".".join(upgraded_to))


## 2
# If you want first number to continue after 9
# If not you can del row 3 and row 9
current_version = list(map(int, input().split('.')))
for index in range(len(current_version)-1, -1, -1):
    if index != 0:
        if current_version[index] + 1 > 9:
            current_version[index] = 0
            continue
        current_version[index] += 1
        break
    current_version[index] += 1
print(*current_version, sep='.')

# result = '.'.join(str(x) for x in current_version)
# print(result)


## 3
# Without using loop

current_version = list(map(int, input().split('.')))
if current_version[-1] + 1 > 9:
    current_version[-1] = 0
    current_version[-2] += 1
    if current_version[-2] > 9:
        current_version[-2] = 0
        current_version[0] += 1
else:
    current_version[-1] += 1
print(*current_version, sep='.')
