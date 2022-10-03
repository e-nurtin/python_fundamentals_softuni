keywords = input().split(', ')
strings_list = input().split(', ')
result = []
for keyword in keywords:
    for string in strings_list:
        if keyword in string:
            result.append(keyword)
            break
# result = [word for word in keywords
#           if any(word in string for string in strings_list)]
print(result)
