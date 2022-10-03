items_and_prices_list = input().split("|")
budget_start = float(input())
budget = budget_start
max_price = 0
current_item_is_sold_for = 0
profit = 0
sold_items_prices_list = []
for item in items_and_prices_list:
    current_item = []
    for element in item.split("->"):
        current_item.append(element)
    value_of_current_item = float(current_item[-1])
    if "Clothes" in current_item:
        max_price = 50.00
    elif "Shoes" in current_item:
        max_price = 35.00
    elif "Accessories" in current_item:
        max_price = 20.50
    if value_of_current_item <= max_price:
        if value_of_current_item <= budget:
            budget -= value_of_current_item
            current_item_is_sold_for = value_of_current_item * 1.4
            sold_items_prices_list.append(current_item_is_sold_for)
            profit += (value_of_current_item * 0.4)
for number in sold_items_prices_list:
    print(f"{number:.2f}", end= " ")
print()
# print(*f"{*sold_items_prices_list:.2f}")
print(f"Profit: {profit:.2f}")
if budget_start + profit >= 150.0:
    print("Hello, France!")
else:
    print("Not enough money.")