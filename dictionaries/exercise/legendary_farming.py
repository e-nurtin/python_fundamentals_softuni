junk_items = {}
needed_items = {'shards': 0, 'fragments': 0, 'motes': 0}
legy_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr',
              'motes': 'Dragonwrath'}
legendary_acquired = False
while True:
    items_info = input().lower().split()
    for index in range(0, len(items_info), 2):
        material = items_info[index + 1]
        quantity = int(items_info[index])
        if material not in needed_items:
            needed_items[material] += int(quantity)
            if needed_items[material] >= 250:
                legendary_acquired = True
                needed_items[material] -= 250
                print(f"{legy_items[material]} obtained!")
                break
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity
    if legendary_acquired:
        break
for material, quantity in needed_items.items():
    print(f"{material}: {quantity}")
for material, quantity in junk_items.items():
    print(f"{material}: {quantity}")
