import re

message = input()


pattern = r"([#|]{1})([ a-zA-Z]+)\1([0-9][0-9]\/[0-9][0-9]\/[0-9][0-9])\1(\d+)\1"

result = re.findall(pattern, message)

# food[3] is the calories of the given food. we sum the total calories and divide them by
# 2000 to get how many days we would last with the available foods.
food_left_for_days = sum([int(food[3]) for food in result]) // 2000

print(f"You have food to last you for: {food_left_for_days} days!")
for item in result:
    item_name = item[1]
    expiration_date = item[2]
    calories = item[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
