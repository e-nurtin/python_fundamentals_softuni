def add_stats(type, name, damage, health, armor, d_d, h_d, a_d):
    dragon_data[type] = dragon_data.get(type, {})
    dragon_data[type][name] = dragon_data[type].get(name, {})
    dragon_data[type][name][d_d] = damage
    dragon_data[type][name][h_d] = health
    dragon_data[type][name][a_d] = armor



def print_result():
    for dragon_type, stats in dragon_data.items():
        avg_dmg = 0
        avg_health = 0
        avg_armor = 0
        for name, stat in stats.items():
            avg_dmg += stats[name][damage_d]
            avg_health += stats[name][health_d]
            avg_armor += stats[name][armor_d]
        print(f"{dragon_type}::({avg_dmg / len(stats):.2f}/{avg_health / len(stats):.2f}"
              f"/{avg_armor / len(stats):.2f})")

        sort_stats = dict(sorted(stats.items(), key=lambda x: x[0]))

        for name, status in sort_stats.items():
            print(f"-{name} -> damage: {status[damage_d]}, "
                  f"health: {status[health_d]}, armor: {status[armor_d]}")


dragon_data = {}
damage_d = 'damage'
health_d = 'health'
armor_d = 'armor'

count_of_dragons = int(input())

for i in range(count_of_dragons):
    dragon_type, dragon_name, dragon_damage, \
    dragon_health, dragon_armor = [int(x) if x.isdigit() else x for x in input().split()]

    if dragon_damage == 'null':
        dragon_damage = 45

    if dragon_health == 'null':
        dragon_health = 250

    if dragon_armor == 'null':
        dragon_armor = 10

    add_stats(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor,
              damage_d, health_d, armor_d)

print_result()