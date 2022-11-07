import re

text = input()

# pattern = r"(#|@)([a-zA-Z]{3,})\1(#|@)([a-zA-Z]{3,})\1"
pattern = r"(#|@)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
result = re.findall(pattern, text)
valid_words = []

for index in range(len(result)):
    word_one = result[index][1]
    word_two = result[index][2]
    if word_one == word_two[::-1]:
        valid_words.append(f"{word_one} <=> {word_two}")

if result:
    print(f"{len(result)} word pairs found!")
else:
    print("No word pairs found!")

if valid_words:
    print("The mirror words are:")
    print(', '.join(valid_words))
else:
    print("No mirror words!")