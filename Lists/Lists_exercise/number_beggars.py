presents_for_beggars_string = input()
count_of_beggars = int(input())
list_of_presents = presents_for_beggars_string.split(", ")
list_of_beggars = []
beggar = 0
current_index = 0
for i in range(1, count_of_beggars + 1):
    list_of_beggars.append(0)
while len(list_of_presents) > current_index:
    for current_beggar in range(count_of_beggars):
        if current_index < len(list_of_presents):
            list_of_beggars[current_beggar] += int(list_of_presents[current_index])
            current_index += 1
        else:
            if len(list_of_beggars) < count_of_beggars:
                list_of_beggars.append(0)
            current_index += 1
print(list_of_beggars)
