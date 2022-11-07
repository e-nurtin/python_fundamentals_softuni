current_year = int(input()) + 1
year_as_string = str(current_year)
while len(set(year_as_string)) != len(year_as_string):
    current_year += 1
    year_as_string = str(current_year)
print(current_year)
