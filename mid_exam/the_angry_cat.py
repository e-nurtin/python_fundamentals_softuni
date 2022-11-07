def expensive_item_check(entry, items):
    expensive_item = 0
    for number in items:
        if entry <= number:
            expensive_item += number
    return expensive_item


def cheap_item_check(entry, items):
    cheaper_item = 0
    for number in items:
        if entry > number:
            cheaper_item += number
            if cheaper_item > entry:
                cheaper_item -= number
                break
    return cheaper_item


def compare_items(left_side, right_side):
    if left_side >= right_side:
        to_print = f"Left - {left_side_dmg}"
    else:
        to_print = f"Right - {right_side_dmg}"
    return to_print


price_ratings = list(map(int, input().split(', ')))
entry_point = int(input())
type_of_item = input()

left_side_items = price_ratings[entry_point - 1::-1]
right_side_items = price_ratings[entry_point + 1:]
entry_point = price_ratings[entry_point]

left_side_dmg = 0
right_side_dmg = 0
damage_done = ""

if type_of_item == "expensive":
    left_side_dmg = expensive_item_check(entry_point, left_side_items)
    right_side_dmg = expensive_item_check(entry_point, right_side_items)
    damage_done = compare_items(left_side_dmg, right_side_dmg)

elif type_of_item == "cheap":
    left_side_dmg = cheap_item_check(entry_point, left_side_items)
    right_side_dmg = cheap_item_check(entry_point, right_side_items)
    damage_done = compare_items(left_side_dmg, right_side_dmg)

print(damage_done)
