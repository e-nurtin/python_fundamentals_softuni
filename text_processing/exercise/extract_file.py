path = input().split('\\')
string = ''

for item in path:
    if '.' in item:
        string = item

index = string.find('.')

file_name = string[:index]
file_extension = string[index + 1:]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
