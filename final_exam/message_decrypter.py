import re

count_of_messages = int(input())

validity = r"^(\$|%)(?P<tag>[A-Z][a-z]{2,})\1: (\[[0-9]+\]\|){3}$"

for _ in range(count_of_messages):
    current_message = input()

    match = re.match(validity, current_message)
    if match:
        numbers = re.findall('\d+', current_message)
        tag = match.group('tag')
        message = ''.join([chr(int(num)) for num in numbers])
        print(f"{tag}: {message}")
    else:
        print("Valid message not found!")
        