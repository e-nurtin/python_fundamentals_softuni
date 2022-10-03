quantity_of_decoration = int(input())
days_left_until = int(input())
ornaments = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
christmas_spirit = 0
total_cost = 0
for day in range(1, days_left_until + 1):
    if day % 11 == 0:
        quantity_of_decoration += 2
    if day % 2 == 0:
        total_cost += ornaments * quantity_of_decoration
        christmas_spirit += 5
    if day % 3 == 0:
        total_cost += (tree_skirt + tree_garland) * quantity_of_decoration
        christmas_spirit += 10 + 3
    if day % 5 == 0:
        total_cost += tree_lights * quantity_of_decoration
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_skirt + tree_garland + tree_lights

if days_left_until % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")