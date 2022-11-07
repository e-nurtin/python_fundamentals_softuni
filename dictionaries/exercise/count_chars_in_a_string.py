string_to_count = "".join(s for s in input().split())
letter_occurences = {}

for letter in string_to_count:
    if letter not in letter_occurences:
        letter_occurences[letter] = 0
    letter_occurences[letter] += 1

for key, value in letter_occurences.items():
    print(f"{key} -> {value}")
