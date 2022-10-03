lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmets_broken = lost_fights_count // 2
total_swords_broken = lost_fights_count // 3
total_shields_broken = lost_fights_count // 6
total_armor_broken = total_shields_broken // 2
expenses = total_helmets_broken * helmet_price +\
            total_swords_broken * sword_price +\
            total_shields_broken * shield_price +\
            total_armor_broken * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")

# total_repairs = 0
# shield_break_count = 0
# for current_fight in range(1, lost_fights_count + 1):
#     if current_fight % 2 == 0:
#         total_repairs += helmet_price
#         if current_fight % 3 == 0:
#             shield_break_count += 1
#             total_repairs += shield_price
#             if shield_break_count == 2:
#                 shield_break_count = 0
#                 total_repairs += armor_price
#     if current_fight % 3 == 0:
#         total_repairs += sword_price
# print(f"Gladiator expenses: {total_repairs:.2f} aureus")
