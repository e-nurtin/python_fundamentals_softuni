import re

dates = input()

search_pattern = r'\b(\d{2})([\/.-])([A-Z]{1}[a-z]{2})\2(\d{4})\b'

found_valid_dates = re.findall(search_pattern, dates)

for date in found_valid_dates:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")