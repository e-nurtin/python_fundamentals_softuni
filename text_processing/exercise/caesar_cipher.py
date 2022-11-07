string_to_cipher = input()
ascii_code = 0
ciphered_string = ""
for symbol in string_to_cipher:
    ciphered_string += chr(ord(symbol) + 3)
print(ciphered_string)
