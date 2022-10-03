def characters_in_between(char_one, char_two):
    characters = []
    for char in range(ord(char_one) + 1, ord(char_two)):
        characters.append(chr(char))
    return characters


character_one = input()
character_two = input()
result = characters_in_between(character_one, character_two)
print(" ".join(result))
