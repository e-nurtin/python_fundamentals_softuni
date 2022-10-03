names_list = input().split(', ')

result = sorted(names_list, key=lambda name: (-len(name), name))
print(result)
