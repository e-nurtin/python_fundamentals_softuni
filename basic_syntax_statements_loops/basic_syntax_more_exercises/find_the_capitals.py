word = input()
upper_indexes = []
for index, letter in enumerate(word):
    if letter.isupper():
        upper_indexes.append(index)
print(upper_indexes)
