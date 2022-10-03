numbers = list(map(int,input().split(", ")))

max_value = 10
while len(numbers) != 0:
    filtered_list = list(filter(lambda x: x <= max_value, numbers))
    removed = [numbers.remove(x) for x in filtered_list]

    print(f"Group of {max_value}'s: {filtered_list}")
    max_value += 10
