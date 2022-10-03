key = int(input())
count_of_characters = int(input())

for i in range(count_of_characters):
    current_character = input()
    decrypted_char = ord(current_character) + key
    print(chr(decrypted_char), end="")
