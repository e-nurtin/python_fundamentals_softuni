import re
phone_numbers = input()

valid_numbers_filter = r"\+359-2-[\d]{3}-[\d]{4}\b|\+359 2 [\d]{3} [\d]{4}\b"

result = re.findall(valid_numbers_filter, phone_numbers)

print(', '.join(result))
