# import re
#
# places = input()
# travel_points = 0
# valid_places = []
# pattern = r"(=|\/{1})([A-Z]{1}[A-Za-z]{2,})\1"
# result = re.findall(pattern, places)
#
# if result:
#     valid_places = [x[1] for x in result]
#     for place in valid_places:
#         travel_points += len(place)
#
# print(f"Destinations: {', '.join(valid_places)}")
# print(f"Travel Points: {travel_points}")

import re

pattern = r"(=|\/)(?P<place>[A-Z][A-Za-z]{2,})\1"
text = input()

result = re.findall(pattern, text)

print(f"Destinations: {', '.join([match[1] for match in result])}")
print(f"Travel Points: {sum([len(match[1]) for match in result])}")
