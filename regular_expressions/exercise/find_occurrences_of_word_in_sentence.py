import re

sentence = input()
searched_word = input()
pattern = fr"\b{searched_word}\b"
count = re.findall(pattern, sentence, flags=re.I)

print(len(count))
