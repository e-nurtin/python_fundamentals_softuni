user_input = input().split('-')
to_do = [0] * 10
while "End" not in user_input:
    # to_do.append([x for x in user_input])
    priority = int(user_input[0]) - 1
    note = user_input[1]
    to_do.pop(priority)
    to_do.insert(priority, note)
    user_input = input().split('-')
result = [x for x in to_do if x != 0]
print(result)