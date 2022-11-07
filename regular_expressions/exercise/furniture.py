import re

# total_price = 0
# pattern = r"\b(?<=(>>))([a-z]+)(?=(<<))<<(\d+[\.\d]*)!(\d+[\.\d]*)\b"
#
# items_bought = []
# command = input()
#
# while command != "Purchase":
#
#     furniture = re.findall(pattern, command, flags=re.I)
#
#     if furniture:
#         items_bought.append(furniture[0][1])
#         price = float(furniture[0][3])
#         quantity = float(furniture[0][-1])
#         total_price += price * quantity
#
#     command = input()
#
# print(f"Bought furniture:")
# for item in items_bought:
#     print(item)
# print(f"Total money spend: {total_price:.2f}")

import re
total_price = 0
pattern = r">{2}([a-zA-Z]+)<{2}(\d+\.?\d+)!(\d+)\b"

items_bought = []
command = input()

while command != "Purchase":

    match = re.match(pattern, command)

    if match:
        furniture, price, quantity = match.groups()
        items_bought.append(furniture)
        total_price += float(price) * float(quantity)

    command = input()

print(f"Bought furniture:")
for item in items_bought:
    print(item)
print(f"Total money spend: {total_price:.2f}")