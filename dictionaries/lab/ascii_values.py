list_of_characters = input().split(", ")

# ascii_dict_of_characters = {x: ord(x) for x in list_of_characters}
ascii_dict_of_characters = {}
for char in list_of_characters:
    ascii_dict_of_characters[char] = ord(char)
print(ascii_dict_of_characters)
