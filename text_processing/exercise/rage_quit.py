rage_text = input().upper()
fixed_text = ""
index = -1
count_of_unique_symbols = 0
while len(rage_text) > 0:
    index += 1
    symbol = rage_text[index]
    count_of_repeats = ""

    if symbol.isdigit():
        count_of_repeats += symbol

        if index + 1 < len(rage_text) and rage_text[index + 1].isdigit():
            count_of_repeats += rage_text[index + 1]

        fixed_text += rage_text[:index] * int(count_of_repeats)
        rage_text = rage_text[index + len(count_of_repeats):]
        index = -1


print(f"Unique symbols used: {len(set(fixed_text))}")
print(fixed_text)
