def collect_item(item):
    if item not in inventory_items:
        inventory_items.append(item)


def drop_item(item):
    if item in inventory_items:
        inventory_items.remove(item)


def combine_items(items):
    old_item, new_item = items.split(':')
    if old_item in inventory_items:
        index = inventory_items.index(old_item)
        if index < len(inventory_items):
            inventory_items.insert(index + 1, new_item)


def renew_item(item):
    if item in inventory_items:
        inventory_items.append(inventory_items.pop(inventory_items.index(item)))


inventory_items = input().split(', ')

command = input()
while command != "Craft!":
    action, info = [x for x in command.split(' - ')]
    if action == "Collect":
        collect_item(info)
    elif action == "Drop":
        drop_item(info)
    elif action == "Combine Items":
        combine_items(info)
    elif action == "Renew":
        renew_item(info)
    command = input()

print(", ".join(inventory_items))
