import re

cool_threshold = 1
cool_emojis = []
pattern = r"(::|\*\*)([A-Z]{1}[a-z]{2,})\1"
digits_pattern = r"\d"

text = input()

digits = re.findall(digits_pattern, text)
for number in digits:
    cool_threshold *= int(number)

emojis = re.findall(pattern, text)
for index in range(len(emojis)):
    emoji_coolness = 0
    current_emoji = emojis[index][1]

    for symbol in current_emoji:
        emoji_coolness += ord(symbol)

    if emoji_coolness >= cool_threshold:
        cool_emojis.append(f"{emojis[index][0]}{emojis[index][1]}{emojis[index][0]}")


print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
print('\n'.join(cool_emojis))
