# Translate from Morse code to English.

morse_alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

# Translate from Morse code to English.

sentence = input().split(' | ')
message = ""
for word in sentence:
    characters = word.split()
    for char in characters:
        for key, value in morse_alphabet.items():
            if value == char:
                message += key
                break
    message += " "
print(message.strip())

# Translate from English to Morse code.
#
# sentence = input().upper().split()
# message = ""
#
# for word in sentence:
#     for character in word:
#         for key, value in morse_alphabet.items():
#             if key == character:
#                 message += value
#                 break
#         message += " "
#     if sentence[-1] != word:
#         message += ' | '
# print(message)
