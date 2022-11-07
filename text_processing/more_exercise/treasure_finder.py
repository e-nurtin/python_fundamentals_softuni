def decrypt_message(crypted_message, keys):
    decrypted_string = ""
    index = 0
    for character in crypted_message:
        if index == len(keys):
            index = 0
        decrypted_string += chr(ord(character) - keys[index])
        index += 1
    return decrypted_string


def find_keywords(decrypted, symbol):
    start = message.find(symbol)
    if symbol == '<':
        symbol = '>'
    end = message.find(symbol, start + 1, -1)
    found = decrypted[start + 1: end]
    return found


# keys = list(map(int, input().split()))
keys = [int(x) for x in input().split()]

command = input()
while command != "find":

    message = decrypt_message(command, keys)
    type_of_element = find_keywords(message, '&')
    coordinates = find_keywords(message, '<')

    print(f"Found {type_of_element} at {coordinates}")

    command = input()
