import re

message = input()

# pattern = r"[#|]{1}([ a-zA-Z]*)[#|]{1}(\d{2}\/\d{2}\/\d{2})[#|]{1}(\d+)[#|]{1}"
pattern = r"([#|]{1})([ a-zA-Z]+)\1([0-9][0-9]\/[0-9][0-9]\/[0-9][0-9])\1(\d+)\1"

result = re.findall(pattern, message)

food_left_for_days = sum([int(x[3]) for x in result]) // 2000

print(f"You have food to last you for: {food_left_for_days} days!")
for item in result:
    item_name = item[1]
    expiration_date = item[2]
    calories = item[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
