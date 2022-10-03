# def decipher(secret_word):
#     index = 0
#     for x in secret_word:
#         num = ""
#         message = ""
#         for character in secret_word[index]:
#             if character.isdigit():
#                 num += character
#             else:
#                 message += character
#         if len(message) > 1:
#             message = message[-1:] + message[1:-1] + message[0]
#             secret_word[index] = chr(int(num)) + message
#         secret_word[index] = chr(int(num)) + message
#         index += 1
#     return secret_word


secret_message = input().split()
deciphered_message = []
# print(' '.join(decipher(secret_message)))
for word in secret_message:
    number = [x for x in word if x.isdigit()]
    characters = [x for x in word if not x.isdigit()]
    ascii_char = [chr(int(''.join(number)))]
    current_word = ascii_char + characters
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    deciphered_message.append(''.join(current_word))
print(' '.join(deciphered_message))
