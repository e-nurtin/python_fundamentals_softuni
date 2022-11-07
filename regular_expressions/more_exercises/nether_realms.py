import re


def calc_health(symbols):
    current_health = 0
    for char in symbols:
        current_health += ord(char)
    return current_health


def calc_damage(nums, arith):
    total_sum = sum(list(map(float, nums)))
    for symbol in arith:
        if symbol == '/':
            total_sum /= 2
        elif symbol == '*':
            total_sum *= 2
    return total_sum


data = {}
demons = input().split(',')

letters_pattern = r"[^0-9\+\-\*\/\.\s\,]"
numbers_pattern = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
arithmetic_pattern = r"[\*\/]"

for i in demons:
    demon = i.strip()

    result = re.findall(letters_pattern, demon)
    letters = ''.join(result)

    if demon not in data:
        data[demon] = {}
        data[demon]['health'] = 0
        data[demon]['damage'] = 0

    #  Calculate health and add it to the dictionary.
    health = calc_health(letters)
    data[demon]['health'] = health

    # Find numbers, multiply or divide and add it to dictionary.
    numbers = re.findall(numbers_pattern, demon)
    arithmetics = re.findall(arithmetic_pattern, demon)
    damage = calc_damage(numbers, arithmetics)
    data[demon]['damage'] = damage

for name, info in sorted(data.items()):
    print(f"{name} - {data[name]['health']} health, {data[name]['damage']:.2f} damage")

