countries = input().split(', ')
capitals = input().split(', ')
# countries_dict = {key: value for key, value in zip(countries, capitals)}
# countries_dict = {countries[index]: capitals[index] for index in range(len(
#     capitals))}
countries_dict = dict(zip(countries, capitals))
for key, value in countries_dict.items():
    print(f"{key} -> {value}")
