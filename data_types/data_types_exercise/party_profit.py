group_count = int(input())
days_count = int(input())
total_coins = 0
for day in range(1, days_count + 1):
    daily_expenses = 0
    if day % 10 == 0:
        group_count -= 2
    if day % 15 == 0:
        group_count += 5
    total_coins += 50
    daily_expenses = group_count * 2
    total_coins -= daily_expenses
    if day % 3 == 0:
        daily_expenses = group_count * 3
        total_coins -= daily_expenses
    if day % 5 == 0:
        total_coins += (group_count * 20)
        if day % 3 == 0:
            daily_expenses = group_count * 2
            total_coins -= daily_expenses
coins_per_companion = int(total_coins / group_count)
print(f"{group_count} companions received {coins_per_companion} coins each.")
