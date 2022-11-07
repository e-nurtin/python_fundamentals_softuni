import re

numbers_to_search = input()

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

result = re.finditer(pattern, numbers_to_search)

for number in result:
    print(number.group(), end=' ')
